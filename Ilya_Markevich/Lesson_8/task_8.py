from task_8_dec import dec_1, dec_2, dec_3, dec_4, dec_5, dec_6

@timer
@func_name
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
    return a, b

data = fibonacci(10)
print(data)


@dec_1
@dec_2
def sl(a, b, c):
    answer = ((a * a ** c) / b) * 0,5
    return answer
