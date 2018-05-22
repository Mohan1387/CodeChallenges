var = 'AAAAABBBCCCCDDEEEE'
vardict = {}

for i in var:
  try:
    vardict[i] = vardict[i]+1
  except KeyError:
    vardict[i] = 1 

x = ''
for (k,v) in vardict.items():
  x += k+str(v)

print(x)
