import pandas as pd 
import plotly.express as px
df = pd.read_csv('CourtenayMillsRecordsEdited.csv').query("M/F == 'F'")
