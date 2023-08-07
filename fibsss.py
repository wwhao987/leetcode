
import sys
sys.setrecursionlimit(10000)
def FasteRecFubo(n):
    m = n/2
    hprv, hcur = FasteRecFubo(m-1,m)
    prev = hprv**2+hcur**2
    curr = hcur*(2*hprv+hcur)
    next = prev+curr
    if n%2==1:
        return prev,curr
    
    else:
        return curr,next
    
    
print(FasteRecFubo(10))