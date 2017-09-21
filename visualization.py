import pandas as pd
import folium
import os

os.chdir('c:\\precourse\project\project_github\data')

m = folium.Map(location=[41.39, 2.15], zoom_start=13)

data_file = pd.read_csv('comparison_data.csv', encoding='latin1', skiprows=[1], na_values='nd', decimal=',')
names = ['C_Barri', 'Dte.', 'Barris', 'average_area', 'average_rent', 'average_rent_per_m2', 'number_contracts']
data_file.columns = names
data_file = data_file.iloc[:-1]

func = lambda x: str(x).split(' ', 1)[1]

data_file['Barris'] = data_file.Barris.apply(func)


m.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', 'average_area'],
             key_on='feature.properties.N_Barri', fill_color='RdPu', fill_opacity=0.7, line_opacity=0.4)


m.save('average_area.html')

n = folium.Map(location=[41.39, 2.15], zoom_start=13)

n.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', 'average_rent'],
             key_on='feature.properties.N_Barri', fill_color='YlGn', fill_opacity=0.7, line_opacity=0.4)

n.save('average_rent.html')

o = folium.Map(location=[41.39, 2.15], zoom_start=13)

o.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', 'average_rent_per_m2'],
             key_on='feature.properties.N_Barri', fill_color='OrRd', fill_opacity=0.7, line_opacity=0.4)

o.save('average_rent_per_m2.html')

# TODO: COMMENTS, IMPROVE STARTING LOCATION
