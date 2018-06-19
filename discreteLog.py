import math
'''
    This is an implementation of the Babystep - Giantstep algorithm in order 
    to solve the descreet logarithm problem.
    values to test with generator = 5, modolo = 167, answer = 49 -> the expected solution is 70
    49 = 5 ^ 70 mod 167
'''

def calculate_descreet_power(num: int, exp: int, mod:int) -> int:
    ans = 1
    for _ in range(1, exp+1):
        ans = (ans * num) % mod
    return ans

ans = calculate_descreet_power(439, 23425, 104729)
print('expected result = {}'.format(23425))

generator   = 439
mod_num     = 104729
Q           = 100000

# user input of variabls
# ans = generator^x % mod_num
# generator = int(input('Please enter the generator (5): '))
# mod_num   = int(input('Please enter the modolo (167, 49943): '))
# ans       = int(input('Please enter the answer (49): '))
# Q         = int(input('Please enter the maximum value that should be suported: '))

print(generator, mod_num, ans)


# calculation of the baby step list:
# Q = |N^0.5| <- rounded up , N = mod_num -1
# {(ans * generator^x, x): 0 <= x <= Q - 1}

# Calculating Q instead of having a predefined search space can lead to very long computations or even the program crashing.
# Q = math.ceil(math.sqrt(mod_num-1))  # calculate sqrt of mod_num - 1 and then round up the result to the next int.

baby_step_dic = {}
step = ans % mod_num  # calculating step 0
baby_step_dic[step] = 0

for i in range(1, Q):
    step = step * generator % mod_num
    baby_step_dic[step] = i


# calculate the giant step list
step = calculate_descreet_power(generator, Q, mod_num)
step0 = step
solution = -1

if step in baby_step_dic:
    solution = 1*Q-baby_step_dic[step]
else:
    for i in range(2, Q+1):
        step = step * step0 % mod_num
        if step in baby_step_dic:
            solution = i*Q-baby_step_dic[step]
            break

print('The solution is: {}'.format(solution))
