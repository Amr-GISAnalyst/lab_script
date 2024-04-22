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
today = date.today()

# setting env variables for AUTH to use it safely.
#--------------------------------------------------
USER_NAME = os.getenv("USER")
PASSWORD = os.getenv("PASS")
URL = os.getenv("URI")

lab = "11"

#API Request.
#-------------
response = requests.get(url=f"{URL}/{lab}/{today}", auth=(USER_NAME, PASSWORD))
response.raise_for_status()

data = response.json()
print(len(data))
print(data)
