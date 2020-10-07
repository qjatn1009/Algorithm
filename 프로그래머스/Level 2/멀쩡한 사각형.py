#https://leedakyeong.tistory.com/135#comment16270807 참고
import math
def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))


print(solution(7, 9))