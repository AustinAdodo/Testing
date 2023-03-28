from math import pow, ceil


def spiralize(size=[[0]]):
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


if __name__ == '__main__':
    limit = 1_00
    list1 = []
    test = [3]
    list2 = []
    seperator = ", "

    for r in range(1, limit):
        if isprime(r):
            list1.append(r)
    my_list_str = [str(i) for i in list1]
    my_list_str2 = [str(i) for i in list2]
    print(count_primes_less_than(limit))
    print(seperator.join(my_list_str))
    # check = (3 in test)
    print(len(list2))
    print(seperator.join(my_list_str2))
    test.sort(reverse=True)
    print(test)

    # if 'name' in my_dict:
    # print('The dictionary contains the key "name"')
    # string = "the quick brown fox jumps over the lazy dog"
    # word = "the"
    # first_occurrence = string.find(word)
    # second_occurrence = string.find(word, first_occurrence + 1)
