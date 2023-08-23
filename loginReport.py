path="/home/tspl/Documents/Script_baz_lol/loginReportCal/attendence.csv"
import pandas as pd

df = pd.read_csv(path)
df['login_date'] = pd.to_datetime(df['login_date'])
df['login_date'] = df['login_date'].dt.date
login_counts = df['login_date'].value_counts()
login_counts_df = login_counts.reset_index()
login_counts_df.columns = ['login_date', 'login_count']
login_counts_df.to_csv('/home/tspl/Documents/Script_baz_lol/loginReportCal/login_counts_result.csv', index=False)
print(type(login_counts))
print("Date\t\tLogin Count")
for date, count in login_counts.items():
    print(f"{date}\t{count}")
