#--------------------------------------------------------------------------------------------------
# Purpose            : This is a simulation of a deadly circle -
#                      100 people stand in a circle. Number 1 has a sword. He kills the next
#                      person (i.e. Nunber 2) and gives the sword to the next living person 
#                      (i.e. Number 3). Everyone does the same until only 1 survives. Who 
#                      survives? What if the circle was 150 people, or 273 people?
# Date Created       : 17Nov2022
# Author             : A.S.Harrison
# Amendment History  : Date         Author          Description
#                      17Nov2022    A.S.Harrison    Created
#--------------------------------------------------------------------------------------------------

CIRCLE_SIZE = int(100)                                                  # How many people are in the circle?
ALIVE = int(0)                                                          # Value of a living person
DEAD = int(1)                                                           # Value of a dead person
Circle = [0] * CIRCLE_SIZE                                              # Make Space for each person

# Find the next person of a particular state (dead or alive) --------------------------------------
def NextPerson(intState: int, intStart: int):                           
    intCurrent = intStart                                               # Starting from the specifed person
    while True:
        if intCurrent > CIRCLE_SIZE - 1: intCurrent = 0                 # If we go off the end, go back to the beginning
        if Circle[intCurrent] == intState: break                        # If we have found a person of the desired state (dead or alive) then break out of the loop
        intCurrent += 1                                                 # Otherwise, move on to the next person
    return intCurrent


# Initial conditions - everyone is alive so number 0 will have the knife and kill number 1 -------
intKnife = int(0)                                                       # Person 0 has the knife
intVictim = int(1)                                                      # Person 1 is the first victim
Circle[intVictim] = DEAD                                                # Kill the first victim

while True:                                                             # Start an infinite loop (we'll break when there's only one person left)
    intKnife = NextPerson(ALIVE, intVictim + 1)                         # The knife is passed to the next alive person
    intVictim = NextPerson(ALIVE, intKnife + 1)                         # Who's going to kill the next alive person
    if intKnife == intVictim: break                                     # If they're the same person then he's the last man standing
    Circle[intVictim] = DEAD                                            # Kill the victim

print("Survivor = " + str(intKnife + 1))                                # Display the result (+1 because the simulation is zero-based)

