import argparse
presidents = {"Путин": ["7000 Ядерок", "дзюдо", "Танки"], "Baiden": ["6500 Ядерок", "опасная ходьба", "Авиация"],"Si Czinpin": ["3000 Ядерок", "секретные технологии", "Флот"]}
parser = argparse.ArgumentParser(description="Характерстики президентов")
parser.add_argument("-a", "-add", dest="param1")
parser.add_argument("-l", "-list", dest="param2")

args = parser.parse_args()

if args.param1:
    name, skills = args.param1.split(":")
    if name in presidents:
        presidents.get(name).append(skills)
        print("Президент", name, "приобрёл новое вооружение")
        print(name, ":", presidents[name])
    else:
        presidents[name] = skills
        print("Президент", name, "вооружён")
        print(name, ":", presidents[name])
if args.param2:
    for name, skills in presidents.items():
        print(name, ":", skills)