# getting today's Data in a format looks like ([y]2024-[m]04-[d]01).
import requests
from datetime import date
import os
import arcpy
from dotenv import load_dotenv, dotenv_values
#----------------------------------------------
load_dotenv()
#----------------------------------------------
# setting env variables for AUTH to use it safely.
#---------------------------------------------------------------
USER_NAME = os.getenv("USER")
PASSWORD = os.getenv("PASS")
URL = os.getenv("URI")
DATABASE = os.getenv("GDB") #env variable for DATABASE Connection.
input_fields = []
output_fields = []
#workspace GDB
#----------------
arcpy.env.overwriteOutput = True
arcpy.env.workspace = DATABASE
#------------------------------------------
#listing fields in both featureclasses
#----------------------------------------
input_list = arcpy.ListFields("GIS.APP_Features\\GIS.input")
for field in input_list:
    if field.name == "Shape" or field.name == "OBJECTID" or field.name == "lab_code" or field.name == "wtp_name" or field.name == "GlobalID":
        pass
    else:
       input_fields.append(field.name)

output_list = arcpy.ListFields("GIS.APP_Features\\GIS.output")
for field in output_list:
    if field.name == "Shape" or field.name == "OBJECTID" or field.name == "lab_code" or field.name == "wtp_name" or field.name == "GlobalID":
        pass
    else:
       output_fields.append(field.name)
#-----------------------------------------------------------------------
#setting up Today's Date
#----------------------
today = date.today()
#---------------------------------------------------------------
lab = ["1", "7", "8", "9", "10", "11", "12", "13", "14", "15"] #Lab Code.
input_data = {"1":[],"7":[],"8":[],"9":[],"10":[],"11":[],"12":[],"13":[],"14":[],"15":[]} #input values list.
output_data = {"1":[],"7":[],"8":[],"9":[],"10":[],"11":[],"12":[],"13":[],"14":[],"15":[]} #output values list.
#API Request.
#-------------
for labvalue in lab:
    data_list = [] #adding the response.json to a list.
    response = requests.get(url=f"{URL}/{labvalue}/{today}", auth=(USER_NAME, PASSWORD))
    response.raise_for_status()
    data = response.json() 
    for i in data: #adding the response.json to a list.
        data_list.append(i)
#-----------------------------------------------------------------------------------
# Slicing Data.json to input and output according to the Element Order.
#----------------------------------------------------------------------------            
    for x in input_data:
        if x == labvalue:
            input_data[x] = data_list[0:8:1]
    for i in output_data:
        if i == labvalue:
            output_data[i] = data_list[8:15:1]
#-------------------------------------------------------------------------------------------------------------------------
#start edit session for input fetureclass adding lab values.
#-------------------------------------------------------------------
edit = arcpy.da.Editor(DATABASE)
edit.startEditing(with_undo=False, multiuser_mode=True)
edit.startOperation()
for code in lab: #Adding Data to the intake featureclass from data_list.json to the fields according to Lab Code.
    with arcpy.da.UpdateCursor("GIS.APP_Features\\GIS.input",input_fields,f"lab_code = {code}") as input_rows:
            for row in input_rows:
                    for i in range(len(input_fields)):
                        if input_data[code][i] is None:
                            row[i] = None #continue
                            input_rows.updateRow(row) 
                        else:
                            row[i] = input_data[code][i]
                    input_rows.updateRow(row)
edit.stopOperation()
edit.stopEditing(save_changes=True)
#----------------------------------------------------------------------------------------------------------------------------
#start edit session for output fetureclass adding lab values.
#-------------------------------------------------------------------
edit = arcpy.da.Editor(DATABASE)
edit.startEditing(with_undo=False, multiuser_mode=True)
edit.startOperation()
for code in lab: #Adding Data to the output featureclass from data_list.json to the fields according to Lab Code.
    with arcpy.da.UpdateCursor("GIS.APP_Features\\GIS.output",output_fields,f"lab_code = {code}") as output_rows:
            for row in output_rows:
                    for i in range(len(output_fields)): 
                        if output_data[code][i] is None:
                            row[i] = None #continue
                            output_rows.updateRow(row)
                        else:
                            row[i] = output_data[code][i]
                    output_rows.updateRow(row)
edit.stopOperation()
edit.stopEditing(save_changes=True)
print("Operation Done Successfuly")
