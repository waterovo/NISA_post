import binascii
import gmpy2
from Crypto.Util.number import *
p=1249559655343546956371276497499
q=1249559655343546956371276497489
r=1249559655343546956371276497537
s=1249559655343546956371276497423
e=0x10001
c=0x22fda6137013bac19754f78e8d9658498017f05a4b0814f2af97dc2c60fdc433d2949ea27b13337961ef3c4cf27452ad3c95
n=p*q*r*s

phi=(p-1)*(q-1)*(r-1)*(s-1)
d=gmpy2.invert(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))
