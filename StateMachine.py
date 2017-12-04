class StateMachine:
    'Design a representation of the finite state machine using a python dictionary to represent transitions.'

    currState = 'A' #Initial current state

    #TRANSITIONS
    aTrans = {'a' : 'B', 'b' : 'C'}
    bTrans = {'a' : 'B', 'b' : 'D'}
    cTrans = {'a' : 'E', 'b' : 'F'}
    dTrans = {'a' : 'B', 'b' : 'G'}
    eTrans = {'a' : 'E', 'b' : 'E'}
    fTrans = {'a' : 'H', 'b' : 'E'}
    gTrans = {'a' : 'I', 'b' : 'G'}
    hTrans = {'a' : 'H', 'b' : 'H'}
    iTrans = {'a' : 'I', 'b' : 'I'}

    #STATES
    states = {'A' : aTrans, 'B' : bTrans, 'C' : cTrans, 'D' : dTrans, 'E' : eTrans, 'F' : fTrans, 'G' : gTrans, 'H' : hTrans, 'I' : iTrans}

    #BOOLEAN DICTIONARY FOR STATES & TRANSITIONS. 'TRUE' MEANS THAT THE STATE AND/OR TRANSITION HAS BEEN VISITED BY THE STATE MACHINE.
    usedStates = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False, 'H': False,
              'I': False}  # All states are initially unused
    usedTransition = {'A:a': False, 'A:b': False, 'B:a': False, 'B:b': False, 'C:a': False, 'C:b': False, 'D:a': False,
                   'D:b': False, 'E:a': False, 'E:b': False, 'F:a': False, 'F:b': False, 'G:a': False, 'G:b': False,
                   'H:a': False, 'H:b': False, 'I:a': False, 'I:b': False}


    def getCurrState(self):
        return self.currState

    def getUsedStates(self):
        return self.usedStates

    def getUsedTransitions(self):
        return self.usedTransition

    def isStringCompatible(self, str):
        self.currState = self.getLastState(str)
        if (self.currState == 'I' or self.currState == 'H'):
            print "TRUE"
            return "TRUE"
        else:
            print "FALSE"
            return "FALSE"

    def getLastState(self, str):
        self.clear() #RESET
        for char in str:
            try:
                self.usedStates[self.currState] = True
                self.usedTransition[self.currState + ":" + char] = True
                self.currState = self.states[self.currState][char]
                self.usedStates[self.currState] = True
            except:
                return "error"
                print "FALSE"
        print self.usedStates
        return self.currState

    def clear(self):
        self.currState = 'A'
        self.usedStates = {key: False for key in self.usedStates}
        self.usedTransition = {key: False for key in self.usedTransition}
