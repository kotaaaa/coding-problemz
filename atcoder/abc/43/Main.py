
s = input()

text = ""
for i in s:
    if i == '0':
        text += i
    elif i == '1':
        text += i
    elif i == 'B':
        l = len(text)
        if l > 0:
            text = text[:l-1]

print(text)