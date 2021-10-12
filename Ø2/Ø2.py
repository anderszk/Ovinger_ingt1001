#3.1
def checker(i:int) -> str:
    if i < 0:
        return "negative"
    elif i > 0:
        return "positive"
    elif i == 0:
        return "zero"

#3.2
def checker2(f:float) -> str:
    if f < 0:
        if f > -1:
            return "small negative"
        else:
            return "negative"
    elif f > 0:
        if f < 1:
            return "small positive"
        else:
            return "positive"
    elif f == 0:
        return "zero"


#3.3



