N = input()
l = len(N)
sum = 0
for i in range(l-1):
  sum = sum + (9 * 10**(i))*(i+1)

sum = sum + l*(int(float(N)) - 10**(l-1)+1)
print(sum)