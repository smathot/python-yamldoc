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
import yaml
from yamldoc._basedoc import BaseDoc
from yamldoc._exceptions import InvalidDocString

class FunctionDoc(BaseDoc):

	"""
	desc:
		A docstring processer for function and method objects.
	visible:
		False
	"""

	def __init__(self, *args, **kwargs):

		super(FunctionDoc, self).__init__(*args, **kwargs)
		self.parseArgSpec()

	def header(self, _dict):

		l = []
		for arg in self.args:
			l.append(arg)
		for kw, default in self.keywords.items():
			if isinstance(default, unicode):
				default = u'u\'%s\'' % default
			elif isinstance(default, str):
				default = u'u\'%s\'' % default.decode(self.enc)
			l.append(u'%s=%s' % (kw, default))
		if self.argumentList != None:
			l.append(u'\*%s' % self.argumentList)
		if self.keywordDict != None:
			l.append(u'\*\*%s' % self.keywordDict)
		return u'*function* %s(%s)' % (self.name().replace(u'__',
			u'\_\_'), u', '.join(l))

	def sections(self, _dict):

		md = super(FunctionDoc, self).sections(_dict)
		if u'arguments' in _dict:
			md += u'__Arguments:__\n\n' + self.argSection(_dict[u'arguments'])
		if u'keywords' in _dict:
			md += u'__Keywords:__\n\n' + self.argSection(_dict[u'keywords'])
		if u'argument-list' in _dict:
			md += u'__Argument list:__\n\n' + self.argListSection(
				_dict[u'argument-list'])
		if u'keyword-dict' in _dict:
			md += u'__Keyword dict:__\n\n' + self.argListSection(
				_dict[u'keyword-dict'], prefix=u'**')
		if u'returns' in _dict:
			md += u'__Returns:__\n\n' + self.returnsSection(_dict[u'returns'])
		return md

	def argSection(self, argDict):

		md = u''
		for arg, _dict in argDict.items():
			md += u'- `%s` -- %s\n' % (arg, _dict[u'desc'])
			for prop, val in _dict.items():
				if prop == u'desc':
					continue
				if prop == u'type':
					if isinstance(val, list) and prop != u'default':
						val = u', '.join(val)
				elif prop == u'default':
					val = repr(val)
				md += u'\t- %s: %s\n' % (prop.capitalize(), val)
		return md + u'\n'

	def argListSection(self, _dict, prefix=u'*'):

		md = u''
		for argList, val in _dict.items():
			md += u'- `%s%s`: %s\n' % (prefix, argList, val)
		return md + u'\n'

	def returnsSection(self, _dict):

		md = _dict[u'desc'] + u'\n\n'
		for prop, val in _dict.items():
			if prop == u'desc':
				continue
			if isinstance(val, list):
				val = u', '.join(val)
			md += u'- %s: %s\n' % (prop.capitalize(), val)
		return md + u'\n'

	def argDict(self, argDict, args):

		for arg, val in argDict.items():
			if arg not in args:
				raise InvalidDocString(
					u'%s(): Defined non-existing argument: %s' \
					% (self.name(), arg))
			argDict[arg] = self.valDict(val)
		for arg in args:
			if arg not in argDict:
				argDict[arg] = self.valDict(u'No description')
		return argDict

	def kwDict(self, kwDict, keywords):

		for kw, val in kwDict.items():
			if kw not in keywords:
				raise InvalidDocString(
					u'%s(): Defined non-existing keyword: %s' \
					% (self.name(), kw))
			kwDict[kw] = self.valDict(val, default=keywords[kw])
		for kw in keywords:
			if kw not in kwDict:
				kwDict[kw] = self.valDict(u'No description',
					default=keywords[kw])
		return kwDict

	def argListDict(self, alDict, al):

		if al == None and len(alDict) != 0:
			raise Exception('Defined non-existing argument or keyword list.')
		if isinstance(alDict, basestring):
			alDict = {al: alDict}
		if len(alDict) > 1:
			raise Exception('Only one argument and keyword list allowed.')
		if al not in alDict:
			alDict[al] = u'No description.'
		return alDict

	def argSpec(self):

		# Parse argument specification. If the @validate decorator is used, the
		# argument specification is stored as __argspec__, otherwise we use
		# introspection.
		if hasattr(self.obj, u'__argspec__'):
			return self.obj.__argspec__
		return inspect.getargspec(self.obj)

	def parseArgSpec(self):

		argSpec = self.argSpec()
		if argSpec.args == None:
			argSpec.args = []
		if argSpec.defaults == None:
			self.args = argSpec.args
			self.keywords = {}
		else:
			self.args = argSpec.args[:len(argSpec.args)-len(argSpec.defaults)]
			self.keywords = {}
			for kw, default in zip(argSpec.args[len(self.args):],
				argSpec.defaults):
				self.keywords[kw] = default
		self.argumentList = argSpec.varargs
		self.keywordDict = argSpec.keywords
		# We don't process the `self` argument
		if len(self.args) > 0 and self.args[0] == u'self':
			self.args = self.args[1:]

	def valDict(self, val, **properties):

		if isinstance(val, str):
			val = val.decode(self.enc)
		if isinstance(val, basestring):
			val = {u'desc' : val}
		val.update(properties)
		if u'type' in val and not isinstance(val[u'type'], list):
			val[u'type'] = [val[u'type']]
		return val

	def _dict(self):

		_dict = super(FunctionDoc, self)._dict()
		# Make sure that all necessary sections are present
		if u'desc' not in _dict:
			_dict[u'desc'] = u'No description.'
		if len(self.args) > 0 and u'arguments' not in _dict:
			_dict[u'arguments'] = {}
		if len(self.keywords) > 0 and u'keywords' not in _dict:
			_dict[u'keywords'] = {}
		if self.argumentList != None and u'argument-list' not in _dict:
			_dict[u'argument-list'] = {}
		if self.keywordDict != None and u'keyword-dict' not in _dict:
			_dict[u'keyword-dict'] = {}
		# Parse all sections, and make sure that they
		for sectionName, sectionValue in _dict.items():
			if sectionName == u'returns':
				_dict[sectionName] = self.valDict(sectionValue)
			elif sectionName == u'arguments':
				_dict[sectionName] = self.argDict(sectionValue, self.args)
			elif sectionName == u'keywords':
				_dict[sectionName] = self.kwDict(sectionValue,
					self.keywords)
			elif sectionName == u'argument-list':
				_dict[sectionName] = self.argListDict(sectionValue,
					self.argumentList)
			elif sectionName == u'keyword-dict':
				_dict[sectionName] = self.argListDict(sectionValue,
					self.keywordDict)
		return _dict

	def _name(self):

		return self.obj.__name__.decode(self.enc)
