import pandas as pd 
import plotly.express as px
df = pd.read_csv('CourtenayMillsRecordsEdited.csv').query("Gender == 'F'")
fig = px.pie(df, values='ID Number', names='Denomination', title='Religious Affiliations of Women')
fig.show()

