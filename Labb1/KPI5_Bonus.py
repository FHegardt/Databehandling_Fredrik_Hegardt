import pandas as pd
import seaborn as sns
import numpy as np
import plotly_express as px

vaccin = pd.ExcelFile('Folkhalsomyndigheten_Covid19_Vaccine.xlsx')
vaccin_kommun = pd.read_excel(vaccin, 'Vaccinerade tidsserie')

fig = px.scatter(vaccin_kommun, x = "Vecka", y = "Andel vaccinerade", 
    color = "Region", size_max = 70,
    log_x = False, animation_frame = "Vecka", title="Gapminder",
    range_x = [100, 100000], range_y = [25,90])
fig.show()