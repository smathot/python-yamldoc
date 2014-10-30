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

import types
import inspect

def DocFactory(obj, types=[u'function', u'class', u'module', u'property'],
	*args, **kwargs):

	"""
	desc:
		Creates a type-specific doc object.

	example: |

		import yamldoc
		
		# Create a type-specific docstring processor for `myFunction`.
		df = yamldoc.DocFactory(myFunction)
		# Get a markdown-style formatted docstring and print it.
		md = unicode(df)
		print md

	arguments:
		obj:	The object to document.

	keywords:
		types:
			desc:	A list of types that should be documented.
			type:	list

	argument-list:
		See [BaseDoc.__init__] for a description of available arguments.

	keyword-dict:
		See [BaseDoc.__init__] for a description of available keywords.

	returns:
		A doc object.
	"""

	if u'function' in types and inspect.isfunction(obj) or \
		inspect.ismethod(obj):
		from yamldoc._functiondoc import FunctionDoc as Doc
	elif u'class' in types and inspect.isclass(obj):
		from yamldoc._classdoc import ClassDoc as Doc
	elif u'module' in types and inspect.ismodule(obj):
		from yamldoc._moduledoc import ModuleDoc as Doc
	elif u'property' in types and type(obj) == property:
		from yamldoc._propertydoc import PropertyDoc as Doc
	else:
		return None
	return Doc(obj, *args, **kwargs)
