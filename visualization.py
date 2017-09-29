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

# UNCOMMENT TO DRAW THE FOLIUM MAPS
# for i in range(4):
#     map = folium.Map(location=[41.41, 2.15], zoom_start=13)
#
#     map.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', columns[i]],
#                    key_on='feature.properties.N_Barri', fill_color=colors[i], fill_opacity=0.7, line_opacity=0.4,
#                    legend_name=legends[i], highlight= True)
#
#     map.save(str(columns[i])+'.html')


# UNCOMMENT TO DRAW COMPARISON BAR GRAPHS AND CHANGE THE "y='number_contracts'" AND "by='number_contracts'"
# TO DRAW THE DIFFERENT GRAPHS
compare = sns.barplot(x='Barris', y='average_rent_per_m2', palette='gist_rainbow',
                      data=data_file.sort_values(by='average_rent_per_m2', ascending=False))
compare.axes.set_title('Average rent per M^2 - 1st Trimestre 2017', size=25, color='r')
compare.set_ylabel('Rent per M^2', size=15)
for item in compare.get_xticklabels():
    item.set_rotation(90)

plt.subplots_adjust(top=0.95, bottom=0.2, left=0.04, right=0.98)
plt.show()


# OTHER STUFF DONT LOOK :P
'''
data_file.drop(['Unnamed: 0', 'Dte.'], inplace=True, axis=1)
sns.jointplot(x='average_rent_per_m2',y='average_rent', data=data_file)
sns.jointplot(x='average_area',y='average_rent', data=data_file)


sns.pairplot(data_file.dropna())
sns.pairplot(data_file.dropna(), hue='Barris')

cor = data_file.corr()
sns.heatmap(cor, annot=True, cmap='coolwarm')

'''