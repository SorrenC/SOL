# Imports
from sol.Functions.OrbitDetermination.KepElementsPlot import KepElementPlot

## TEST DATA
e=0
i=40
a=2294967.891
W=50
w=30
f=150.814 

Plot = KepElementPlot(i,a,e,W,w,f).KepPlot()