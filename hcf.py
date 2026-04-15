#finding HCF of Numbers
from math import gcd
from functools import reduce 
def find_hcf(nums):
    return reduce(gcd,nums)
print(find_hcf([24,36,60]))