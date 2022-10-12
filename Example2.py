print(f"x|y|z|¬(X∧Y)vZ")
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            result = not(x & y) or z
            print(f"{x}|{y}|{z}|{int(result)}")