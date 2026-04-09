import pandas as pd 
import plotly.express as px
df = pd.read_csv('CourtenayMillsRecordsEdited.csv')
fig = px.pie(df, values='ID Number', names='Denomination', title='Religious Affiliations of Mill Employees')
fig.show()

count = df['ID Number'].value_counts()
df = df.assign('count')
df = pd.read_csv('CourtenayMillsRecordsEdited.csv').query("Denomination != 'Baptist'")
df = px.bar(df, x='count', y='Denomination', title='Religious Affiliations of Employees who are Not Baptist')