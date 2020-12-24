import matplotlib.pyplot as plt
import matplotlib
import pandas as pd 


#TODO: Add a column to table that standardizes answers

#Input CSV
df = pd.read_csv('/Users/chrismullins/dev/Public Ethics Comission/User-Satisfaction/PRR User Satisfaction Survey.csv')

departmentCells = []


# for row in df["Which City department responded to your request?"]:
#     if row == 'Fire' or row == 'Fire Department':
#         departmentCells.append('Fire')
#     elif row.indexOf('Police') or row.indexOf('police)'):
#       departmentCells.append('Police')
#     else:
#       departmentCells.append('N/A')

#print(departmentCells)

#Parse through 
df['Departments'] = df.apply(lambda x: 'Fire' if x['Which City department responded to your request?'] in ['Fire','Fire Department'] else 'NULL')



#test


df.describe()

#df.to_csv('/Users/chrismullins/dev/Public Ethics Comission/User-Satisfaction/out.csv')