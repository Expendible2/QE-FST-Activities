import pandas as pd
data=pd.read_excel("Act19.xlsx")
print(f"No of rows {len(data["firstname"])} and No of columns {len(data.columns)-1}")
print("Email Column Data")
print(data["email"])
print("Firstname in Ascending order")
print(data["firstname"].sort_values(ascending=True))