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

class PropertyDoc(BaseDoc):

	"""
	desc:
		A docstring processer for property objects.
	visible:
		False
	"""

	def header(self, _dict):

		return u'property __%s__' % self.name()

	def _name(self):

		_dict = self._dict()
		if u'name' not in _dict:
			raise Exception(u'Property docstrings require a name attribute')
		return _dict[u'name']
