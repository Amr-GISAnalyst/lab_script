# getting today's Data in a format looks like ([y]2024-[m]04-[d]01).
import requests
from datetime import date
import os
import arcpy
from dotenv import load_dotenv, dotenv_values
#----------------------------------------------
load_dotenv()
#----------------------------------------------
#getting Today's Date
#----------------------
today = "2024-04-22"#date.today()

# setting env variables for AUTH to use it safely.
#--------------------------------------------------
USER_NAME = os.getenv("USER")
PASSWORD = os.getenv("PASS")
URL = os.getenv("URI")

lab = {"nozha": "1",
       "syouf": "7",
       "mamoora": "8",
       "sharqy": "9",
       "mansheya2": "10",
       "mansheya1": "11",
       "fornelgraya": "12",
       "maryout": "13",
       "kilo40": "14",
       "zhour": "15",}

#API Request.
#-------------
for x, y in lab.items():
    response = requests.get(url=f"{URL}/{y}/{today}", auth=(USER_NAME, PASSWORD))
    response.raise_for_status()
    data = response.json()
    print(len(data))
    print(f" station {x}'s Data is: {data}")
