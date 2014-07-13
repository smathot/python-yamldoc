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

import yamldoc
from academicmarkdown import build
fd = yamldoc.DocFactory(yamldoc)
md = build.MD(unicode(fd))
build.TOCAnchorHeaders = True
build.HTML(unicode(fd), u'readme.html')
open(u'readme.md', u'w').write(md.encode(u'utf-8'))
