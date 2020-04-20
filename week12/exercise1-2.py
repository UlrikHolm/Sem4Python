import pandas as pd
import pymysql
from sqlalchemy import create_engine
import re

#Download data fra linket og gem det i en dataframe 
#og gem det i en mysql database
def first():

#Lav en funktion der returnerer en dict med minimum følgende data:
#- Find antallet af crimes mellem to givne datoer i 2006 (givet som parameter til funktionen)
#- Find den totale mængde af "burglary" i januar