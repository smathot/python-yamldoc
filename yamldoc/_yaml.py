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
import yaml
from collections import OrderedDict

def orderedLoad(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):

	"""
	desc:
		Loads YAML strings while treating dictionaries as OrderedDict objects,
		so that argument order is preserved.

	arguments:
		stream:
			desc:	YAML text.
			type:	[str, unicode]

	returns:
		desc:	A data structure.
	"""

	class OrderedLoader(Loader):
		pass
	def construct_mapping(loader, node):
		loader.flatten_mapping(node)
		return object_pairs_hook(loader.construct_pairs(node))
	OrderedLoader.add_constructor(
		yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
		construct_mapping)
	return yaml.load(stream, OrderedLoader)
