
s = input()
rs = s[::-1]
# rs.replace("6","")
for e,i in enumerate(rs):
    if i == "6":
        print("9",end="")
    elif i == "9":
        print("6",end="")
    else:
        print(i,end="")