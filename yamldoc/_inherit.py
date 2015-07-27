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

class inherit(type):

	"""
	desc: |
		A metaclass that inherits docstrings from parent classes.

	source:
		- http://groups.google.com/group/comp.lang.python/msg/26f7b4fcb4d66c95
		- http://stackoverflow.com/questions/8100166/inheriting-methods-docstrings-in-python

	example: |
		# This will make all functions of A inherit the corresponding docstrings
		# from B.
		import yamldoc
		class A(B):
			__metaclass__ = yamldoc.inherit
	"""

	def __new__(meta, name, bases, clsdict):

		"""
		desc:
			Constructor.

		visible:	False
		"""

		if not('__doc__' in clsdict and clsdict['__doc__']):
			for mro_cls in (mro_cls for base in bases for mro_cls in base.mro()):
				doc=mro_cls.__doc__
				if doc:
					clsdict['__doc__']=doc
					break
		for attr, attribute in clsdict.items():
			if not attribute.__doc__:
				for mro_cls in (mro_cls for base in bases for mro_cls in base.mro()
					if hasattr(mro_cls, attr)):
						doc=getattr(getattr(mro_cls,attr),'__doc__')
						if doc:
							attribute.__doc__=doc
							break
		return type.__new__(meta, name, bases, clsdict)
