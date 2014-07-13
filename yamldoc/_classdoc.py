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

from yamldoc._basedoc import BaseDoc
from yamldoc._docfactory import DocFactory

class ClassDoc(BaseDoc):

	"""
	desc:
		A docstring processer for class objects.
	visible:
		False
	"""

	def header(self, _dict):

		return u'*class* %s' % self.name()

	def misc(self, _dict):

		md = u''
		for attribName, attrib in self.objAttribs():
			df = DocFactory(attrib, namePrefix=u'%s.' % self.name(),
				level=self.level+1)
			if df != None:
				md += unicode(df)
		return md

	def _name(self):

		return self.obj.__name__.decode(self.enc)
