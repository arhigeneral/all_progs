

def f(count):
    answer = [0]
    num1 = 1
    num2 = 1
    while True:
        num1 += num2
        num2 += num1
        if num1 % 2 == 0:
            answer.append(num1)
        elif num2 % 2 == 0:
            answer.append(num2)
        if len(answer) == count:
            break
    return print(answer)

f(100)  
