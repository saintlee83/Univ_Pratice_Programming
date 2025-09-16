def test():
  a = 10000
  b = 10000
  print(id(a), id(b))

  return a is b

a = 10000
b = 10000
print(id(a), id(b))
print(test())