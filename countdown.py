daysUntilElection = input("How many days until the Election? ")

while int(daysUntilElection) >  0:
    if daysUntilElection == 1:
        print(str(daysUntilElection) + " more day until the Election!")
        daysUntilElection = int(daysUntilElection) - 1
    else:
        print(str(daysUntilElection) + " more days until the Election!")
        daysUntilElection = int(daysUntilElection) - 1
