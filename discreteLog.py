'''
    This is an implementation of the Babystep - Giantstep algorithm in order 
    to solve the descreet logarithm problem. As described in Section 2.1 "The Classical Baby-Step Giant-Step Algorithm"
    In: https://www.ssi.gouv.fr/archive/fr/sciences/fichiers/lcr/colepo05.pdf
'''

# calculates gratest comen divisor Sourced from:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# calculates the modular inverse. Sourced from:
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def calculate_discrete_power(num: int, exp: int, mod: int) -> int:
    '''Calculates the discrete power of num ^ exp % mod and returns an int.

    Args:
        num (int): the number that is raised to the power
        exp (int): the power to which num is raised
        mod (int): the value of the modulo.
    '''
    ans = 1
    for _ in range(1, exp+1):
        ans = (ans * num) % mod
    return ans


def calculate_descreet_log(ans: int, generator: int, modulo: int, Q: int) -> int:
    '''Calculates the exponent to which a generator has been raised 
    given the answer, the generator and the modulo and returns the value of the
    exponent as an int. If no solution is found -1 is returned

                        ans = generator ^ exponent % modulo

    Args:
        ans (int)       : the result of generator ^ exponent % modulo
        generator (int) : the generator used in order to calulate the ans
        modulo (int)   : the modulo used in the equation above
        Q (int)         : defines the range that should be searched, this is limited manualy
                            in order for the calculations to return a result within a usefull time.
    '''

    # calculation of the baby step list:
    baby_step_dic = {}
    step = 1

    
    # populating the baby_step_dic
    for i in range(0, Q):
        baby_step_dic[(step % modulo)] = i
        step = step * generator % modulo

    
    # calculate the giant step list
    #
    # the last value for step after the for loop populating the baby_step_dic is generator ^ (Q-1).
    # the first value of the giant step list is generator ^ Q so we can easely derive the first value of the
    # giant list from the last value of step.
 
    solution = -1  # if no solution is found -1 returned

    # calculate mod inverse of step
    inw_step = modinv(step, modulo)
    step = ans

    for i in range(0, Q+1):
        if step in baby_step_dic:
                        solution = (i*Q + baby_step_dic[step]) % modulo
                        break
        step = (step * inw_step) % modulo
            

    return solution

import math
if __name__ == '__main__':
    # Setup of the variables in the form of:
    # ans = generator ^ exponent % modulo
    generator = 439
    modulo = 104729
    exponent = 23427
    ans = calculate_discrete_power(generator, exponent, modulo)
    Q = 10000 # limit to prevent from calculation not termenating within usefull time.
    if(Q > math.ceil(math.sqrt(modulo))): # if the Q is biger than sqrt(modulo) rounded up, the program doesn't work properly
        Q = math.ceil(math.sqrt(modulo))  

    ex = calculate_descreet_log(ans, generator, modulo, Q)
    print('The exponent which was used was: {}\nThis answer is: {}'.format(
        ex, exponent == ex))
