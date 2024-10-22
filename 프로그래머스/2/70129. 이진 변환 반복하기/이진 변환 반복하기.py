def solution(s):
    answer = []
    cnt=0
    clear=0
    while True:
        new_s = ""
        for ch in s:
            if ch=="0":
                clear+=1
                continue
            new_s+=ch

        l = len(new_s)
        ans=""
        while l>0:
            ans = str(l%2)+ans
            l=l//2
        cnt+=1
        s=ans
        if s=="1":
            break
    
    return [cnt,clear]