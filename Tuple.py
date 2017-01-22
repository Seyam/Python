import sys
import os


TVSeries ={
 'Horror':'Walking Dead',
'Thriller':'The Prison Break',
'Drama':'Suits'
}



print(len(TVSeries))
print(TVSeries['Horror'])
#print(TVSeries.keys())
#print(TVSeries.values())
del TVSeries['Drama']
print(TVSeries)
