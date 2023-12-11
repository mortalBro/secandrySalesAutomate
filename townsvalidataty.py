# import pandas as pd


# csv_file = '/home/tspl/Documents/Script_baz_lol/allBackup.csv'
# df = pd.read_csv(csv_file)
# i=0
# hm={}
# for index, row in df.iterrows():
#    if(row["Region"]=="AHEMDABAD BRANCH"):
#       val=row["Town"]
#       if val not in hm:
#          ls=[]
#          ls.append(row["Brand Code"])
#          hm[val]=ls
#       else:
#          hm[val].append(str(row["Brand Code"]))
      
# print(hm)



import pandas as pd

csv_file = '/home/tspl/Documents/Script_baz_lol/allBackuooooooooop.csv'
df = pd.read_csv(csv_file)

hm = {}

for index, row in df.iterrows():
   if row["Region"] == "MUMBAI BRANCH":
      val = row["Town"]
      if val not in hm:
         ls = []
         ls.append(row["Brand Code"])
         hm[val] = ls
      else:
         hm[val].append(str(row["Brand Code"]))

result_df = pd.DataFrame(list(hm.items()), columns=['Town', 'Brand Codes'])

result_df.to_csv('/home/tspl/Documents/Script_baz_lol/mumbaikoop.csv', index=False)

