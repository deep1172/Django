class Database:
    def connect(self):
        return "Connected to Database"
    
class Service:
    def __init__(self, db:Database):
        self.db = db  # loosly coupled

    def get_data(self ):
        return self.db.connect() 

# Usage 
db = Database()
# db_staging = DatabaseStaging()
service = Service()
print(Service.get_data())