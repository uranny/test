n = int(input(), 16)
i = 1
for i in range(1, 16):
    print('%X*%X=%X'%(n, i, (n*i)))
    i += 1