n = int(input())
L = [list(map(int, input().split())) for i in range(n)] #이차원 배열로 저장 O(n)
L.sort(key=lambda x:x[1]) #오른쪽 끝점 기준 정렬 O(nlogn)

count = 1
k = L[0][1] #첫번째로 나오는 오른쪽 끝점을 기준 잡음
for i in range(n):
	if k < L[i][0]: #k 보다 작은 왼쪽 점을 가진 막대기는 모두 패스하면 아직 박히지 않은 첫번째 막대기가 나온다
		count += 1
		k = L[i][1]	
print(count)

'''
오른쪽 끝점 정렬을 한 후 첫 번째로 나오는 오른쪽 점에 못을 하나 박는다. 오른쪽 끝 점 정렬을 한 후 순차적으로 보기 때문에 최초로 k보다 큰 왼쪽 점을 만나면 해당 막대기의 오른쪽 끝점에 못을 하나 더 박는다.

정렬하는 시간 + 핀을 박는 시간은 O(nlogn + n) = O(nlogn)이다.
'''