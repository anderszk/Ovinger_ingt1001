#oppg4
def swap_first_last(nums: list) -> list:
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums


#oppg6
def sumWithoutSmallest(nums: list) -> int:
    nums.sort()
    return sum(nums) - nums[0]


#oppg8
def alternate_sum(nums: list) -> int:
    total = 0
    for i in nums:
        if nums.index(i)%2 == 0:
            total += i
        else:
            total -= i
    return total


#oppg9
def reverseList(nums: list) -> list:
    nums.reverse()
    return nums


import random
#oppg15
def toss() -> list:
    nums = []
    for i in range(0,20):
        nums.append(random.randint(0,6))
    return nums


#Oppg16
def sort_toss(nums: list):
    run = False
    for index, value in enumerate(nums):
        try:
            if run == False and nums[index+1] == value:
                run = True
                print("(", end=" ")
                print(value, end=" ")
            elif run == True and nums[index+1] != value:
                run = False
                print(value, end=" ")
                print(")", end=" ")
            else:
                print(value, end=" ")
        except IndexError as ie:
            break


#Oppg27
price_chart = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
               [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
               [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
               [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
               [10, 10, 20, 20, 20, 20, 20, 20, 10, 10],
               [20, 20, 30, 30, 40, 40, 30, 30, 20, 20],
               [20, 30, 30, 40, 50, 50, 40, 30, 30, 20],
               [30, 40, 50, 50, 50, 50, 50, 50, 40, 30]]


def book_seat():
    global price_chart
    found = False
    prompt = input("Enter (P)rice, (S)eat, or (Q)uit: ")
    price_classes = [10, 20, 30, 40, 50]

    while prompt != "Q":
        if prompt == "P":
            price = int(input("Enter a price here, prices are 10, 20, 30, 40 and 50: "))
            if price in price_classes:
                for index, row in enumerate(price_chart):
                    if found == False:
                        for index2, seat in enumerate(row):
                            if seat == price:
                                print("Your seat is: in row:",index+1,"and column: ",index2+1)
                                price_chart[index][index2] = 0
                                found = True
                                break
                    else:
                        found = False
                        break
            else:
                print("Please enter a valid input")

        elif prompt == "S":
            row = int(input("Enter the desired row (1-9): "))
            seat = int(input("Enter the desired seat (1-10): "))
            if 1 <= row <= 9 and 1 <= seat <= 10:
                if price_chart[row - 1][seat - 1] != 0:
                    price_chart[row-1][seat-1] = 0
                    print("Your seat is booked in row:", row, "and seat: ",seat)
                else:
                    print("Seat taken, please try again")
            else:
                print("Your inputs were invalid, please try again")

        else:
            print("Please follow the instructions on valid inputs in the parantheses")

        prompt = input("Enter (P)rice, (S)eat, or (Q)uit: ")

    for i in price_chart:
        print(i)
        print("\n")


def appendList(num1: list, num2:list) -> list:
    return num1+num2

num1= [1,2,3,7,8,9,0]
num2 = [4,5,6]

def merge(num1: list, num2:list) -> list:
    new = []
    for i in range(0, min(len(num1), len(num2))):
        new.extend([num1[i],num2[i]])
    return new+num1[len(num2):] if max(len(num1), len(num2)) == len(num1) else new+num2[len(num1):]


print(merge(num1,num2))







