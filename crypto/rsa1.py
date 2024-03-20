from gmpy2 import *
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

p = 473398607161
q = 4511491
e =  17

n = p*q
phi =(p-1)*(q-1)
d = gmpy2.invert(e, phi)
print(d)