def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        marker = True
        for i in range(2, result):
            if result % i == 0:
                marker = False
        if marker:
            print("Простое")
            return result
        else:
            print("Составное")
            return result
    return wrapper



@is_prime
def summ_three(a, b, c):
    return a + b + c


result = summ_three(2,3,6)
print(result)