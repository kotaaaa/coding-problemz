
n = int(input())
st = [list(map(str, input().split())) for _ in range(n)]
# s, t = [list(i) for i in zip(*st)]

sorted_arr = sorted(st, key=lambda i: int(i[1]),reverse=True)
print(sorted_arr[1][0])