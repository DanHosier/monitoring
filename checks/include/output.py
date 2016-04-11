#! /usr/bin/python
'''
output.py - outputs status code, status output, perfdata and script name in
    in the appropriate format for the monitoring system in use.
        - status code = int
        - status output = list
        - perfdata = list
        - name = string
'''

def check_mk (sc,so,pd,n):
    print "{} {} {} {}".format (sc,so,pd,n)
    

