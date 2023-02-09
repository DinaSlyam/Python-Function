def has_33_incorrect(x):
  print("\nRunning the incorrect function")
  for i in range(len(x)-1):
    print("Checking indices {} and {}".format(i, i+1))
    if x[i:i+2] == [3,3]:
      print("indices contain 2 consecutive 3's. Returning true")
      return True
    else:
      print("indices don't contain 2 consecutive 3's. Returning false")
      return False

def has_33_correct(x):
  print("\nRunning the correct function")
  for i in range(len(x)-1):
    print("Checking indices {} and {}".format(i, i+1))
    if x[i:i+2] == [3,3]:
      print("indices contain 2 consecutive 3's. Returning true")
      return True
  print("Did not find consecutive 3's. Returning false")
  return False


list = [1, 2, 4, 5, 6, 3, 3, 2, 5]
has_33_incorrect(list)
has_33_correct(list)