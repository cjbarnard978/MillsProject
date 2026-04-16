import pandas as pd 
import plotly.express as px
df = pd.read_csv('CourtenayMillsRecordsCorrected.csv')
fig = px.pie(df, values='ID Number', names='Denomination', title='Religious Affiliations of Mill Employees')
fig.show()

