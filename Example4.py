N = int(input())
list = []
count = 0
for i in range(-N,N+1):
    res = -N+count
    list.append(res)
    count+=1

print(f"Созданный массив равен: {list}")
num = 2
for i in range(0,num):
    temp = list[len(list)-1]   
    j = len(list)-1
    while j > 0:
            list[j] = list[j-1]
            j-=1
    list[0] = temp
    count-=1
print(f"Смещённый массив равен: {list}")

