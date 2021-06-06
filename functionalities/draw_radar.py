import plotly.graph_objects as go
import pandas as pd
import numpy as np
def draw_radar(df9,df10):



    # Remove rows with a nan
    df10 = df10[df9.Considerar_pais != 0]
    df10 = df10[np.logical_not(np.isnan(df10.Cluster))]
    df10 = df10.reset_index(drop=True)
    
    
    #Keep names
    names=list(df10.country)
    nn=len(names)
    
    
    #Keep titles
    data_top = df10.head(1)
    var=data_top.iloc[1:1, 4:30].columns
    categories=list(var)
    
    #Keep values
    values = df10[categories]
    
    
    #Create figure
    fig = go.Figure()
    
    
    # Create dimensions                      
    for i in range(nn):
        fig.add_trace(go.Scatterpolar(
            r= values.loc[i],
            theta=categories,
            fill='none',
            name=names[i]
        ))
    
    
    fig.update_layout(
      polar=dict(
          radialaxis=dict(
          visible=True,
          range=[0, values.max()]
        )),
      showlegend=True,
      paper_bgcolor='rgba(0,0,0,0)',
      font_color="#70BFFA"
    )
    fig.write_html('radar.html', auto_open=True)