def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Iterative Python 3 program to find 
# modular inverse using extended 
# Euclid algorithm 
  
# Returns modulo inverse of a with 
# respect to m using extended Euclid 
# Algorithm Assumption: a and m are 
# coprimes, i.e., gcd(a, m) = 1 
# 
# Gets u.
def mod_inverse_u(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x

# Get v  
def mod_inverse_v(p, u, q):
    return (1 - p * u) // q

p = 26513
q = 32321
g = gcd(p, q) # gcd = 1

# pu + qv = 1
# v = (1 - pu) / q

# 26513 * u + 32321 * v = 1
# 26513 * 10245 + 32321v = 1
# 271625685 + 32321v = 1
# 32321v = -271625684
# v = -271625684 / 32321  = -8404

u = mod_inverse_u(p, q)
v = mod_inverse_v(p, u, q)

print(f"p={p}, q={q}, u={u}, v={v}")