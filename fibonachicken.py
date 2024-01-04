memory = {1: 1, 2: 1}


def fibonacci(n):
    if n in memory:
        number = memory[n]
    else:
        number = fibonacci(n - 1) + fibonacci(n - 2)
        memory[n] = number
    return number


def fibonachicken(n):
    fibonacci(n)
    value = 0
    key = 0
    if n in memory.values():
        for key, val in memory.items:
            if val == n:
                result = memory[key - 1]
                value = val
                key = key
    else:
        # 본인보다 작은 수 중 제일 큰 피보나치 수 구하기
        target = []
        for i in memory.values():
            if i < n:
                target.append(i)
            나머지 = n - target[-1]
            print("뾰잉", target)

        # 나머지로 피보나치 수 구하기
        a = fibonacci(나머지)
        # 두 개 더하기
        result = target[-1] + a
    print("주문 해야 할 닭의 수는 {} 입니다.".format(result))
    print("{}명이 {}마리, {}명이 {}마리".format(key, target[-1], key - 1, a))


'''
모든 양의 정수는 두 개의 서로 다른 피보나치 수의 합으로 나타낼 수 있다
Zeckendorf's Theorem : 각 정수를 고유한 피보나치 표현으로 분해할 수 있음
'''

print(fibonachicken(4))