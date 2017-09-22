import pandas as pd
import folium
import os

os.chdir('c:\\precourse\project\project_github\data')

data_file = pd.read_csv('comparison_data.csv', encoding='latin1', skiprows=[1], na_values='nd', decimal=',')

# one of the files had one more row at the end, let's just ignore it to avoid errors
data_file = data_file.iloc[:-1]

# Folium refuses to work using as key the number of the the barrios so i will have to use the names, but for that need
# to split the column with the names and discard the initial part example: "1. el Raval" <-- we want only the name
func = lambda x: str(x).split(' ', 1)[1]

data_file['Barris'] = data_file.Barris.apply(func)

# plotting with Folium
rent_m2_map = folium.Map(location=[41.41, 2.15], zoom_start=13)

rent_m2_map.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', 'average_area'],
                       key_on='feature.properties.N_Barri', fill_color='RdPu', fill_opacity=0.7, line_opacity=0.4)

rent_m2_map.save('average_area.html')

# n = folium.Map(location=[41.39, 2.15], zoom_start=13)
#
# n.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', 'average_rent'],
#              key_on='feature.properties.N_Barri', fill_color='YlGn', fill_opacity=0.7, line_opacity=0.4)
#
# n.save('average_rent.html')
#
# o = folium.Map(location=[41.39, 2.15], zoom_start=13)
#
# o.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', 'average_rent_per_m2'],
#              key_on='feature.properties.N_Barri', fill_color='OrRd', fill_opacity=0.7, line_opacity=0.4)
#
# o.save('average_rent_per_m2.html')

