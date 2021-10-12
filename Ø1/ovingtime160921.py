#Vil gi True hvis og bare hvis inputen ikke er "stopp"
def validator(string: str) -> bool:
    if string != "stopp":
        return True
    else:
        return False

def min_max():
    inp = input("Skriv inn tall her: ")
    highest = int(inp)
    lowest = int(inp)
    while validator(inp):
        num = int(inp)  # Caster string-input til integer
        if num < lowest:  # Sammenligner med laveste gitte tall
            lowest = num  # Setter verdi
        if num > highest:  # Sammenligner med laveste gitte tall
            highest = num  # Setter verdi
        inp = input("Skriv inn et nytt tall her (skriv 'stopp' hvis du vil avslutte): ")  # Ny input

    # Printer max og min
    print("Highest number is: %d, lowest number is: %d" % (highest, lowest))


if __name__ == "__main__":
    #Vil kjøre sålenge input ikke er "stopp" eller et tall
    try:
       min_max()

    except ValueError as e:
        print("""This is an invalid input! 
    Please enter an number
    and write 'stopp' if you want to exit""")
        min_max()









