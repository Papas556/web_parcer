link = "https://feedback.edadeal.ru/default"
if "=" in link:
    link = link.split("=")
    number = int(link[-1])
    print(number)