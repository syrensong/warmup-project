import pyparsing as pp
import firebase_engine as fe
from pyparsing import Word, Literal, Combine, Group, Optional
import shlex
import warnings
warnings.filterwarnings("ignore", message="Detected filter using positional arguments.")
from tabulate import tabulate

query_keywords = pp.oneOf("POPULATION WHERE WAGE STATE AREA RANK BIG")
operators = pp.oneOf("< > == <= >=")
and_function = pp.Literal("AND")
or_function = pp.Literal("OR")
help_function = pp.Literal("HELP")

expression = query_keywords + operators  + query_keywords

#Base query function that calls specific functions based on the given input
def doQuery (column, city="none", operand="none", quantity=0, detail="none"):
    if column == "HELP":
        getHelp()
        return
    
    if quantity != 0:
        if column == "POPULATION":
            doNumPopulationQuery(operand, quantity, detail)
        elif column == "WAGE":
            doNumWageQuery(operand, quantity, detail)
        elif column == "AREA":
            doNumAreaQuery(operand, quantity, detail)
        elif column == "RANK":
            doNumRankQuery(operand, quantity, detail)
        return
    
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
        return
    
    print("Invalid Query Message")

#City Queries
#Returns the population of the given city
def doCityPopulationQuery(city):
    city_data = fe.getCityPopulation(city)
    if city_data:
        print(f"The population of {city} is {city_data}")
    else:
        print(f"City '{city}' not found")
        
#Returns the state of the given city
def doCityWhereQuery(city):
    city_data = fe.getStateByCity(city)
    
    if city_data:
        print(f"{city} is in {city_data}")
    else:
        print(f"City '{city}' not found")

#Returns all the cities in the given state
def doCityStateQuery(state):
    city_data = fe.getCityByState(state)

    if city_data:
        print(f"The cities in {state} are:")
        for city in city_data:
            print(f" - {city['name']}")
    else:
        print(f"State '{state}' not found")

#Returns the area of the given city
def doCityAreaQuery(city):
    city_data = fe.getCityArea(city)
    if city_data:
        print(f"The area of {city} is {city_data}")
    else:
        print(f"Area of '{city}' not found")

#Returns the rank of a given city
def doCityRankQuery(city):
    city_data = fe.getCityRank(city)
    if city_data:
        print(f"{city} is ranked number {city_data}")
    else:
        print(f"Rank of {city} is not found")

#Returns whether or not a city is considered a big city
def doCityBigQuery(city):
    city_data = fe.isCityBig(city)
    if "big city" in city_data:
        print(f"'{city}' is a big city")
    else:
        print(f"'{city}' is not a big city")

#Number Queries
#Returns the cities whose population is <=> the given quantity
def doNumPopulationQuery(operand, quantity, detail):
    #return city
    city_data = fe.getCityByPopulation(operand, quantity)
    if detail == "none":
        if city_data:
            for data in city_data:
                print(f"{data['name']}")
        else:
            print(f"Cities not found")
    else:
        if city_data:
            table = tabulate(city_data, headers="keys")
            print(table)
        else:
            print(f"City '{city}' not found")

#Returns the cities whose wage is <=> the given quantity
def doNumWageQuery(operand, quantity, detail):
    city_data = fe.getCityByWage(operand, quantity)
    if detail == "none":
        if city_data:
            for data in city_data:
                print(f"{data['name']}")
        else:
            print(f"Cities not found")
    else:
        if city_data:
            table = tabulate(city_data, headers="keys")
            print(table)
        else:
            print(f"City '{city}' not found")

#Returns the cities whose area is <=> the given quantity
def doNumAreaQuery(operand, quantity, detail):
    city_data = fe.getCityByArea(operand, quantity)
    if detail == "none":
        if city_data:
            for data in city_data:
                print(f"{data['name']}")
        else:
            print(f"Cities not found")
    else:
        if city_data:
            table = tabulate(city_data, headers="keys")
            print(table)
        else:
            print(f"City '{city}' not found")

#Returns the cities whose rank is <=> the given quantity
def doNumRankQuery(operand, quantity, detail):
    city_data = fe.getCityByRank(operand, quantity)
    if detail == "none":
        if city_data:
            for data in city_data:
                print(f"{data['name']}")
        else:
            print(f"Cities not found")
    else:
        if city_data:
            table = tabulate(city_data, headers="keys")
            print(table)
        else:
            print(f"City '{city}' not found")

#Prints the options for possible queries
def getHelp():
    print("City Commands\n"
            "\tWHERE “City”: returns the state the chosen city is in\n"
            "\tPOPULATION “City”: returns the population of the chosen city\n"
            "\tSTATE “State”: returns a list of all the cities in the chosen state\n"
            "\tAREA “City”: returns the area of the chosen city\n"
            "\tRANK “City”: returns the rank of the chosen city\n"
            "\tBIG “City”: returns if the chosen city is big\n"
        "Number Commands: <, <=, =, >=, >\n"
            "\tPOPULATION <=> #: returns cities with a population <=> the given number\n"
            "\tWAGE <=> #: returns cities with a living wage <=> the given number\n"
            "\tAREA <=> #: returns cities with an area <=> the given number\n"
            "\tRANK <=> #: returns cities with a rank <=> the given number\n"
        "Detail: added to the end of a number query to return a table of the returned cites"
        "Exit: ends the program"
            )

if __name__ == '__main__':
    print("Please choose your command between WHERE, POPULATION, WAGE, STATE, AREA, RANK, BIG, NUMBER, HELP:")
    run = True
    while run:
        user_input = input("$$ ").strip()
        parts = shlex.split(user_input)
        print(parts)
        column = parts[0].upper()
        city = "none"
        operator = "none"
        quantity = 0
        detail = "none"
        if column == "EXIT":
            run = False
            break
        elif column == "HELP":
            doQuery(column, city, operator, quantity, detail)
        elif parts[1] in {"<", ">", "<=", ">=", "="}:
            operator = parts[1]
            quantity = int(parts[2])
            if len(parts) > 3 and parts[3] in {"detail"}:
                detail = parts[3]
            doQuery(column, city, operator, quantity, detail)
        else:
            city = parts[1]
            if len(parts) > 2 and parts[2] in {"detail"}:
                detail = parts[2]
            doQuery(column, city, operator, quantity, detail)
        