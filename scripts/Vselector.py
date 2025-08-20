#! /usr/bin/env python
import sys, json

josn_file = 'gvariable.json' 
decodejson = json.load(open(josn_file, 'r'))

if len(sys.argv) < 2:
    print('error' , end="")

elif len(sys.argv) == 2 : 
    
    key = sys.argv[1].strip()
  
    if key in decodejson: 
        print(decodejson[key], end="")
    else :
        print('unkownvariable',end="")




