list1 = [1,2,3]
list2 = []




weather_forecast = "I morgen får Trøndelag sol. Nordland for det meste solfylt, litt regn i indre strøk"
def occurences(weather_forecast, keyword):
    count = 0
    for i in weather_forecast.split(" "):
        if keyword.upper() in i.upper():
            count += 1
    return count

print(occurences(weather_forecast, "sol"))

inte = "5"
def check(number_str):
    l = number_str
    if "." in number_str:
        l = number_str.split(".", 1)
    if "".join(l).isdigit():
        return True
    else:
        return False


def clothing(weather: str) -> str:
    if weather.upper() == "SOL":
        return "shorts"
    elif weather.upper() == "REGN":
        return "regnbukse"
    elif weather.upper() == "SNØSTORM":
        return "bobledress"
    else:
        return None


weather_data = [["sol", 1],["regn", 13]]

def add_weather(weather_data, todays_weather):
    if any(todays_weather in i for i in weather_data):
        for i in weather_data:
            print(i)
            if todays_weather in i:
                i[1] += 1
    else:
        weather_data.append([todays_weather, 1])


weather_data = [["sol", 2],["regn", 13],["vind", 5], ["torden", 1]]

def log_much_weather_data (weather_data:list, weather_list:list) -> None:
    for i in weather_list:
        if any(i[0] in j for j in weather_data):
            for count in weather_data:
                if i[0] in count:
                    count[1] += i[1]
        else:
            weather_data.append([i[0], i[1]])


print(weather_data)
log_much_weather_data(weather_data,[["sol", 2],["regn", 13],["vind", 5], ["torden", 1]])
print(weather_data)
