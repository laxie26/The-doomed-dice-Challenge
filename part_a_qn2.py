def total_combinations(dice_a, dice_b):
    total=[[] for i in range(6)]
    current=[]
    for i in dice_a:
        for j in dice_b:
            current=[i,j]
            total[i-1].append(current)
            current=[]
    return total

dice_a=[1, 2, 3, 4, 5, 6]
dice_b=[1, 2, 3, 4, 5, 6]
total=total_combinations(dice_a, dice_b)

print("Total Possible Combinations are:")
for i in total:
    for j in i:
        print(j,end=" ")
    print()
