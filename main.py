from math import pow, ceil


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def spiralize(size=[[int]]):
    # even_numbers = [x for x in numbers if x % 2 == 0]
    # even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    spiral = [[]]
    return spiral


# Eratosthenes
def seiveofEratosthenes(n: int) -> int:
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


def count_primes_less_than(n: int) -> int:
    result = seiveofEratosthenes(n)
    return result


if __name__ == '__main__':
    limit = 100
    list1 = []
    list2 = []
    seperator = ", "

    for r in range(1, limit):
        if isprime(r):
            list1.append(r)
    my_list_str = [str(i) for i in list1]
    my_list_str2 = [str(i) for i in list2]
    print(count_primes_less_than(limit))
    print(seperator.join(my_list_str))
    print(len(list2))
    print(seperator.join(my_list_str2))
    # if 'name' in my_dict:
    # print('The dictionary contains the key "name"')
    # string = "the quick brown fox jumps over the lazy dog"
    # word = "the"
    # first_occurrence = string.find(word)
    # second_occurrence = string.find(word, first_occurrence + 1)
