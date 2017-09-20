#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Trunk capacity: 25 Idle: 4 Active: 21(agents - 2, menu - 15, other - 4)'''

import re
from telnetconnector import connector

output = connector('stat tru 1') #incoming trunk-group 1
#ports = re.findall('\\t(.*)\tA', connector('list sta 5800 count 20')) #agents station between 5800 and 5820, their names starts whith 'A'
ports = ['S00132', 'S00133', 'S00134', 'S00135', 'S00136', 'S00137', 'S00138', 'S00139', 'S00140', 'S00141', 'S00142', 'S00131', 'S00143', 'S00144', 'S00145', 'S00146', 'S00147', 'S00148', 'S00149'] #agents stations ports
error = ['OOS/FE-idle', 'out-of-service', 'out-of-service-NE']
if any([i in error for i in output]):
    print ('Error')
else:
    agent = 0
    for i in ports:
        if output.find(i) != -1:
            agent += 1       
    active = output.count('active')
    capacity = output.count('in-service')
    menu = output.count('001V9') # announcement board 
    print ('Trunks: {} Idle: {} Active: {}(agents - {}, menu - {}, other - {})'.format(capacity, capacity - active, active, agent, menu, active - agent - menu))
