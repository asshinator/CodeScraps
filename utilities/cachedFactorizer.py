"""Efficiently prime-factorize N integers. Cache for the N+1th"""

class cachedFactorizer:
    def __init__(self):
        self.sieve = []
        self.primeList = []
        self.entries = []
        self.factorizedEntries = []
        self.numberOfFactorizedEntries = 0
        self.sieveConsolidatedUpto = 0
    def add(self, number:int):
        self.entries += [number]
    def evaluate(self):
        start = self.numberOfFactorizedEntries
        biggestEntry = max(self.entries[start:])
        sqrt = 10000 # square root of biggestEntry
        self.factorizedEntries += (len(self.entries) - start)*[{}]
        #fill the sieve.
        startSieve = len(self.sieve)
        self.sieve += [True]*(biggestEntry - startSieve)
        for x in range(2,sqrt):
            for y in range(startSieve // x, sqrt // x):
                self.sieve[x*y] = False
                consolidateSieve(x*x)
    def consolidateSieve(self,number:int):
        start = self.sieveConsolidatedUpto
        if(start>=number):
            return
        for x in range(start,number):
            if(self.sieve[x]==True):
                self.primeList += [x]
        self.sieveConsolidatedUpto = number

        