import math

def softmax(scores: list[float]) -> list[float]:
    max_val = max(scores)
    s_exp = [math.exp(i-max_val) for i in scores]
    s = sum(s_exp)
    softmax = [i/s for i in s_exp]
    return softmax