import random

def prob(probp:int,x, fallback):
    
    flip = random.randint(1,100)

    if probp > flip:
        return x
    else:
        return fallback

def rndc(x): 
    """return random.choice(x)"""
    
    return random.choice(x)

def rndcs(x):
    """
    return str(random.choice(x))
    """
    return str(random.choice(x))


n = 10
da = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
dn = "1234567890" *7
do = "+-/*"
dso = "^"

dl = [da,dn,do]

for i in range(n):

    rr = lambda fn: [f() for f in [fn]*random.randint(1,3)]
    rc = lambda: rndc(rndc([da,dn]))

    ftxt_ = lambda: [rr(rc)] +  [dso]+[rc()]  + [rndc(do)] + [rr(rc)]
        
    txt_ = ftxt_() + prob(50, [rndc(do)]+ftxt_(),[])  +prob(20,[rndc(do)]  +ftxt_(), [])

    print(str(txt_).replace("[","").replace("]","").replace('"','').replace("'","").replace(",","").replace(" ",""))
