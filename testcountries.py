
def replacewords(array):

    house=[flat,apartment,]
    with open("countries.txt") as f:
        content = f.readlines()
        content = [x.strip() and x.split() for x in content]


        for index, i in enumerate(array):
            if i == "COUNTRY":
                 for country in content:
                     input[index]=country
                     print "SEND THIS TO FURTHER ANALYSIS"

        for index, i in enumerate(array):
            if i == "HOUSE":
                 for house in house:
                     input[index]=house
                     print "SEND THIS TO FURTHER ANALYSIS"

