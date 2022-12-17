def IsPrime(number):
    for i in range(2 , number // 2 + 1):
        if number % i == 0:
            return False
    else:
        return True






























