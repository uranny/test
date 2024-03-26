list = []
n = int(input())
a = input().split()
for i in range(24):
    list.append(0)
for i in range(n):
    list[int(a[i])] += 1
for i in range(1, len(list)):
    print(list[i], end=' ')