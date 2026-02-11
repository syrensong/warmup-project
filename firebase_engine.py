import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate("../warmup-project-ea50f-firebase-adminsdk-fbsvc-81f9c5d810.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()


class City:
    # Initializes the fields for our collections
    def __init__(self, name, state, population=0, wage=0, area=0, density=0, rank=0, big_city=False):
        self.area = area
        self.big_city = big_city
        self.density = density
        self.wage = wage
        self.name = name
        self.population = population
        self.rank = rank
        self.state = state

    # Turns the document into a python dictionary where we can access data
    def to_dict(self):
        return {
            'name': self.name,
            'state': self.state,
            'rank': self.rank,
            'population': self.population,
            'wage': self.wage,
            'area': self.area,
            'density': self.density,
            'big_city': self.big_city
        }
        

    def __repr__(self):
        return f"City(\
                name={self.name}, \
                state={self.state}, \
                rank={self.rank},\
                population={self.population}, \
                wage={self.wage}, \
                area={self.area},\
                density={self.density},\
                big_city={self.big_city},\
            )"

# Returns the names of all cities in our document
def getCityByName(city_name):
    docs = db.collection("Cities").where("name", "==", city_name).limit(1).stream()
    for doc in docs:
        return doc.to_dict()
    return None


# City Queries
# Returns population of a given city
def getCityPopulation(city):
    docs = db.collection("Cities").where("name", "==", city).stream()
    for doc in docs:
        data = doc.to_dict()
        return data["population"]
    return None

# Returns the state of a given city
def getStateByCity(city):
    docs = db.collection("Cities").where("name", "==", city).stream()
    for doc in docs:
        data = doc.to_dict()
        return data["state"]
    return None

# Returns all cities in a given state
def getCityByState(state_name):
    docs = db.collection("Cities").where("state", "==", state_name).stream()
    return_list = []
    for doc in docs:
        return_list.append(doc.to_dict())
    if return_list == []:
        return None
    else:
        return return_list

# Returns the area of a given city
def getCityArea(city):
    docs = db.collection("Cities").where("name", "==", city).stream()
    for doc in docs:
        data = doc.to_dict()
        return data["area"]
    return None

# Returns the rank of a given city
def getCityRank(city):
    docs = db.collection("Cities").where("name", "==", city).stream()
    for doc in docs:
        data = doc.to_dict()
        return data["rank"]
    return None

# Returns whether or not a city is big using the city name
def isCityBig(city):
    docs = db.collection("Cities").where("name", "==", city).stream()
    for doc in docs:
        data = doc.to_dict()
        return data
    return None

# Number Queries
# Returns cities with a wage which fits the expression provided, 
# ex. getCityByPopulation(>, 1000000) would return all cities with a population greater than 1 million
def getCityByPopulation(operator, value):
    docs = db.collection("Cities").where("population", operator, value).stream()
    return_list = []
    for doc in docs:
        return_list.append(doc.to_dict())
    if return_list == []:
        return None
    else:
        return return_list

# Returns cities with a wage which fits the expression provided, 
# ex. getCityByWage(>=, 20) would return any cities with a living wage greater than or equal to 20 dollars
def getCityByWage(operator, value):
    docs = db.collection("Cities").where("wage", operator, value).stream()
    return_list = []
    for doc in docs:
        return_list.append(doc.to_dict())
    if return_list == []:
        return None
    else:
        return return_list

# Returns cities with an area which fits the expression provided, 
# ex. getCityByArea(<=, 10000) would return any cities with an area less than or equal to 10000 sq. miles
def getCityByArea(operator, value):
    docs = db.collection("Cities").where("area", operator, value).stream()
    return_list = []
    for doc in docs:
        return_list.append(doc.to_dict())
    if return_list == []:
        return None
    else:
        return return_list
    
# Returns cities with a rank which fits the expression provided, 
# ex. getCityByRank(<=, 10) would return the top ten cities with the largest population
def getCityByRank(operator, value):
    docs = db.collection("Cities").where("rank", operator, value).stream()
    return_list = []
    for doc in docs:
        return_list.append(doc.to_dict())
    if return_list == []:
        return None
    else:
        return return_list

# Returns all cities in the collection
def getAllCities():
    docs = db.collection("Cities")
    for doc in docs:
        return doc.to_dict()
    return None
