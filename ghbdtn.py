import argparse
presidents = {"Putin": "7000 Ядерок, дзюдо, Танки", "Baiden": "6500 Ядерок, опасная ходьба, Авиация","Si Czinpin": "3000 Ядерок, секретные технологии, Флот"}

parser = argparse.ArgumentParser(description="Характерстики президентов")
parser.add_argument("-list", dest="param3")

args = parser.parse_args()

if args.param3:
    name, lst = args.param3.split(":")
    if name in presidents:
        presidents[name] = [presidents.get(name), int(lst)]
        print("Президент", name, "приобрёл новое вооружение")
        print(name, ":", presidents[name])
    else:
        presidents[name] = int(lst)
        print("Президент", name, "вооружён")
        print(name, ":", presidents[name])