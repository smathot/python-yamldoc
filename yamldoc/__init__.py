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

---
desc: |
	v%-- python: "from yamldoc import version; print version" --%

	*Copyright 2014 Sebastiaan Mathôt* (<http://www.cogsci.nl/smathot>)

	__About yamldoc:__

	With `yamldoc` you can take Python docstrings to the next level.

	-	A systematic YAML-based docstring notation.
	-	Generates markdown-formatted documentation for modules, classes, and
		functions.
	-	Automatically validate input and output of functions and methods.

	__Index:__

	%--
	toc:
		mindepth: 1
		maxdepth: 2
		exclude: [Index]
	--%

example: |
	%-- include: examples/example.py --%
---
"""

version = u'0.1.0'

from _basedoc import BaseDoc
from _functiondoc import FunctionDoc
from _classdoc import ClassDoc
from _moduledoc import ModuleDoc
from _docfactory import DocFactory
from _validate import validate
