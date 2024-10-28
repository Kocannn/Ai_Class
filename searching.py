

def search(y):
  x = [5, 5, 10, 3, 2, 6, 7]
  for index, value in enumerate(x):
    if value == y:
      return index
  return 0




print(search(4))  
print(search(2))  
    