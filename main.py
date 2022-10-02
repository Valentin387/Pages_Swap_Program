


class process:
    def __init__(self, value):
        self.value=value

    def Set_Coin(self, coin):
        self.coin=coin

    def Set_Youth(self, youth):
        self.youth=youth

    def get_Value(self):
        print(self.value)


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

        #I prepare frame
        AlreadyStarted=False

        while len(intInput) > 0:
            f=0
            singleFrame=[]
            if not AlreadyStarted:
                temp=0
                while temp < framesLength:
                    singleFrame.append("pass")

            if not intInput[0] in singleFrame:
                print("fault report")
                faultList[f]="F"
            f+=1




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
