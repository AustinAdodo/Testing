from math import pow, ceil


def ConvToRoman2(number: int, res: str):
    remainder = number
    result1 = res
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M", ]
    if remainder == 0:
        return result1
    else:
        b = list(filter(lambda al: al <= number, num))
        temp = b[-1]
        remainder = number % temp
        for index in range(int(number / temp)):
            res += sym[num.index(temp)]
        return ConvToRoman2(remainder, res)


def count_x(n: int):
    count = 0
    x = "X"
    for i in range(1, n + 1):
        if x in ConvToRoman2(i, ""):
            t = [i for i in ConvToRoman2(i, "")]
            t1 = list(filter(lambda p: p == "X", t))
            count += len(t1)
    return count


def spiralize():
    # even_numbers = [x for x in numbers if x % 2 == 0]
    # even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    spiral = [[0]]
    return spiral


# Eratosthenes
def sieveofEratosthenes(n: int) -> int:
    sieve = [True for i in range(n + 1)]
    primes = []
    sieve[1] = False
    # iterate from 2 to sqrt(n)
    # if the number is prime mark up all multiples of n as composite
    for i in range(2, ceil(pow(n, 0.5)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    for i in range(2, n + 1):
        if sieve[i]:
            primes.append(i)
    return len(primes)


def isprime(n: int) -> bool:
    result = False
    y = 2
    if n == 1:
        return result
    while y * y <= n:
        if n % y == 0:
            return result
        y += 1
    result = True
    return result


def closest_temperature():
    n = int(input())  # the number of temperatures to analyse
    temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
    result = ''
    if len(temps) == 0:
        print("0")
    else:
        temps_split = temps.split()
        result = temps_split[0]
        for temp in temps_split:
            if abs(int(temp)) < abs(int(result)):
                result = temp
            elif abs(int(temp)) == abs(int(result)):
                result = max(int(temp), int(result))

    print(result)


def count_primes_less_than(n: int) -> int:
    result = sieveofEratosthenes(n)
    return result


# print("{:.2e}".format(b))
def Fibonacci(n):
    if n < 2:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def ansFib(n):
    a, b = 0, 1
    sum1 = 0
    while b < n:
        if b % 2 != 0:
            sum1 += b
        a, b = b, a + b
    return sum1


def pallindrome(n=0):
    revn = []
    normal = []
    revn[:0] = list(map(int, str(n)))
    revn = revn[::-1]
    normal[:0] = list(map(int, str(n)))
    if revn == normal:
        return True
    return False


# lst = [0,0,0,0,0,0,1]
# while lst and lst[0] == 0:
#     lst.pop(0)


# 545040
def pallindrome_count(n):
    count = [i for i in range(n) if pallindrome(i)]
    return sum(count)


# 2865
def Ascii_Code_Sum(st: str):
    s = "".join(st.split(" "))
    vow = ["a", "e", "i", "o", "u"]
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y',
                  'Z']
    a = [i for i in s]
    ascii_code = [ord(i) for i in a]
    ascii_code1 = [(-1 * i) for i in ascii_code if chr(i).lower() in vow]
    ascii_code2 = [i for i in ascii_code if chr(i).upper() in consonants]
    return sum(ascii_code1 + ascii_code2)


if __name__ == '__main__':
    limit = 1_000_000
    my_list = ['apple', 'banana', 'cherry', 'date']
    result = list(map(lambda x, i: x.upper() if i % 2 == 0 else x.lower(), my_list, range(len(my_list))))
    print(result)
    # print(b)
    # pallindrome_count(20)
    # first_occurrence = string.find(word)
    # second_occurrence = string.find(word, first_occurrence + 1)
