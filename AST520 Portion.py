# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:37:19 2019

@author: Gonzalo
"""


#arrays for data (all # of columns)
sector = ['sample_sector0']
tessFile = ['HD_lsls.fits']
curveID = ['curve1']
correlation = ['99.322811332']

LN = 0

out_file = open('sample_candidates.csv', 'w')

line1 = 'sector' + ',' + 'tessFile' + ',' + 'curveID' + ',' + 'correlation' + '\n'

out_file.write(line1)

for i in sector:
    
        line =  sector[LN] + ',' + tessFile[LN] + ',' + curveID[LN] + ',' + correlation[LN] + '\n'
        LN += 1
        out_file.write(line)
        
out_file.close()