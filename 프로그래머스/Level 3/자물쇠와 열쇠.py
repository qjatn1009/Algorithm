# 모든 경우의 수 해보는거 시뮬레이션
def solution(key, lock):
    answer = True
    m, n = len(key), len(lock)
    board = [[0 for _ in range(2*m+n)] for _ in range(2*m+n)]
    for i in range(n):
        for j in range(n):
            board[i+m][j+m] = lock[i][j]
    # def check_key():
        
    
    def rotation(key): # 키를 3번 회전(시계방향)
        return list(zip(*key[::-1])) # 진짜 똑똑하다.
            
        
    

    
    
                  
    
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

