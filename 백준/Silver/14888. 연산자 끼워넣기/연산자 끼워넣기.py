operations = []
def operatorPermutations(n, new_arr):
    global op, visited
    if len(new_arr) == n:
        operations.append(new_arr)
        return
    for i in range(len(op)):
        if not visited[i]:
            visited[i] = 1
            operatorPermutations(n, new_arr + [op[i]])
            visited[i] = 0

def calculate(numbers, operation):
    result = numbers[0]
    for i in range(len(operation)):
        if operation[i] == '+':
            result += numbers[i+1]
        elif operation[i] == '-':
            result -= numbers[i+1]
        elif operation[i] == '*':
            result *= numbers[i+1]
        elif operation[i] == '/':
            if result < 0:
                result = -(-result // numbers[i+1])
            else:
                result //= numbers[i+1]
    return result

n = int(input())
numbers = list(map(int, input().split()))
operator_num = list(map(int, input().split()))

op = ['+']*operator_num[0] + ['-']*operator_num[1] + ['*']*operator_num[2] + ['/']*operator_num[3]
visited = [0]*len(op)

#연산자 조합 생성 (operations)
operatorPermutations(n-1, [])

#최소값, 최대값 초기화
min_result, max_result = float('inf'), -float('inf')

#각 연산자에 조합에 대해 계산
for operation in operations:
    result = calculate(numbers, operation)
    if result > max_result:
        max_result = result
    if result < min_result:
        min_result = result
print(max_result)
print(min_result)