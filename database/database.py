import sqlite3
from pathlib import Path

#Finds root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

#Stores the database inside the data directory
DATABASE_PATH = PROJECT_ROOT / "data" / "campaign.db"

#Creates a connection to the campaign database
def get_connection():
    #create data folder if it doesn't exist
    DATABASE_PATH.parent.mkdir(
        parents = True,
        exist_ok= True
    )

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection