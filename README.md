# lab_script

## a Script requests Data from Lab Database and deploys it to SDE GeoDataBase.

## the purpose is to update 2 layers tables with the lab analysis values in both intake and output water treated.
## .env file has username, passord, API Endpoint and Datbase(.gdb) path.
## appending the response after slicing it to two different Dictionaries according to the Intke nd output water lab anaalysis values.
## starting Edit sessions for both featurelasses input and output using UpdateCursor to deploy the Data in to the ttribute Table.
## The goal of the project is to scheadual the script so that the data will be changed automatially and synced in the DashBoard created on Arcgis Portal.
