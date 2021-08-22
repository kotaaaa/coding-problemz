
x = input()
# print(x.find('.'))
dot = x.find('.')
if dot == -1:
    print(x)
else:
    print(x[:x.find('.')])