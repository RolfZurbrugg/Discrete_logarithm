import math
'''
    This is an implementation of the Babystep - Giantstep algorithm in order 
    to solve the descreet logarithm problem.
    values to test with generator = 5, modolo = 167, answer = 49 -> the expected solution is 70
    49 = 5 ^ 70 mod 167
'''

# user input of variabls
# ans = generator^x % mod_num
generator = int(input('Please enter the generator: '))
mod_num       = int(input('Please enter the modolo: '))
ans       = int(input('Please enter the answer: '))

print(generator, mod_num, ans)


# calculation of the baby step list:
# Q = |N^0.5| <- rounded up , N = mod_num -1
# {(ans * generator^x, x): 0 <= x <= Q - 1}

Q = math.ceil(math.sqrt(mod_num-1))  # calculate sqrt of mod_num - 1 and then round up the result to the next int.

baby_step_dic = {}
# calculating step 0
step = ans % mod_num
baby_step_dic[step] = 0

for i in range(1, Q):
    step = step * generator % mod_num
    baby_step_dic[step] = i


# sorted(baby_step_dic) # todo not sure if this is necesary
print(baby_step_dic)


# calculate the giant step list
# step = (math.pow(generator,Q) % mod_num)  # causes Overflow for large numbers
step = generator
for _ in range(2,Q):
    step = step * generator % mod_num

step0 = step

solution = -1

if step in baby_step_dic:
    solution = 1*Q-baby_step_dic[step]
else:
    for i in range(2, Q*Q):
        step = step * step0 % mod_num
        if step in baby_step_dic:
            solution = i*Q-baby_step_dic[step]
            break

print('The solution is: {}'.format(solution))
