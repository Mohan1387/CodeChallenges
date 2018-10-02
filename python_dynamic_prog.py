#Recursion
'''
def fibo_list(x):
  if x == 1 or x == 2:
    return 1
  else:
    return fibo_list(x-1) + fibo_list(x-2)
    
res = fibo_list(10)
print(res)
'''

#Recursion memoised 
'''
N = 100
temp = [None]*(N+1)

def fibo_list(x, temp):
  if temp[x] is not None:
    return temp[x]
  if x == 1 or x == 2:
    result = 1
  else:
    result = fibo_list(x-1, temp) + fibo_list(x-2, temp)
    temp[x] = result
  return result

def fib_memo(n):
  return fibo_list(n, temp)

res = fib_memo(N)
print(res)
print(temp[50])
print(len(temp))
'''

#bottom up

def fib_bottom(n):
  if n == 1 or n == 2:
    return 1
  bottomup = [None]*(n+1)
  bottomup[1] = 1
  bottomup[2] = 1
  for i in range(3, n+1):
    bottomup[i] = bottomup[i-1] + bottomup[i-2]
  return bottomup

res = fib_bottom(1000)
print(res)