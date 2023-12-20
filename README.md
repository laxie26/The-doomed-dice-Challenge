                                           THE DOOMED DICE CHALLENGE
                                                   PART-A
  PROBLEM STATEMENT:
               You have two dice- dice_a and dice_b.You need to find the total number of combinations possible.You also need to find the distribution of all combinations.Also you need to find the probabilities of each sum out of all combinations.

  SOLUTION:
  
   1)You need to use two for loops(one nested inside the other),one for generating values of dice_a and the other for generating the values of dice_b for each value in dice_a.A count variable should be declared that counts the total possibilities i.e., 36
   
   2)Here,you need to use two for loops in the same way as the previous step and have a current list that stores a combination temporarily.Another 2D list(total) that stores all the combination is declared and the current list should be appended to the total list.Print the total list using 2 for loops.
   
   3)Using the 2D list generated in the step 2,we now have the list called total.Using two for loops,take each combination,generate its sum.Declare another list called psum.Initialize 12 zeroes.Each time,we generate a sum,store in a temporary variable called temp and increment the (temp-1)th index of psum.
   
   4)Print the probabilities of each sum by dividing it by 36 which is the total number of combinations.

Below is the output of part A problem statement
![output_screenshot1](https://github.com/laxie26/The-doomed-dice-Challenge/assets/143947051/795ebc42-61a6-4c84-adea-e8cec2131280)

                                                 PART-B
PROBLEM STATEMENT:
                 Loki dooms your dice for his fun removing all the “Spots” off the dice.You have the tools to re-attach the “Spots” back on the Dice.
 However, Loki has doomed your dice with the following conditions:
 Die A cannot have more than 4 Spots on a face.
 Die A may have multiple faces with the same number of spots.
 Die B can have as many spots on a face as necessary i.e. even more than 6.
 But in order to play your game, the probability of obtaining the Sums must remain the
 same!
 
 SOLUTION:
 1)Let us analyze the problem well.Let's understand the criteria for each dice.
 
 2)For dice_a,we need to generate a list such that it has numbers only from 1-4 and can have multiple numbers on it(repetition of numbers is allowed).
 
 3)So we need to define a function that can generate combinations of elements with repetition.So,we create a function dice_a_combo and we generate all possible lists of length 6 using backtracking.The elements [1,2,3,4] are passed as input.
 
 4)Now,let's look at dice_b.It can have faces whose number of spots can be greater than 6 also.
 
 5)We declare a function called dice_b_combo which generates lists of length 6 without repetition because they haven't mentioned any repetition for dice_b.The elements are[1,2,3,4,5,6,7,8] because the highest number in dice_a is 4.To obtain 12 we need 8 to be the highest number in dice_b.
 
 6)This backtracking function generates lists that satisfy the criteria for dice_b.
 
 7)Declare a function transform that takes dice_a and dice_b as input.Here dice_a and dice_b are old dice values.The values for dice_a=dice_b=[1,2,3,4,5,6]
 
 8)We need to print the values of new_die_a and new_die_b
 
 9)The output for dice_a_combo is stored in combo1 and the output of dice_b_combo is stored in combo2.Hence,the two variables combo1 and combo2 stores the possible lists of dice_a and dice_b respectively.
 
 10)psum stores the probabilities of sum of all distribution of old dice_a and old_dice_b.
 
 11)Using two for loops,we take each pair of lists(one from combo1 and other from combo2) and generate the probability of sums out of all distributions using a functon called probsum.If the output of prob sum is equal to psum,then the two lists are the compatible values for new_die_a and new_die_b.
 
 12)The function probsum takes two lists,generates sum of all possible distributions and finds the probability of sums of all distributions.It returns the probability sum to the transform function which checks it with the psum which is the probability sum of old dice.
 
 13)Once the compatible lists are found,they are printed.
 

Below is the output for part B problem statement
![output_screenshot](https://github.com/laxie26/The-doomed-dice-Challenge/assets/143947051/975da7e5-23d6-4660-b175-c2c5a34ed5f7)
