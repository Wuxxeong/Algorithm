N = int(input())
switch = list(map(int, input().split()))
student_num = int(input())  
whose_switch = [list(map(int, input().split())) for _ in range(student_num)]

def change_switch(s):
  if switch[s] == 1: switch[s] = 0
  elif switch[s] == 0: switch[s] = 1


for student in whose_switch:
  if student[0] == 1: #남자
    i = 1
    while i * student[1] <= len(switch):
      change_switch(i*student[1]-1)
      i += 1
  elif student[0] == 2: #여자
    start, end = student[1], student[1]
    change_switch(student[1]-1)
    while start-2 >= 0 and end < len(switch):
      start -= 1
      end += 1
      if switch[start-1] != switch[end-1]: break
      change_switch(start-1)
      change_switch(end -1)

for i in range(N):
    print(switch[i], end=" ")
    if i % 20 == 19:
        print()