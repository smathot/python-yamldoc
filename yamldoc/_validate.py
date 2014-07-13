#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
This file is part of YAMLDoc.

YAMLDoc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

YAMLDoc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with YAMLDoc.  If not, see <http://www.gnu.org/licenses/>.
"""

import inspect
from yamldoc._functiondoc import FunctionDoc
from yamldoc._exceptions import InvalidReturnValue, InvalidArgument, \
	InvalidKeyword

def checkVal(val, spec):

	"""
	desc:
		Checks whether a value matches a value specification.

	arguments:
		val:		A value to check.
		spec:
			desc:	A value specification.
			type:	dict

	returns:
		desc:		True if the value is valid, False otherwise.
		type:		bool
	"""

	if u'type' in spec:
		_type = type(val)
		if val.__class__.__name__ in spec[u'type']:
			return True
		return False
	return True

def validate(func):

	"""
	desc:
		A decorator to validate arguments and return values for a function or
		method. This decorator allows you to fully specify and check the input
		and output of a function or method through a properly formatted
		docstring.

	example: |

		import yamldoc

		@yamldoc.validate
		def test(a):

			\"\"\"
			desc:
				Example function.

			arguments:
				a:
					desc:	An argument that should be integer.
					type:	int

			returns:
				desc:		The function should return a boolean.
				type:		bool
			\"\"\"

			return True

	arguments:
		func:
			desc:	The function to validate.
			type:	[function, method]
	"""

	def inner(*args, **kwargs):

		"""
		desc:
			The decorator inner function that checks the arguments and return
			value for the function.

		argument-list:
			args:	A list of arguments to be passed to the function.

		keyword-dict:
			kwargs:	A list of keywords to be passed to the function.

		returns:
			The function's return value.
		"""


		# First check all arguments. Because keywords can also be passed as
		# regular arguments, we treat these as regular arguments as well.
		argSpec = []
		if u'arguments' in inner._dict:
			argSpec += inner._dict[u'arguments'].values()
		if u'keywords' in inner._dict:
			argSpec += inner._dict[u'keywords'].values()
		# Ignore the self argument for methods
		_args = list(args)
		if inner.__argspec__.args != None and inner.__argspec__.args[0] == \
			u'self':
			_args = _args[1:]
		if len(_args) > len(argSpec):
			raise InvalidArgument(
				u'%s(): Too many arguments. Expecting at most %d.' \
				% (func.__name__, len(argSpec)))
		for i in range(len(_args)):
			if not checkVal(_args[i], argSpec[i]):
				raise InvalidArgument(
					u'%s(): Argument %s should be of type(s) %s, not %s.' \
					% (func.__name__, i+1, argSpec[i][u'type'],
					_args[i].__class__.__name__))
		# Next check the keyword arguments
		kwSpec = {}
		if u'keywords' in inner._dict:
			kwSpec.update(inner._dict[u'keywords'])
		for kw, val in kwargs.items():
			if kw not in kwSpec:
				raise InvalidKeyword(u'%s(): Unexpected keyword: %s' \
					% (func.__name__, kw))
			if not checkVal(kwargs[kw], kwSpec[kw]):
				raise InvalidKeyword(
					u'%s(): Keyword %s should be of type(s) %s, not %s.' \
					% (func.__name__, kw, kwSpec[kw][u'type'],
					val.__class__.__name__))
		# Call the function
		retVal = func(*args, **kwargs)
		# Check the return value
		if u'returns' in inner._dict:
			if not checkVal(retVal, inner._dict[u'returns']):
				raise InvalidReturnValue(
					u'%s(): Return value should be of type(s) %s, not %s' \
					% (func.__name__, inner._dict[u'returns'][u'type'],
					retVal.__class__.__name__))
		return retVal

	# We need to copy the docstring and argument specification, otherwise using
	# this decorator will break the documentation functions.
	inner.__doc__ = func.__doc__
	inner.__argspec__ = inspect.getargspec(func)
	inner._dict = FunctionDoc(func)._dict()
	return inner
