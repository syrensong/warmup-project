import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
# Laylas path: /Users/laylamusallam/Downloads/CS3050/warmup-project-ea50f-firebase-adminsdk-fbsvc-29b43b0a28
# Varuns path: C:/Users/varun/CS_3050/warmup-project-ea50f-firebase-adminsdk-fbsvc-81f9c5d810.json
cred = credentials.Certificate("../warmup-project-ea50f-firebase-adminsdk-fbsvc-81f9c5d810.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

try:
    # Check if Firebase is already initialized
    app = firebase_admin.get_app()
except ValueError:
    # If not initialized, initialize it
    cred = credentials.Certificate("C:/Users/varun/CS_3050/warmup-project-ea50f-firebase-adminsdk-fbsvc-81f9c5d810.json")
    app = firebase_admin.initialize_app(cred)

db = firestore.client()

class City:
    def __init__(self, name, state, population=0, living_wage=0, area=0, density=0, rank=0, big_city=False):
        self.area = area
        self.big_city = big_city
        self.density = density
        self.living_wage = living_wage
        self.name = name
        self.population = population
        self.rank = rank
        self.state = state

    def to_dict(self):
        return {
            'name': self.name,
            'state': self.state,
            'rank': self.rank,
            'population': self.population,
            'living_wage': self.living_wage,
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
                living_wage={self.living_wage}, \
                area={self.area},\
                density={self.density},\
                big_city={self.big_city},\
            )"

docs = db.collection("cities").stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

def get_city_by_name(city_name):
    docs = db.collection("Cities").where("name", "==", city_name).limit(1).stream()
    for doc in docs:
        return doc.to_dict()
    return None

#get cities by state(state name) returns all cities in state
def get_city_by_state(state_name):
    docs = db.collection("Cities").where("state", "==", state_name).stream()
    for doc in docs:
        return doc.to_dict()
    return None
#get cities by population(operator, value) for example population > 10000 would be get cities by population(>, 10000)
def get_city_by_population(operator, value):
    docs = db.collection("Cities").where("population", operator, value).stream()
    for doc in docs:
        return doc.to_dict()
    return None
#get cities by wage(operator, value)
def get_city_by_wage(operator, value):
    docs = db.collection("Cities").where("wage", operator, value).stream()
    for doc in docs:
        return doc.to_dict()
    return None
#get cities by area(operator, value)
def get_city_by_area(operator, value):
    docs = db.collection("Cities").where("area", operator, value).stream()
    return_list = []
    for doc in docs:
        return_list.append(doc.to_dict())
        print(f"Found city: {doc}") 
    if return_list == []:
        return None
    else:
        return return_list
#get cities by rank(operator, value)
def get_city_by_rank(operator, value):
    docs = db.collection("Cities").where("rank", operator, value).stream()
    for doc in docs:
        return doc.to_dict()
    return None
#get all cities()
def get_all_cities():
    docs = db.collection("Cities")
    for doc in docs:
        return doc.to_dict()
    return None


print(get_city_by_area(">", 1000))