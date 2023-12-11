import pandas as pd

user = '/home/tspl/Documents/Script_baz_lol/userA.csv'
csv = '/home/tspl/Documents/Script_baz_lol/dataxp.csv'
use = pd.read_csv(user)
cs=pd.read_csv(csv)
i=0
cs["wd_id"]="id"
for index, row in cs.iterrows():
    da=row["WD Name"]
    print("kuchHUA")
    for i,j in use.iterrows():
        daa=j["first_name"]
        if(str(daa)==str(da)):
            row["wd_id"]=j["user_id"]

print("AAAAAAAAAAAAAAAAAAA")
cs.to_csv('aaaaaaaabhijeet.csv', index=False)
print("ASSSSSSSSSSSSSSSSSSSS")
