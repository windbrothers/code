# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:28:45 2020

@author: Administrator
"""

import re
# match 是从头开始匹配
#match= re.match(r'[1-9]\d{4}','10086 BIT ')
#search 是全局开始匹配
match= re.search(r'[1-9]\d{4}','BIT 10086')
#if match:
#    print(match.group(0))
#else:
#    print('error')
#ls =re.findall(r'[1-9]\d{4}','BAT10086 dx10000')
#print(ls)
#s=re.split(r'[1-9]\d{4}','BAT10086 dx10000')
#print(s)
#s=re.split(r'[1-9]\d{4}','BAT10086 dx10000',maxsplit=1)
#print(s)

#for m in re.finditer(r'[1-9]\d{4}','BAT10086 dx10000'):
#    if m:
#        print(m.group(0))


#m=re.sub(r'[1-9]\d{4}','-happy','BAT10086 dx10000')
#print(m)

#2

#m= re.search(r'[1-9]\d{4}','BIT 10086 dx10000')
#print(m.string)
#print(m.re)
#print(m.pos)
#print(m.endpos)
#print(m.span())
#3
m=re.search(r'PY.*N','uuPYANJJjSSSNoN')
#贪婪匹配
print(m.group(0))
##精确匹配
#m=re.search(r'PY.*?N','PYANJJjSSSNoN')
#print(m.group(0))