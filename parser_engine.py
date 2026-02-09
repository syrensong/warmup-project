import pyparsing as pp
from firebase_admin import db
import firebase_engine as fe
from pyparsing import Word, Literal, Combine, Group, Optional
from lark import Lark, Transformer




query_keywords = pp.oneOf("POPULATION WHERE WAGE STATE AREA RANK BIG")
operators = pp.oneOf("< > <= =>")
#operator = Literal("<") | Literal(">") | Literal("<=") | Literal("=>")|Literal("AND")|Literal("OR")|Literal("HELP")
and_function = pp.Literal("AND")
or_function = pp.Literal("OR")
help_function = pp.Literal("HELP")

expression = query_keywords + operators  + query_keywords
print (expression)



def main():
    print("$$")
    print(fe.get_city_by_name("New York"))
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

def doCityPopulationQuery(operator, value):
    #return city
    city_data = fe.get_city_by_population(operator, value)
    if city_data:
        for data in city_data:
            print(f"{data['name']}")
    else:
        print(f"City '{city}' not found")

def doCityWhereQuery(city):
    return city

def doCityStateQuery(city):
    return city

def doCityAreaQuery(operator, value):
    #return city
    city_data = fe.get_city_by_area(operator, value)
    if city_data:
        for data in city_data:
            print(f"{data['name']}")
    else:
        print(f"City '{city}' not found")

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
            "\tPOPULATION <=> #: returns cities with a population >,<,= the given number\n"
            "\tWAGE <=> #: returns cities with a living wage >,<,= the given number\n"
            "\tAREA <="> #: returns cities with an area >,<,= the given number\n"
            "\tRANK <=> #: returns cities with a rank >,<,= the given number\n"
            )
    
doCityAreaQuery(">", 100)

while True:
    user_input = input("Please choose your command between WHERE, POPULATION, STATE, AREA, RANK, BIG, NUMBER,HELP: ")
    column = user_input.split()[0]
    city = "none"
    operator = "none"
    quantity = 0
    if len(user_input) == 2:
        city = user_input.split()[1]
        operator=none, quantity=0
    elif len(user_input) == 3:
        operator = user_input.split()[1]
        num = int(user_input.split()[2])
    doQuery(column, city, operator, num)


main()
