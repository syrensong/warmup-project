import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
# Laylas path: /Users/laylamusallam/Downloads/CS3050/warmup-project-ea50f-firebase-adminsdk-fbsvc-29b43b0a28

cred = credentials.Certificate('path.json')
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

    @staticmethod
    def to_dict(self):
        

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