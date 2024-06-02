import argparse
house = {"flat1":{"id":1, "name":"Leo", "clothes":"T-shirt"}, "flat2":{"id":2, "name":"Petr", "clothes":"Jeans"}, "flatF3":{"id":3, "name":"Denis", "clothes":"Jacket"}}

def changeFlats(Leo, Petr, Denis):

day=1
events={{"event":changeFlats(), "probability":0.6}, {"event":changeClothes }}

while True:
    command = input("->")
    if command == "next":
        day+=1
        print(f"today is {day} day")