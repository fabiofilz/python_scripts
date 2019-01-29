"""
exer1: Given an integer n, return True if n is within 10 of either 100 or 200
"""

def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(almost_there(90))
# true

print(almost_there(150))
# false

"""
exer2: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""

def has_33(nums):
    for i in range(0, len(nums)-1):
      
        if nums[i:i+2] == [3,3]:
            return True  
    
    return False

print(has_33([1, 3, 3]))
# True

print(has_33([1, 3, 1, 3]))
# False


"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
"""
def spy_game(nums):

    code = [0,0,7,'x']
    
    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works
       
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
# True

print(spy_game([1,0,2,4,0,5,7]))
# True

print(spy_game([1,7,2,0,4,5,0]))
# false

"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
"""


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    #
    return len(primes)


# print(count_primes(100))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 25




