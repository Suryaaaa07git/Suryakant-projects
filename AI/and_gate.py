# AND Gate using Perceptron

def AND(x1, x2):
    w1, w2 = 1, 1
    threshold = 1.5
    output = x1*w1 + x2*w2
    
    if output >= threshold:
        return 1
    else:
        return 0

# Test cases
print("AND Gate Results:")
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))
