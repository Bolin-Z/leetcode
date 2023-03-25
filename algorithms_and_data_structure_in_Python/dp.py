# recursion
def recMC(coinValueList:list[int], change:int) -> int:
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins

# recursion with memory
def recDC(coinValueList:list[int], change:int) -> int:
    knownResult = [0] * (change + 1)
    def __recDC(coinValueList:list[int], change:int) -> int:
        minCoins = change
        if change in coinValueList:
            knownResult[change] = 1
            return 1
        elif knownResult[change] > 0:
            return knownResult[change]
        else:
            for i in [c for c in coinValueList if c <= change]:
                numCoins = 1 + __recDC(coinValueList, change - i)
                if numCoins < minCoins:
                    minCoins = numCoins
                    knownResult[change] = minCoins
        return minCoins
    return __recDC(coinValueList, change)

# dynamic programming version
def dpMakeChange(coinValueList:list[int], change:int) -> int:
    minCoins = [0] * (change + 1)
    for cents in range(change + 1):
        coinCount = cents # charge by 1-cent
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins[change]

class DpMakeChangeWithSolver:
    def __init__(self) -> None:
        self.__flag = False

    def solve(self, coinValueList:list[int], change:int) -> None:
        self.__coinsUsed = [0] * (change + 1)
        self.__change = change
        self.__result =self.__dpMakeChangeWithSol(coinValueList, self.__change)
        self.__flag = True
    
    def getResult(self) -> int:
        result = None
        if self.__flag:
            result = self.__result
        return result

    def __dpMakeChangeWithSol(self, coinValueList:list[int], change:int) -> int:
        minCoins = [0] * (change + 1)
        for cents in range(change + 1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coinValueList if c <= cents]:
                if minCoins[cents - j] + 1 < coinCount:
                    coinCount = minCoins[cents - j] + 1
                    newCoin = j
            minCoins[cents] = coinCount
            self.__coinsUsed[cents] = newCoin
        return minCoins[change]
    
    def printCoins(self) -> None:
        if self.__flag:
            print("solution: ",end="")
            coin  = self.__change
            while coin > 0:
                thisCoin = self.__coinsUsed[coin]
                print(thisCoin, end=" ")
                coin = coin - thisCoin
            print("")

DpMakeChangeSolver = DpMakeChangeWithSolver()

if __name__ == "__main__":
    DpMakeChangeSolver.solve([1, 5, 10, 25], 63)
    print(DpMakeChangeSolver.getResult())
    DpMakeChangeSolver.printCoins()