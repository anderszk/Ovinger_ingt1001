# Øving 3 i INGT1001 Python-modul

#1a
def sum_range() -> int:
    total = 0
    for i in range(2,101):
        total += i
    return total

#Alternativ løsning
print(sum(range(2,101)))


#1b
def sum_squares() -> int:
    total = 0
    for i in range(2,101):
        total += i**2
    return total


#1c
def sum_power_2() -> int:
    total = 0
    for i in range(0,21):
        total += 2**i
    return total


#1d
def sum_odds_interval() -> int:
    a = int(input("Enter value A here: "))
    b = int(input("Enter value B here: "))
    total = 0
    for i in range(a,b+1):
        if i % 2 == 1:
            total += i
    return total


#1e
def add_digits() -> int:
    num = input("Enter a number here: ")
    total = 0
    for i in num:
        if int(i)%2 == 1:
            total += int(i)
    return total



#16
def factors_on_n() -> None:
    num = int(input("Enter a integer here: "))
    for i in range(1, num+1):
        if num % i == 0:
            print(i)


#17
def primes_upto_n() -> None:
    num = int(input("Enter a number here: "))













#2a



