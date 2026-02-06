
def main():
    print("$$")
    getHelp()

def doQuery (column, city="none", operand="none", quantity=0): 
    if city != "none":
        if column == "POPULATION":
            doCityPopulationQuery(city)
        elif column == "WHERE":
            doCityWhereQuery(city)
        elif column == "STATE":
            doCityStateQuery(city)
        elif column == "AREA":
            doCityAreaQuery(city)
        elif column == "RANK":
            doCityRankQuery(city)
        elif column == "BIG":
            doCityBigQuery(city)
    elif quantity != 0:
        if column == "POPULATION":
            doNumPopulationQuery(operand, quantity)
        elif column == "WAGE":
            doNumWageQuery(operand, quantity)
        elif column == "AREA":
            doNumAreaQuery(operand, quantity)
        elif column == "RANK":
            doNumRankQuery(operand, quantity)
    elif column == "HELP":
        getHelp()
    else:
        print("Invalid Query Message")

def doCityPopulationQuery(city):
    return city

def doCityWhereQuery(city):
    return city

def doCityStateQuery(city):
    return city

def doCityAreaQuery(city):
    return city

def doCityRankQuery(city):
    return city

def doCityBigQuery(city):
    return city

def doNumPopulationQuery(operand, quantity):
    return quantity

def doNumWageQuery(operand, quantity):
    return quantity

def doNumAreaQuery(operand, quantity):
    return quantity

def doNumRankQuery(operand, quantity):
    return quantity

def getHelp():
    print("City Commands\n"
            "\tWHERE “City”: returns the state the chosen city is in\n"
            "\tPOPULATION “City”: returns the population of the chosen city\n"
            "\tSTATE “State”: returns a list of all the cities in the chosen state\n"
            "\tAREA “City”: returns the area of the chosen city\n"
            "\tRANK “City”: returns the rank of the chosen city\n"
            "\tBIG “City”: returns if the chosen city is big\n"
        "Number Commands: <, <=, =, >=, >\n"
            "\tPOPULATION >, <, = #: returns cities with a population >,<,= the given number\n"
            "\tWAGE >, <, = #: returns cities with a living wage >,<,= the given number\n"
            "\tAREA >, <, = #: returns cities with an area >,<,= the given number\n"
            "\tRANK >, <, = #: returns cities with a rank >,<,= the given number\n"
            )

main()