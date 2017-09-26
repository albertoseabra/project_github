import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


columns = ['average_area', 'average_rent', 'average_rent_per_m2', 'number_contracts']
legends = ['AVERAGE AREA', 'AVERAGE RENT', 'AVERAGE RENT PER M2', 'NUMBER OF NEW CONTRACTS']
colors = ['RdPu', 'YlGn', 'OrRd', 'YlOrRd']

# for i in range(4):
#     map = folium.Map(location=[41.41, 2.15], zoom_start=13)
#
#     map.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', columns[i]],
#                    key_on='feature.properties.N_Barri', fill_color=colors[i], fill_opacity=0.7, line_opacity=0.4,
#                    legend_name=legends[i], highlight= True)
#
#     map.save(str(columns[i])+'.html')

# compare = sns.barplot(x='Barris', y='average_rent', data=data_file)
# for item in compare.get_xticklabels():
#     item.set_rotation(90)

