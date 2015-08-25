import sys
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
class Decomp:
    def __init__(self, time, state, k):
        self.subA = state[1]
        self.subB = state[0]
        self.subC = state[2]
        self.k = k[1]
        
    def showdata(self, t, s):
        sys.stdout.write(RED+"{0:>8}".format(round(t,6))+ENDC)
        sys.stdout.write("{0:>8}".format('%d' % (s[0])))
        sys.stdout.write("{0:>8}".format('%d' % (s[1])))
        sys.stdout.write("{0:>8}".format('%d' % (s[2])))
        print
        
    def propensity(self, s):
        return self.k*s[2]
    
    def execute(self, state):
        state[0] += 1
        state[1] += 1
        state[2] -= 1
        return state
