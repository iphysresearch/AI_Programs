#! /usr/bin/env python

import sys


# -- Stadium Data
# Stadium
# Stadium Capacity    
# expanded capacity (standing)   
# Location    
# Playing surface 
# Is Artificial Turf  
# Team    
# Opened  
# Weather 
# Station Roof Type
# elevation


for line in sys.stdin:
    line = line.strip()

    contents = line.split(",")
    contents[0] = contents[0].lower()
    
    print("\t".join(contents))