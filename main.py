


class process:
    def __init__(self, value):
        self.value=value

    def Set_Coin(self, coin):
        self.coin=coin

    def Set_Youth(self, youth):
        self.youth=youth

    def get_Value(self):
        print(self.value)


if __name__ =="__main__":

    Entry=""
    halt=True
    while halt:
        rawInput=input("please write a string of integers separated by commas: ")
        splitedInput=rawInput.split(',')
        intInput = []
        for element in splitedInput:
            try:
                temp=int(element.strip())
                intInput.append(temp)
            except:
                print("error, the input must be integers only")

        print(intInput)
        keyToken=False
        option=""
        while not keyToken:
            option=input("Another ride? (y:yes / n:no): ")
            if option == 'n':
                keyToken=True
                halt=False
            elif option == 'y':
                keyToken=True
            else:
                print("no valid input")

    print("\n\n END OF LINE \n\n")
