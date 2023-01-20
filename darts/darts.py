import math

def score(x, y):
    distance = math.sqrt(x**2 + y**2) # first obtaining the distance to target
    if (distance > 10):
        return 0
    elif (5 < distance and distance <= 10):
        return 1
    elif (1 < distance and distance <= 5):
        return 5
    else: # if distance <= 1
        return 10
    
