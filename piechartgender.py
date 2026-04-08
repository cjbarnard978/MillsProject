import pandas as pd 
import plotly.express as px
df = pd.read_csv('CourtenayMillsRecordsEdited.csv').query("Gender == 'F'")
fig = px.pie(df, values='ID Number', names='Denomination', title='Religious Affiliations of Women')
fig.show()

df = pd.read_csv('CourtenayMillsRecordsEdited.csv').query("Gender == 'M'")
fig = px.pie(df, values='ID Number', names='Denomination', title='Religious Affiliations of Men')
fig.show()

df = pd.read_csv('CourtenayMillsRecordsEdited.csv')
fig = px.pie(df, values='ID Number', names='Marital Status', title='Marital Status of Employees who Identified a Religious Affiliation')
fig.show()