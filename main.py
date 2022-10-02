
from tabulate import tabulate

class process:
    def __init__(self, value):
        self.value=value
        self.ForwardPositions=-1

    def Set_Value(self, value):
        self.value=value

    def Set_Coin(self, coin):
        self.coin=coin

    def Set_Youth(self, youth):
        self.youth=youth

    def set_ForwardPositions(self, ForwardPositions):
        self.ForwardPositions=ForwardPositions

    def get_ForwardPositions(self):
        return self.ForwardPositions

    def get_Value(self):
        return self.value


def displayMenu01():
    print("\t\t Options Menu \n\n")
    print("(1) Optimal algorithm")
    print("(2) FIFO algorithm")
    print("(3) LRU algorithm")
    print("\n\n")

if __name__ =="__main__":

    #program's while
    Entry=""
    halt=False
    while not halt:
        #input section
        rawInput=input("please write a string of integers separated by commas: ")
        splitedInput=rawInput.split(',')
        intInput = []
        for element in splitedInput:
            try:
                temp=int(element.strip())
                intInput.append(temp)
            except:
                print("error, the input must be integers only")
                halt=True
        if halt:
            break
        print(intInput)

        keyToken2=False
        framesLength=0
        while not keyToken2:
            try:
                framesLength=int(input("Enter frames length 'x' where [0 < x <=10 ]: "))
                if framesLength > 0 and framesLength <= 10:
                    keyToken2=True
            except:
                print("error, the input must be an integer")

        print(framesLength)
        ExecutionLength=len(intInput)

        keyToken3=False
        swapOption=0
        domain01=[1,2,3]
        while not keyToken3:
            try:
                displayMenu01()
                swapOption=int(input("Enter your choice: "))
                if swapOption in domain01:
                    keyToken3=True
                else:
                    print("error, input out of range, check menu")
            except:
                print("error, the input must be an integer")
        print(swapOption)

        #body section

        #I prepare fault list
        faultList=[]
        temp=0
        while (temp < ExecutionLength):
            faultList.append("pass")
            temp+=1
        f=0

        #I prepare the first frame
        AlreadyStarted=False
        FramesTable=[]

        while len(intInput) > 0:
            singleFrame=[]
            if not AlreadyStarted:
                temp=0
                while temp < framesLength:
                    singleFrame.append("pass")
                    temp+=1
            else:
                singleFrame=FramesTable[-1]

            if not intInput[0] in singleFrame: #if the process is not in frames
                print("fault report")
                faultList[f]="F"
                f+=1

            isThereRoom=False
            pos=0
            for element in singleFrame:
                if element=="pass":
                    isThereRoom=True
                    break
                pos+=1

            if isThereRoom:
                singleFrame[pos]=process(intInput[0])
            elif swapOption == 1: #Optimal
                ForwardedList=[]
                for process in singleFrame:
                    value=process.get_Value()
                    for number in intInput:
                        if number==value:
                            break
                        process.set_ForwardPositions(get_ForwardPositions()+1)
                    ForwardedLista.append(process.get_ForwardPositions())
                if -1 in ForwardedList:
                    singleFrame[index(-1)].Set_Value(intInput[0])
                else:
                    singleFrame[index(max(ForwardedList))].Set_Value(intInput[0])

            elif swapOption == 2: #FIFO

            elif swapOption == 3: #LRU

            else:
                print("Action no specified")

            FramesTable.append(singleFrame)
            intInput.pop(0)

        print(tabulate(intInput))
        print(tabulate(FramesTable))
        print(tabulate(faultList))

        #program's end section
        keyToken=False
        option=""
        while not keyToken:
            option=input("Another ride? (y:yes / n:no): ")
            if option == 'n':
                keyToken=True
                halt=True
            elif option == 'y':
                keyToken=True
            else:
                print("no valid input")

    print("\n\n END OF LINE \n\n")
