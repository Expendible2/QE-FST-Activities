import pandas as pd
data={"firstname":["Satvik", "Avinash","Lahri"],
      "lastname":["Shah", "Kati","Rath"],
      "email":["satshah@ex.com","avinashk@ex.com","lahrirath@ex.com"],
      "phonenumber":[1234567890,2468135790,1324567890]}
d=pd.DataFrame(data)
d.to_excel("Act19.xlsx")