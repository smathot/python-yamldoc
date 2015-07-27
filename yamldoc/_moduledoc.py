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

from yamldoc.py3compat import *
from yamldoc._basedoc import BaseDoc
from yamldoc._docfactory import DocFactory

class ModuleDoc(BaseDoc):

	"""
	desc:
		A docstring processer for module objects.
	visible:
		False
	"""

	def header(self, _dict):

		return u'*module* %s' % self.name()

	def misc(self, _dict):

		md = u''
		if self.onlyContents:
			prefix = u''
		else:
			prefix = u'%s.' % self.name()
		for attribName, attrib in self.objAttribs():
			if attribName in self.exclude:
				continue
			df = DocFactory(attrib, types=[u'class', u'function', u'module'],
				namePrefix=prefix, level=self.level+1, container=self.container,
				exclude=self.exclude)
			if df is not None:
				md += str(df)
		return md

	def name(self):

		return self._name()

	def _name(self):

		if self.customName is not None:
			return self.customName
		return safe_decode(self.obj.__name__, enc=self.enc)
