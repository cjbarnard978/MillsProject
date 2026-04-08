import pandas as pd 
import plotly.express as px
df = pd.read_csv('CourtenayMillsRecordsEdited.csv')
fig = px.pie(df, values='ID Number', names='Denomination')
fig.show()

