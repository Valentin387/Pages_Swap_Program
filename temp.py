import random

for ini in range(3):
    for i in range(10):
        if i==5:
            if i % 2 == 1:
                break
                print("odd")
        print("i:", i)
    print("ini: ", ini)
