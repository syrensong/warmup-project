import pyparsing as pp
from firebase_admin import db
import firebase_engine as fe
from pyparsing import Word, Literal, Combine, Group, Optional
from lark import Lark, Transformer
import shlex




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
    if column == "HELP":
        getHelp()
        return
    
    if quantity != 0:
        if column == "POPULATION":
            doNumPopulationQuery(operand, quantity)
        elif column == "WAGE":
            doNumWageQuery(operand, quantity)
        elif column == "AREA":
            doNumAreaQuery(operand, quantity)
        elif column == "RANK":
            doNumRankQuery(operand, quantity)
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

#Works
def doCityPopulationQuery(city):
    city_data = fe.getCityPopulation(city)
    
    if city_data:
        print(f"The population of {city} is {city_data}")
    else:
        print(f"City '{city}' not found")

#Works
def doCityWhereQuery(city):
    city_data = fe.getStateByCity(city)
    
    if city_data:
        print(f"{city} is in {city_data}")
    else:
        print(f"City '{city}' not found")

#Works
def doCityStateQuery(state):
    city_list = fe.get_city_by_state(state)

    if city_list:
        print(f"The cities in {state} are:")
        for city in city_list:
            print(f" - {city['name']}")
    else:
        print(f"State '{state}' not found")

def doCityAreaQuery(city):
    return city

def doCityRankQuery(city):
    return city

def doCityBigQuery(city):
    return city

#THIS ONE doesn't WORK!
def doNumPopulationQuery(operand, quantity):
    #return city
    city_data = fe.get_city_by_population(operand, quantity)
    if city_data:
        for data in city_data:
            print(f"{data['name']}")
    else:
        print(f"City not found")

def doNumWageQuery(operand, quantity):
    return quantity

#Works
def doNumAreaQuery(operand, quantity):
    #return city
    city_data = fe.get_city_by_area(operand, quantity)
    if city_data:
        for data in city_data:
            print(f"{data['name']}")
    else:
        print(f"City '{city}' not found")

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
            "\tAREA <=> #: returns cities with an area >,<,= the given number\n"
            "\tRANK <=> #: returns cities with a rank >,<,= the given number\n"
            )

while True:
    print("Please choose your command between WHERE, POPULATION, STATE, AREA, RANK, BIG, NUMBER,HELP: ")
    user_input = input().strip()
    parts = shlex.split(user_input)
    print(parts)
    column = parts[0].upper()
    city = "none"
    operator = "none"
    quantity = 0
    if len(parts) >= 3 and parts[1] in {"<", ">", "<=", ">=", "="}:
        operator = parts[1]
        quantity = int(parts[2])
    elif len(parts) >= 2:
        city = parts[1]
    doQuery(column, city, operator, quantity)
