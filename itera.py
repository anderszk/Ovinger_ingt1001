
list1 = [5,3,2,6,7,1,6]

def second_largest(l:list) -> int:
    l.sort()
    return l[len(l)-2]


def n_largest(l:list, n:int) -> int:
    l = list(set(l))
    l.sort()
    return l[len(l)-n]


def encoder(s:str) -> str:
    vowels = ["a", "e", "i", "o", "u", "y", " "]
    new_word = ""
    for index, char in enumerate(s):
        if char not in vowels:
            new_word += char +"o"+char
        else:
            new_word += char
    return new_word

print(encoder("my name is bob"))
