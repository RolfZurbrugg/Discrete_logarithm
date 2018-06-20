'''
    This is an implementation of the Babystep - Giantstep algorithm in order 
    to solve the descreet logarithm problem.
'''


def calculate_discrete_power(num: int, exp: int, mod: int) -> int:
    '''Calculates the discrete power of num ^ exp % mod and returns an int.

    Args:
        num (int): the number that is raised to the power
        exp (int): the power to which num is raised
        mod (int): the value of the modolo.
    '''
    ans = 1
    for _ in range(1, exp+1):
        ans = (ans * num) % mod
    return ans


def calculate_descreet_log(ans: int, generator: int, mod_num: int, Q: int) -> int:
    '''Calculates the exponent to which a generator has been raised 
    given the answer, the generator and the modolo and returns the value of the
    exponent as an int. If no solution is found -1 is returned

                        ans = generator ^ exponent % mod_num

    Args:
        ans (int)       : the result of generator ^ exponent % mod_num
        generator (int) : the generator used in order to calulate the ans
        mod_num (int)   : the modolo used in the equation above
        Q (int)         : defines the range that should be searched, this is limited manualy
                            in order for the calculations to return a result within a usefull time.
    '''

    # calculation of the baby step list:
    baby_step_dic = {}    
    step = ans % mod_num  # calculating step 0
    baby_step_dic[step] = 0

    # populating the baby_step_dic
    for i in range(1, Q):
        step = step * generator % mod_num
        baby_step_dic[step] = i

    # calculate the giant step list
    step = calculate_discrete_power(generator, Q, mod_num)
    step0 = step
    solution = -1  # if no solution is found -1 returned

    if step in baby_step_dic:
        solution = 1*Q-baby_step_dic[step]
    else:
        for i in range(2, Q+1):
            step = step * step0 % mod_num
            if step in baby_step_dic:
                solution = i*Q-baby_step_dic[step]
                break

    return solution


if __name__ == '__main__':
    # Setup of the variables in the form of:
    # ans = generator ^ exponent % mod_num
    generator = 439
    mod_num = 104729
    exponent = 23425
    ans = calculate_discrete_power(generator, exponent, mod_num)
    Q = 100000  # Set limit to prevent from calculation not termenating within usefull time.

    ex = calculate_descreet_log(ans, generator, mod_num, Q)
    print('The exponent which was used was: {}\nThis answer is: {}'.format(ex, exponent==ex))
