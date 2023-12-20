def total_combinations(dice_a,dice_b):
    ct=0
    for i in dice_a:
        for j in dice_b:
            ct+=1
    return ct

dice_a=[1,2,3,4,5,6]
dice_b=[1,2,3,4,5,6]
total=total_combinations(dice_a,dice_b)
print("Total Possible Combinations are:",end="")
print(total)
