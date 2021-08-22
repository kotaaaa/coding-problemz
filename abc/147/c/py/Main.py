n = int(input())
x = [[0 for _ in range(15)] for _ in range(15)]
y = [[0 for _ in range(15)] for _ in range(15)]
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        x[i][j],y[i][j] = map(int,input().split())
# print(x,y,a)
max_true_person_cnt = 0
for i in range(2**n):
    true_person = [0 for _ in range(n)]
    true_person_cnt = 0
    for j in range(n):
        # print("i",i,"j",j,(i>>j)&1,(i>>j)&1 == 1)
        if (i>>j)&1 == 1:
            true_person[j] = 1
            true_person_cnt += 1
    is_ok = True
    # print(true_person)
    for j in range(n):
        for k in range(a[j]):
            # print("j",j,"k",k,x[j][k],y[j][k])
            if true_person[j] == 1 and true_person[x[j][k]-1] == y[j][k]:
                continue
            # if true_person[j] == 0 and true_person[x[j][k]-1] != y[j][k]:
            if true_person[j] == 0:
                continue
            is_ok = False
            break
    if is_ok:
        max_true_person_cnt = max(max_true_person_cnt,true_person_cnt)
    # print("true_person_cnt,max_true_person_cnt",true_person_cnt,max_true_person_cnt,is_ok)

print(max_true_person_cnt)
        
