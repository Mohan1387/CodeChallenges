lst = [2,3,4,5,6,3]

checklst = []

for i in lst:
  if len(checklst) == 0:
    checklst.append(i)
  else:
    if i in checklst:
      print(str(i)+" is dupicated")
      continue
    else:
      checklst.append(i)
	  

lst = [2,3,4,5,6]

checklst = set()

#o(n) comp 
for i in lst:
  checklst.add(i) # o(1)

#len function has o(1) comp	  
if len(lst) == len(checklst):
  print(True)
else:
  print(False)
  
#total comp = o(N+2 log N)