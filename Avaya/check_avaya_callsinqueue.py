#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from telnetconnector import connector

output = connector('monitor bcms skill 1')
print ('Calls waiting: {}'.format(re.search('s\t(.*)\t', output).group(1)))
