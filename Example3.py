string1 = input()
string2 = input()

for i in range(len(string1)):
    count = 0
    count2 = 1
    for m in range(len(string1)):
        if count2 < len(string1):
            if string2[i] == string1[m]:
                count+=1 
    count2+=1
    print(f"В первой строке буква {string2[i]} встречается {count} раз")
