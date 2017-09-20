import pandas as pd
import folium
import os

os.chdir('c:\\precourse\project\project_github\data')

m = folium.Map(location=[41.39, 2.15], zoom_start=12)

data_file = pd.read_csv('comparison_data.csv', encoding='latin1', skiprows=[1], na_values='nd', decimal=',')
names = ['C_Barri', 'Dte.', 'Barris', 'average_area', 'average_rent', 'average_rent_per_m2', 'number_contracts']
data_file.columns = names


m.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file[:-1], columns=['C_Barri', 'average_rent'],
             key_on='C_Barri', fill_color='YlGn', fill_opacity=0.7, line_opacity=0.2)


m.save('test.html')

# TODO: DOESNT BREAK BUT IS NOT GETTING THE DATA FROM THE RENTS, PROBABLY IS FAILING TO GET THE CORRECT KEY ON 'KEY_ON'
