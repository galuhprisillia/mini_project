# -*- coding: utf-8 -*-

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_list():
    result = []
    for i in range(100, 0, -1):
        if is_prime(i):
            continue
        if i % 3 == 0 and i % 5 == 0:
            result.append("FooBar")
        elif i % 3 == 0:
            result.append("Foo")
        elif i % 5 == 0:
            result.append("Bar")
        else:
            result.append(str(i))
    return result

result_list = generate_list()
print(result_list)
