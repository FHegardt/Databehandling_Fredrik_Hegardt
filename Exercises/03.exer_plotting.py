from _plotly_utils.basevalidators import type_str
import plotly_express as px
import pandas as pd
import numpy as np


link = "https://sv.wikipedia.org/wiki/Sveriges_demografi"
svedemo = pd.read_html(link, match = "Befolkningsförändringar")[0]


#pd.to_numeric(svedemo["Döda"])


svedemo = svedemo.rename(dict({"Unnamed: 0" : "Start",}), axis = "columns")

fig = px.scatter(svedemo, y = "Nativiteten (per 1000)",x = "Dödstalen (per 1000)", 
     size = "Total fertilitet", size_max = 70,
    log_x = False, animation_frame = "Start", title="Sveriges Demografi",
    range_x = [50,250], range_y = [50,500])
fig.show()