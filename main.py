# getting today's Data in a format looks like ([y]2024-[m]04-[d]01).
import requests
from datetime import date
import os
import arcpy
from dotenv import load_dotenv, dotenv_values
#----------------------------------------------
load_dotenv()
#----------------------------------------------
#workspace GDB
#----------------
input_fields = []
output_fields = []
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "E:\\python\\Lab_Project\\lab_script.gdb"
input_layer = "E:\\python\\Lab_Project\\lab_script.gdb\\input"
output_layer = "E:\\python\\Lab_Project\\lab_script.gdb\\output"

#listing fields in both featureclasses
#----------------------------------------
input_list = arcpy.ListFields("input")
for field in input_list:
    if field.name == "Shape" or field.name == "OBJECTID":
        pass
    else:
       input_fields.append(field.name)

output_list = arcpy.ListFields("output")
for field in output_list:
    if field.name == "Shape" or field.name == "OBJECTID":
        pass
    else:
       output_fields.append(field.name)

#getting Today's Date
#----------------------
today = date.today()

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
    # index = 0
    # row_col = 0
    # with arcpy.da.UpdateCursor(input_layer, input_fields) as input_update:
    #     for row in input_update:
    #         if index > 7:
    #             row_col += 1
    #             if row_col > 10:
    #                 break
    #         elif data[index] is None:
    #             index += 1
    #         else:
    #             row[row_col] = data[index]
    #             input_update.updateRow(row)
    #             index += 1

    print(len(data))
    print(f" station {x}'s Data is: {data}")
