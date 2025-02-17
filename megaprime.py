def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False
    return True

def megaprime_count(a, b):
    count = 0
    for j in range(a, b + 1):
        if isprime(j): 
            newlist = list(str(j))
            for k in newlist:
                if not isprime(int(k)): 
                    break 
            else:  
                count += 1  
    return count


string = input()
first, last = map(int, string.split())

print(megaprime_count(first, last))
