#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
from telnetconnector import connector

o = ''
output = connector('disp error')
'''parse from output today and yesterday errors'''
data = '{:d%m\t%d}'.format(datetime.datetime.today())
for i in output.split('ALARMS'):
	if i.find(data) != -1:
		o += i
res = list(map(lambda x: x.replace('d', '\t').replace('\n', '').split('\t'), o.replace('dHARDWARE ERROR REPORT - ACTIVE ', '').split('\nn')))
for i in res:
        print('MtceName: {}, Port: {}, AltName: {}, ErrType: {}, AuxData: {}'.format(i[2], i[1], i[3], i[4], i[5]))
