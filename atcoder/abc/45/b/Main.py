a = input()
b = input()
c = input()

a_i = 0
b_i = 0
c_i = 0

current =  'a'
while True:
    if current == 'a':
        if a_i >= len(a):
            print("A")
            exit()
        next_ = a[a_i]
        a_i += 1
    elif current == 'b':
        if b_i >= len(b):
            print("B")
            exit()
        next_ = b[b_i]
        b_i += 1
    elif current == 'c':
        if c_i >= len(c):
            print("C")
            exit()
        next_ = c[c_i]
        c_i += 1
    current = next_
