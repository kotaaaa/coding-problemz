n, k = map(int, input().split())
x = list(map(int, input().split()))

min_val = pow(10, 9) + 1
for i in range(n - k + 1):
    if x[i + k - 1] <= 0:
        min_val = min(min_val, abs(x[i]))
    elif x[i] >= 0:
        min_val = min(min_val, x[i + k - 1])
    else:
        goback = min(abs(x[i]), x[i + k - 1])
        if abs(x[i]) < x[i + k - 1]:
            # goback = abs(x[i])
            min_val = min(min_val,2*abs(x[i])+x[i + k - 1])
        else:
            min_val = min(min_val,abs(x[i])+2*x[i + k - 1])

print(min_val)
        
