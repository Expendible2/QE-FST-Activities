import pandas as pd
data={
    "Username":["Admin","Charles","Deku"],
    "Passwords":["Password","Charl13","Allmight"]
}
d=pd.DataFrame(data)
d.to_csv("Act17.csv")
