import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import os


os.chdir('c:\\precourse\project\project_github\data')

data_file = pd.read_csv('comparison2.csv', encoding='latin1', na_values='nd')

# doing the same stuff as in the visualization file so that Folium links with the data
data_file = data_file.iloc[:-1]
# split the column with the names and discard the initial part example: "1. el Raval" <-- we want only the name
func = lambda x: str(x).split(' ', 1)[1]
data_file['Barris'] = data_file.Barris.apply(func)


columns = ['area_evol', 'rent_m2_evol', 'contracts_evol', 'rent_evol']
legends = ['EVOLUTION OF THE AVERAGE AREA (%) - 2014/2017',
           'EVOLUTION OF THE AVERAGE RENT PER M^2 (%) - 2014/2017',
           'EVOLUTION OF THE NUMBER OF NEW CONTRACTS (%) - 2014/2017',
           'EVOLUTION OF THE AVERAGE MONTHLY RENT (%) - 2014/2017']
colors = ['RdPu', 'YlGn', 'OrRd', 'YlOrRd']

# drawing and saving the Folium maps:
# for i in range(4):
#     map = folium.Map(location=[41.41, 2.15], zoom_start=13)
#
#     map.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', columns[i]],
#                    key_on='feature.properties.N_Barri', fill_color=colors[i], fill_opacity=0.7, line_opacity=0.4,
#                    legend_name=legends[i], highlight= True)
#
#     map.save(str(columns[i])+'.html')


data_file.drop(['Unnamed: 0', 'Dte.'], inplace=True, axis=1)

# making the graphs using matplotlib:
# can not pass strings, names of the barrios, as a index for an axis so will create a range
x = range(len(data_file))
# to get a sorted graph, sort the data first:
contrats_sort = data_file.sort_values(by='contracts_evol', ascending=False)

# different colors need to be defined manually:
colors = ['g', 'yellow', 'k', 'maroon', 'blue', 'red']

plt.bar(x, contrats_sort['contracts_evol'], color= colors)
# to get the barrios in the x axis need to pass the range previously created and the names of the barrios
plt.xticks(x,contrats_sort['Barris'], rotation=90)
plt.title('EVOLUTION OF THE NUMBER OF NEW CONTRACTS (%) - 2014/2017 - using Matplotlib')
plt.show()


# its easier to just use seaborn to plot the graphics if you are using different colors, you can just use a palette
compare = sns.barplot(x='Barris', y='contracts_evol', palette='gist_rainbow',
                      data=data_file.sort_values(by='contracts_evol', ascending=False))
compare.axes.set_title('EVOLUTION OF THE NUMBER OF NEW CONTRACTS (%) - 2014/2017', size=25, color='r')
compare.set_ylabel('Variation in %', size=15)
for item in compare.get_xticklabels():
    item.set_rotation(90)

plt.subplots_adjust(top=0.95, bottom=0.2, left=0.03, right=0.98)
plt.show()


