import pandas as pd
import seaborn as sns
import numpy as np
import plotly_express as px

vaccin = pd.ExcelFile('Folkhalsomyndigheten_Covid19_Vaccine.xlsx')
vaccin_kommun = pd.read_excel(vaccin, 'Vaccinerade tidsserie')

fig = px.scatter(vaccin_kommun, x = "Vecka", y = "Andel vaccinerade"[0], 
    size= "Antal vaccinerade",
    color = "Region", size_max = 70,
    log_x = False, animation_frame = "Vecka", title="Gapminder",
    range_x = [0, 45], range_y = [0,1])
fig.show()