#binary search
import random

def findNumber():
    try:
        lengthOfList = int(input("\nEnter the amount of numbers you want in the list: "))
        targetNumber = int(input("Enter the number you want to find: "))
    except Exception as Error:
        print("Error: ", Error)

    counter = 0

    while True:
        try:
            theList = random.choices(range(1, 101), k =lengthOfList) # created a list of random numbers
            sortedList = sorted(theList)
            middleNumberInList = (len(sorted(theList)) // 2)

            middleValue = sortedList[middleNumberInList]

            completed = (targetNumber == middleValue)

            if (completed):
                print(f"\nNumber you picked: {targetNumber}\nNumber found: {middleValue}\nList Length: {len(sortedList)}\nTime long it took: {counter}(s)\n")
                break
            else:
                counter += 1
                print(f"({counter}'s) *working*")
                if (targetNumber < middleValue):
                    SearchLeft(sortedList, targetNumber)
                elif (targetNumber > middleValue):
                    SearchRight(sortedList, targetNumber)

        except Exception as Error:
            print("Error: ", Error)
        
def SearchLeft(sortedList, targetNumber, start = [0], end = None):
    if (end == None):
        end = len(sortedList)

def SearchRight(sortedList, targetNumber, start = None, end = None):
    if (end == None):
        end = len(sortedList)


findNumber()