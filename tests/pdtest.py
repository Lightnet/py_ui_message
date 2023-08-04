import os
import pandas as pd

filepath = "raw_data.csv"
#tests
if not os.path.exists(filepath):
  #create it
  print("NOT FOUND DATA")
  mydataset = {
  'name': [],
  'passphrase': [],
  'email': []
  }
  df = pd.DataFrame(mydataset)
  print(df)
  df.to_csv('raw_data.csv', index=False)
  #pass
else:
  df = pd.read_csv('raw_data.csv')
  print(df)
  # Add Row to DataFrame
  #list_row = ['Test', 'Test', 'test@test.test']
  #df.loc[len(df)] = list_row

  #print(df.loc)

  # Insert Dict to the dataframe using DataFrame.append()
  #new_row = {'name':'Test', 'passphrase':'hello', 'email':'test@test.test'}
  #df = df._append(new_row, ignore_index=True)

  df.to_csv('raw_data.csv', index=False)
  print("FOUND DATA")