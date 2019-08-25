import pandas as pd
file1="//home//pi//S1.csv"
df=pd.read_csv(file1,delimiter=',')
for x in range(1,31):
    df['Day{}'.format(x)]=0
df['Attendance']=0
df.to_csv("//home//pi//AttendenceReport.csv")