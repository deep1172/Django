from DependencyInjection.dep_one import Database
from fastapi import FastApi, Depends # type: ignore

app = FastApi()

class Database:
    def connect(self):
        return "connected to Database"
    def disconnect(self):
        return "Disconnected from Database"


def get_database():
    # return "Connect to Database"
    db = Database()

    try:
        yield db
    finally:
        db.disconnect()

@app.get("/admin")
def read_data(db= Depends(get_database)):
    return {"message", "Welcome to admin Panel"}
