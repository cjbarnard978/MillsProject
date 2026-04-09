import numpy as np
import pandas as pd
import plotly.express as px
df = pd.read_csv('CourtenayMillsRecordsEdited.csv').query("Denomination != 'Baptist'")
fig = px.pie(df, values='ID Number', names='Denomination', title='Religious Affiliations of Employees who are Not Baptist')
fig.show()