# P1.1
print("Witam kurwa")

# P1.2
total = 0
iterator = 0
while iterator < 10:
    iterator += 1
    total += iterator

print(total)

# P1.3
total = 0
iterator = 0
while iterator < 10:
    iterator += 1
    if total == 0:
        total = 1
    total *= iterator

print(total)


# P1.4
def cash_money(balance, interest, years):
    gainz = balance * ((1 + interest/100) ** years)
    return gainz

print(cash_money(1000, 5, 3))


# P1.5
print("""+-----+
| Anders |
+-----+""")


# P1.16
print("""English                         Norwegian
-----------------------------   ------------------------------------
Good morning.                   God morgen.
It's a pleasure to meet you.    Hyggelig å møte deg.
Please call me tomorrow.        Ring meg imorgen er du snill?
Have a nice day!                Ha en fin dag!
""")


# P2.4
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
print("""
Sum: {}
Difference: {}
Product: {}
Average: {}
Distance: {}
Minimum: {}
Maximum: {}\n"""
.format(a+b,a-b, a*b, (a+b)/2, abs(a-b), min(a, b), max(a, b)))


# P2.19
def num_2_month():
    months = ["January","February","March","April","May","June","July","August","September", "October", "November","December"]
    number = int(input("Enter your number between 1-12: "))
    if number > 12:
        print("You were supposed to pick a number between 1-12!")
        num_2_month()
    else:
        print("Your chosen month is: " + months[number-1] + "\n")

num_2_month()


#P 2.22
def validator(string):
    return len(string) >= 6
def dotdotdot():
    string = input("Enter a word here!: ")
    if validator(string):
        print("%s...%s\n" % (string[0: 3], string[len(string) - 3: len(string)]))
    else:
        print("String must be atleast 6 characters long")
        dotdotdot()

dotdotdot()


# P2.32
def validator(int):
    return int >= 0
def compute_price():
    shipping = 2
    tax = 0.075
    books = int(input("Enter the number of books here: "))
    price = float(input("Enter the price of the book here: "))
    if not (validator(books) & validator(price)):
        print("Cannot be negative!")
        compute_price()
    else:
        final_price = (price+price*tax+shipping) * books

        print("The total cost of the order is $%.2f.\n" % final_price)

compute_price()


# P2.35


