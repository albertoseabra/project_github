import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import os


os.chdir('c:\\precourse\project\project_github\data')

data_file = pd.read_csv('comparison2.csv', encoding='latin1', na_values='nd')

# doing the same stuff as in the visualization file so that Folium links with the data
data_file = data_file.iloc[:-1]
func = lambda x: str(x).split(' ', 1)[1]
data_file['Barris'] = data_file.Barris.apply(func)


columns = ['area_evol', 'rent_m2_evol', 'contracts_evol', 'rent_evol']
legends = ['EVOLUTION OF THE AVERAGE AREA (%) - 2014/2017',
           'EVOLUTION OF THE AVERAGE RENT PER M^2 (%) - 2014/2017',
           'EVOLUTION OF THE NUMBER OF NEW CONTRACTS (%) - 2014/2017',
           'EVOLUTION OF THE AVERAGE MONTHLY RENT (%) - 2014/2017']
colors = ['RdPu', 'YlGn', 'OrRd', 'YlOrRd']

# UNCOMMENT TO DRAW THE FOLIUM MAPS
for i in range(4):
    map = folium.Map(location=[41.41, 2.15], zoom_start=13)

    map.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', columns[i]],
                   key_on='feature.properties.N_Barri', fill_color=colors[i], fill_opacity=0.7, line_opacity=0.4,
                   legend_name=legends[i], highlight= True)

    map.save(str(columns[i])+'.html')