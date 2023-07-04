import pandas as pd
df = pd.read_excel(io='dataupdate.xlsx', sheet_name='weather').set_index('Day')
print(df.loc[(df.Event.str.contains('แดดร้อน')) | (df.Temperature>25)])