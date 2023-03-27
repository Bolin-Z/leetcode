from typing import Any
import random

class Queue:
    def __init__(self) -> None:
        self.items = []
    def isEmpty(self) -> bool:
        return self.items == []
    def enqueue(self, item:Any) -> None:
        self.items.insert(0, item)
    def dequeue(self) -> Any:
        return self.items.pop()
    def size(self) -> int:
        return len(self.items)

    @staticmethod
    def test() -> None:
        q = Queue()
        print(q.isEmpty())
        q.enqueue('dog')
        q.enqueue(4)
        q.enqueue(True)
        print(q.size())
        print(q.isEmpty())
        q.enqueue(8.4)
        print(q.dequeue())
        print(q.dequeue())
        print(q.size())

class HotPotatoSim:
    @staticmethod
    def hotPotato(namelist:list[str], num:int) -> str:
        simQueue = Queue()
        for name in namelist:
            simQueue.enqueue(name)
        
        while simQueue.size() > 1:
            for i in range(num):
                simQueue.enqueue(simQueue.dequeue())
            simQueue.dequeue()
        
        return simQueue.dequeue()
    
    @staticmethod
    def test() -> None:
        namelist = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
        print(HotPotatoSim.hotPotato(namelist, 7))


class Task:
    def __init__(self, time:int) -> None:
        self.timestamp = time
        self.pages = random.randrange(1, 21)
    
    def getStamp(self) -> int:
        return self.timestamp
    
    def getPages(self) -> int:
        return self.pages
    
    def waitTime(self, currenttime:int):
        return currenttime - self.timestamp

class Printer:
    """
    Printer class
    """
    def __init__(self, ppm:int) -> None:
        self.pagerate : int = ppm
        self.currentTask : Task = None
        self.timeRemaining : int = 0
    
    def tick(self) -> None:
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self) -> bool:
        return self.currentTask != None
    
    def startNext(self, newTask : Task):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60/self.pagerate

class PrinterSim:
    @staticmethod
    def simulation(numSeconds:int, pagesPerMinute:int) -> None:
        
        labprinter = Printer(pagesPerMinute)
        printQueue = Queue()
        waitingtimes = []

        for currentSecond in range(numSeconds):

            if PrinterSim.newPrintTask():
                task = Task(currentSecond)
                printQueue.enqueue(task)
            
            if (not labprinter.busy()) and (not printQueue.isEmpty()):
                nexttask:Task = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter.startNext(nexttask)
            
            labprinter.tick()
    
        averageWait = sum(waitingtimes) / len(waitingtimes)
        print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))

    @staticmethod
    def newPrintTask() -> bool:
        num = random.randrange(1, 181)
        return num == 180

if __name__ == "__main__":
    for i in range(10):
        PrinterSim.simulation(3600, 10)