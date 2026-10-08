import math

def softmax(scores: list[float]) -> list[float]:
    
    dividend = 0
    max_score = max(scores)
    for i in range(len(scores)):
        dividend += math.exp(scores[i] - max_score)

    result = []
    for i in range(len(scores)):
        result.append(math.exp(scores[i] - max_score)/dividend)
    return result