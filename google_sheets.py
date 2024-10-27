import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='{C:\Users\andy8\Downloads\serious-unison-439914-c7-695430c44d35.json}')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['tao1', 'tao2', 'tao3', "tao4"]
df['age'] = [11, 12, 13, 14]

#open the google spreadsheet 
sh = gc.open('{123}')

#select the first worksheet 
wks = sh[0]  

#update the first worksheet with df, starting at cell A1 i.e.(0,0) 
wks.set_dataframe(df,(0,0))
