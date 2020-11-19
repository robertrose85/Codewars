def productFib(prod):
  l = []
  a,b = 0,1
  x = a*b
  while True:
    if x == prod:
      l.insert(0,a)
      l.insert(1,b)
      l.insert(2,True)
      return(l)
      break
    elif x > prod:
      l.insert(0,a)
      l.insert(1,b)
      l.insert(2,False)
      return(l)
      break
    else:
      a,b = b, a+b
      x = a*b

print(productFib(0))