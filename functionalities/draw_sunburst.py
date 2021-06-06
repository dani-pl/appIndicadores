# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:32:10 2020

@author: Daniel
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

def draw_sunburst(df9,df10,df11):

 
    
    #df10 = df10.loc[:, ~df10.columns.str.contains('^Unnamed')]
    
    df = pd.concat([df10, df11.reindex(df10.index)], axis=1)
    
    #Variable for quantification
    data_top = df.head(1)
    var=data_top.iloc[1:1, 0:50].columns
    titles=list(var)
    long_df=len(titles)
    
    
    # Remove rows with a nan or with a 0 in Considerar_pais
    df = df[df9.Considerar_pais != 0]
    df = df[df['Cluster'].notna()]
    df = df.reset_index(drop=True)
     
    values = df[titles[4:(long_df-2)]]
    
    #Create figure 
    fig = px.sunburst(df, path=['Cluster', 'country'], hover_data =values, values=titles[long_df-2])
    fig.update_layout(title_text=titles[long_df-2], title_x=0.5)
    fig.update_layout(
      paper_bgcolor='rgba(0,0,0,0)',
      font_color="#70BFFA"
    )
    fig.write_html('sunburst.html', auto_open=True)