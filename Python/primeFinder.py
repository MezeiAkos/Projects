n = input("n= ")

listOfNumbers = [True for i in range(int(n) + 1)]
for index, item in enumerate(listOfNumbers):
    if item and index > 1:
        j = 2
        while j < int(n):
            if index * j > int(n):
                break
            listOfNumbers[index * j] = False

            j += 1
for index, item in enumerate(listOfNumbers):
    if item:
        print(index)
