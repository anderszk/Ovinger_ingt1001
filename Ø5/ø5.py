#1
def hello_file() -> str:
    file = open("helloworld.txt", "w")
    file.write("Hello World!")
    file.close()
    return open("helloworld.txt", "r").read()

#2
file = open("oppg4.txt", "w")




