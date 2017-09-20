#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys
from connect2n import connector
'''Output for ussd request is - [b'\r\nat&g3=xtd*112#;\r\n <++g03     atd*112#;\r\n -->g03     OK\r\n -->g03     +CUSD: 2,"ZALYSHOK: 1424:00 HV NA INSHI MEREZHI; 1500 SMS PO UKRAINI; 50:00 HV ZA KORDON']'''

def conto(sim):
    ot = connector('at&g' + str(sim) + '=xtd*112#;', 'KORDON', timeout = 5)
    out = ot[0].decode('utf-8')
    error = 'SIM card is busy now'
    if out.find('BUSY') != -1:
        return error
        sys.exit(1)
    try:
        hv = re.search('OK: (.+?) HV', out).group(1)
        mhv = re.search('NI; (.+?) HV', out).group(1)
        sms = re.search('HI; (.+?) SMS', out).group(1)
        return hv[:-3], mhv[:-3], sms
    except AttributeError:
        return error
        sys.exit(1)

if __name__ == '__main__':
    import getopt
    
    sim = None
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hs:",['sim='])
    except getopt.GetoptError:
        print ('check_2nbalance.py -s <number of sim card>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('check_2nbalance.py -s <number of sim card>')
            sys.exit(2)
        elif opt in ('-s', '--simcard'):
            sim = arg

    if sim is None: sim = input("Enter SIM Card Number: ")
    rs = conto(sim)
    if isinstance(rs, tuple):
        print ('Balance is: {} min. to other operators, {} min. for international calls, {} sms.'.format(rs[0], rs[1], rs[2]))
    else:
        print (rs)
