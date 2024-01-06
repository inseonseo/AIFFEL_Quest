memory = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5}

def fibonacci(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibonacci(n - 1) + fibonacci(n - 2)
        memory[n] = number
    return number

def fibonachicken(n):
    fibonacci(n)
    key = 0
    if n in memory.values():
        for key, val in memory.items():
            if val == n:
                result = memory[key - 1]
    else:
        # 본인보다 작은 수 중 제일 큰 피보나치 수 구하기
        target = []
        for key, val in memory.items():
            if val < n:
                target.append(val)
                key = key
            나머지 = n - target[-1]
            a = fibonachicken(나머지)
            print(target)
            result = target[-1] + a

    print("주문 해야 할 닭의 수는 {} 입니다.".format(result))
    #print("{}명이 {}마리, {}명이 {}마리".format(key, target[-1], 나머지, a))
    return(result)

'''
모든 양의 정수는 두 개의 서로 다른 피보나치 수의 합으로 나타낼 수 있다
Zeckendorf's Theorem : 각 정수를 고유한 피보나치 표현으로 분해할 수 있음
'''

print(fibonachicken(18))