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

def DocFactory(obj, types=[u'function', u'class', u'module'], *args, **kwargs):

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

	returns:
		A doc object.
	"""

	if u'function' in types and inspect.isfunction(obj) or \
		inspect.ismethod(obj):
		from yamldoc._functiondoc import FunctionDoc
		return FunctionDoc(obj, *args, **kwargs)
	if u'class' in types and inspect.isclass(obj):
		from yamldoc._classdoc import ClassDoc
		return ClassDoc(obj, *args, **kwargs)
	if u'module' in types and inspect.ismodule(obj):
		from yamldoc._moduledoc import ModuleDoc
		return ModuleDoc(obj, *args, **kwargs)
	return None

