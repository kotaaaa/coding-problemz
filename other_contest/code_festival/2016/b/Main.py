n = int(input())

i = 1
val = 0
vals = []
while val < n:
    # print("i ",i,"val ",val,"vals",vals)
    # val += ((i+1)*i)//2
    val += i
    vals.append(i)
    i += 1
    

# val += i
# vals.append(i)
# print(vals, val)
if val - n != 0:
    vals.remove(val - n)

# print(vals, val)

for i in vals:
    print(i)