# kontrola kolize

x1_oblast = 4
y1_oblast = 2
x2_oblast = 9
y2_oblast = 7

xb = int(input("Zadejte x souřadnici bodu: "))
yb = int(input("Zadejte y souřadnici bodu: "))

x_min = min(x1_oblast, x2_oblast)
x_max = max(x1_oblast, x2_oblast)
y_min = min(y1_oblast, y2_oblast)
y_max = max(y1_oblast, y2_oblast)

if x_min < xb < x_max and y_min < yb < y_max:
    print("Varianta 1: Bod se nachází uvnitř oblasti.")
if xb < x_min or xb > x_max or yb < y_min or yb > y_max:
    print("Varianta 2: Bod se nachází mimo oblast.")
elif x_min <= xb <= x_max and y_min <= yb <= y_max and (xb == x_min or xb == x_max or yb == y_min or yb == y_max):
    if xb == x_min and yb == y_min:
        print("Varianta 3: Bod se nachází na hranici oblasti - vlevo dole.")
    elif xb == x_min and yb == y_max:
        print("Varianta 3: Bod se nachází na hranici oblasti - vlevo nahoře.")
    elif xb == x_max and yb == y_min:
        print("Varianta 3: Bod se nachází na hranici oblasti - vpravo dole.")
    elif xb == x_max and yb == y_max:
        print("Varianta 3: Bod se nachází na hranici oblasti - vpravo nahoře.")

        

