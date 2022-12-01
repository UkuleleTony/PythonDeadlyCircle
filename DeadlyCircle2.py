#--------------------------------------------------------------------------------------------------
# Purpose            : This is a solution to the deadly circle -
#                      100 people stand in a circle. Number 1 has a sword. He kills the next
#                      person (i.e. Number 2) and gives the sword to the next living person 
#                      (i.e. Number 3). Everyone does the same until only 1 survives. Who 
#                      survives? What if the circle was 150 people, or 273 people?
#       
#                      This version of the code came about as a result of discovering a formula
#                      that gives the answer. I used the first version of the code to display
#                      the result of various circle sizes. this gave me -
#
#                               Circle Size    Survivor
#                               2              1
#                               3              3
#                               4              1
#                               5              3
#                               6              5
#                               7              7
#                               8              1
#                               9              3
#                               10             5
#                               11             7
#                               12             9
#                               13             11
#                               14             13
#                               15             15
#                               16             1
#
#                      It turns out that the solution to the deadly circle can be summarised as 
#                           (CircleSize - NearestPowerOf2) * 2 + 1
#                      Where NearestPowerOf2 is the nearest power of 2 that is less than or equal to the circle size
#
#                      This means we can rewrite the simulation with just THREE lines of code
# Date Created       : 01Dec2022
# Author             : A.S.Harrison
# Amendment History  : Date         Author          Description
#                      01Dec2022    A.S.Harrison    Created
#--------------------------------------------------------------------------------------------------

circle, pow = 150, 1                # Initialise the circle size and power of 2 variable
while pow <= circle: pow *= 2       # Find the nearest power of 2 (this will actually find the first one HIGHER than the circle size)
print((circle - (pow / 2)) * 2 + 1) # Calculate the answer (we will have gone one power too far, hence the pow/2)