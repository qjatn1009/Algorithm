def solution(bridge_length, weight, truck_weights):
    answer = 0
    passing = [0]*bridge_length
    pass_over = []
    bridge_weight = 0
    i = 0 
    while len(pass_over) < len(truck_weights) :
        answer += 1
        if len(passing) >= bridge_length:  #다리길이랑 지나고 있는 트럭 비교
            if passing[0] > 0:  # 도착 했을 때
                bridge_weight -= passing[0]
                pass_over.append(passing.pop(0))
            else:
                passing.pop(0) 
        if i == len(truck_weights):  
            passing.append(0)
        else:
            if bridge_weight+truck_weights[i] <= weight and i < len(truck_weights): # 다리에 무게 초과 아닐 때
                bridge_weight += truck_weights[i]
                passing.append(truck_weights[i])
                i+=1
            else:    # 무게 초과 일때
                passing.append(0)

    return answer

# print(solution(2, 10, [7,4,5,6] ))
# print(solution(100, 100, [10] ))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10] ))