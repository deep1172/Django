class Database:
    def connect(self):
        return "Connect to Database"
    
class Service:
    def __init__(self):
        self.db = Database()  # tightly coupled

    def get_data(self):
        return self.db.connect() 

# Usage 

service = Service()
print(Service.get_data())