
import collections
from bb26 import int_to_BB26


primes = {} # Must start empty or with contain all primes up to its highest (as keys)


def prime_factors(n):
    i = 2
    factors = []
    
    if primes and max(primes.keys())**2 < n:
        known_primes = iter(())
    else:
        known_primes = iter(tuple(primes.keys()))
    
    while i * i <= n:
        if n % i:
            i = next(known_primes, i+1)
        else:
            n //= i
            factors.append(i)
            primes[i] = None
    if n > 1:
        factors.append(n)
    return factors
    
    
def prettify_factors(factors, convert = lambda x: x):
    
    if len(factors) <= 1:
        return "neither prime nor composite" if factors == [] else "prime number"
        
    return '*'.join(f'{convert(factor)}^{convert(freq)}' if freq > 1 else f'{convert(factor)}' 
                   for factor, freq in collections.Counter(factors).items()
                  )
                  
                  
print('BB26 prime factorisations: ')           
for x in range(680, 703):
    print(f'{int_to_BB26(x)}={prettify_factors(prime_factors(x), int_to_BB26)}')
