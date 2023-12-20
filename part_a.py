#question1

def total_number_of_combinations(dice_a,dice_b):
    ct=0
    for i in dice_a:
        for j in dice_b:
            ct+=1
    return ct

dice_a=[1,2,3,4,5,6]
dice_b=[1,2,3,4,5,6]
total=total_number_of_combinations(dice_a,dice_b)
print("Total number of Possible Combinations are:",end="")
print(total)

print()
#question2


def total_combinations(dice_a, dice_b):
    total=[[] for i in range(6)]
    current=[]
    for i in dice_a:
        for j in dice_b:
            current=[i,j]
            total[i-1].append(current)
            current=[]
    return total


total=total_combinations(dice_a, dice_b)

print("Total Possible Combinations are:")
for i in total:
    for j in i:
        print(j,end=" ")
    print()

print()

#question3


def total_combinations1(dice_a, dice_b):
    total=[[] for i in range(6)]
    current=[]
    for i in dice_a:
        for j in dice_b:
            current=[i,j]
            total[i-1].append(current)
            current=[]
    return total


total=total_combinations1(dice_a, dice_b)

psum=[]
psum=[0]*12
for i in  total:
    for j in i:
        temp=sum(j)
        psum[temp-1]=psum[temp-1]+1
for i in range(1,len(psum)):
    print("probability sum of " + str(i+1) + " is " + str(psum[i]) + "/36")

print()

