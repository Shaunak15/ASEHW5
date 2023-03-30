import math
class Num():
    
    ## constructor created for Num class
    def __init__(self, at = 0, txt = ""):
        self.at = at
        self.txt = txt

        self.n = 0
        self.mu = 0
        self.m2 = 0

        self.lo = float('inf')
        self.hi = float('-inf')
        self.has =[]
        self.w = -1 if '-$' in txt else 1

    def at(self):
        return self.at

    def txt(self):
        return self.txt
    
    def add(self, value):
        if value != '?':
            float_value = float(value)
            self.n = self.n + 1
            d = float_value - self.mu
            self.mu = self.mu + (d / self.n)
            self.m2 = self.m2 + (d * (float_value - self.mu))
            self.lo = min(float_value, self.lo)
            self.hi = max(float_value, self.hi)

    def mid(self):
        return self.mu

    #n; return standard deviation using Welford's algorithm 
    def div(self): 
        if((self.m2 < 0) or (self.n < 2)):
            return 0
        return pow((self.m2 / (self.n - 1)), 0.5)

    def rnd(self, x, n):
        if x == "?":
            return x
        mult = math.pow(10, n)
        return math.floor(x*mult + 0.5) / mult

    def norm(self, n):
        return n == "?" and n or (n - self.lo)/(self.hi - self.lo + 1e-32)
    
    def dist(self,n1,n2):
        if n1 == "?" and n2 == "?":
            return 1
        n1 = self.norm(n1)
        n2 = self.norm(n2)
        if n1 == "?":
            n1 = n2 < 0.5 and 1 or 0
        if n2 == "?":
            n2 = n1 < 0.5 and 1 or 0
        return abs(n1-n2)