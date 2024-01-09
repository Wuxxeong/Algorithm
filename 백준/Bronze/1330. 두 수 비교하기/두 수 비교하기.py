L = list(map(int, input().split()))
if(L[0] < L[1]):
  print("<")
elif(L[0] > L[1]):
  print(">")
else:
  print("==")