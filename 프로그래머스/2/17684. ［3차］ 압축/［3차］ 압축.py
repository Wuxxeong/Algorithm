def solution(msg):
    answer = []
    ch = ['-','A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T','U',
          'V','W','X','Y','Z']
    
    i = 0
    while i < len(msg):
        w = ''
        # ch 중 현재 입력과 일치하는 가장 긴 문자열 w 를 찾는다
        for j in range(len(msg), i, -1):
            if msg[i:j] in ch:
                w = msg[i:j]
                break
        # w에 해당하는 사전의 색인 번호 answer에 추가 + 입력에서 w 제거(m 재설정)
        answer.append(ch.index(w))
        i += len(w)
        
        # 입력에서 처리되지 않은 다음 글자가 남아있다면 합쳐서 ch에 등록
        if j < len(msg):
            ch.append(w+msg[i])
            
    return answer