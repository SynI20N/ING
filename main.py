import argparse
book = {"Masha": 123, "Pasha": 1234, "Natasha": 32415}

parser = argparse.ArgumentParser(description="Telephone book")
parser.add_argument("-a","--add", dest="param1")

args = parser.parse_args()

if args.param1:
    name, tele = args.param1.split(":")
    if name in book:
        book[name] = [book.get(name), int(tele)]
        print("Контакт с именем", name, "обновлен")
        print(name, ":", book[name])
    else:
        book[name] = int(tele)
        print("Контакт с именем", name, "добавлен")
        print(name, ":", book[name])