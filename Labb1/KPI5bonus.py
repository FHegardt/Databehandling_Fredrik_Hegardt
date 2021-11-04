import pandas as pd
import seaborn as sns
import numpy as np
import plotly_express as px

# KPI 5 - Andelen vaccinerade med en / två doser per kommun och vecka från 2020-v53
# till 2021-v44 plottad med ett rörligt diagram i Plotly Express.

#NOTERA, DU MÅSTE VARA INNE DIREKT I LABB1 i VS FÖR ATT KODEN SKA FUNGERA!





vaccin = pd.ExcelFile("Folkhalsomyndigheten_Covid19_Vaccine.xlsx")
vaccin_kommun3 = pd.read_excel(vaccin, 'Vaccinerade tidsserie')
vaccin_kommun4 = pd.read_excel(vaccin, 'Vaccinerade tidsserie')

vaccin_kommun3 = vaccin_kommun3.drop_duplicates(subset = ("Region", "Vecka"))

vaccin_kommun4 = vaccin_kommun4.drop_duplicates(subset = ("Region","Vecka"), keep= "last")


bigdata = vaccin_kommun3.merge(vaccin_kommun4, how= "inner", on = ("Vecka", "Region"))
bigdata = bigdata.rename({"Andel vaccinerade_x" : "Vaccinerade med en dos", "Andel vaccinerade_y" : "Fullvaccinerade"}, axis = 1)

fig = px.scatter(bigdata, x =  "Vaccinerade med en dos" , y = "Fullvaccinerade", 
    size= "Antal vaccinerade_x",
    title = " Andelen vaccinerade med en / två doser per kommun och vecka från 2020-v55 till 2021-v41",
    color = "Region", size_max = 70,
    log_x = False, animation_frame = "Vecka",
    range_x = [0, 1], range_y = [0,1])
fig.show()