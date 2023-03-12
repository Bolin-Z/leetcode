# IS-A structure
class LogicGate:
    """
    Super class of logic gate
    """
    def __init__(self, n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
    def performGateLogic(self):
        pass

    def setNextPin(self, source:"Connector"):
        pass
    
class BinaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None
    
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()
            
    
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

class UnaryGate(LogicGate):
    def __init__(self, n):
        super().__init__(n)

        self.pin = None
    
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):       
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)
    
    def performGateLogic(self):
        x = self.getPin()
        return 1 if x == 0 else 0

# HAS-A structure
class Connector:
    def __init__(self, fgate:"LogicGate", tgate:"LogicGate") -> None:
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate

if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())

    