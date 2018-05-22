var = 'AAAAABBBCCCCDDEEEE'
vardict = {}

for i in var:
  try:
    vardict[i] = vardict[i]+1
  except KeyError:
    vardict[i] = 1 
  
print(vardict)