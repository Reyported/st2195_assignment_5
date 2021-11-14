def is_divisible_by_k(r, k):
 '''
 Checks whether x is divisible by k.
 1. replaced assert with return
 2. changed x to r to prevent naming conflicts 
 2. iterate over r before function to allow for checking of divisibility since lists cannot be calculated
 '''
 return (r % k == 0)
     
 '''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding 
doubles)
1. changed mutability of x 
2. fixed range values
3. edited the value of if arguments to reflect "2 or 5 or 7" 
 '''
x= []
for i in range(0,1000):
 if (is_divisible_by_k(i, 2) or is_divisible_by_k(i, 5) or is_divisible_by_k(i, 7)):
     x.append(i)
 
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding 
doubles)

1. added a one line solution to this problem
'''
sum(x)

sum(i for i in range(1000) if i % 2 == 0 or i % 5 == 0 or i % 7 == 0)

