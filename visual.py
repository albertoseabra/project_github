import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import os
import re

os.chdir('c:\\precourse\project\project_github\data')

data_file = pd.read_csv('new_comparison.csv', encoding='latin1')


columns = ['average_area', 'average_rent', 'average_rent_per_m2', 'number_contracts']
legends = ['AVERAGE AREA', 'AVERAGE RENT', 'AVERAGE RENT PER M2', 'NUMBER OF NEW CONTRACTS']
colors = ['RdPu', 'YlGn', 'OrRd', 'YlOrRd']


def search_barrio(string):
    found = []
    number = 0

    for name in data_file.Barris:
        if re.search(string.lower(), str(name).lower()):
            number += 1
            found.append((number, name))

    return found


def draw_folium(type, color='OrRd'):
    map = folium.Map(location=[41.41, 2.15], zoom_start=13)

    map.choropleth(geo_data='barris_geo.json', name='choropleth', data=data_file, columns=['Barris', columns[type]],
                   key_on='feature.properties.N_Barri', fill_color=color, fill_opacity=0.7, line_opacity=0.4,
                   legend_name=legends[type], highlight= True)

    map.save(str(columns[type])+'.html')


def draw_bars(type, title='', y_label=''):
    try:
        title = str(title)
    except:
        title = ''
    try:
        y_label = str(y_label)
    except:
        y_label = ''

    compare = sns.barplot(x='Barris', y=type, palette='gist_rainbow',
                          data=data_file.sort_values(by=type, ascending=False))
    compare.axes.set_title(title, size=25, color='r')
    compare.set_ylabel(y_label, size=15)
    for item in compare.get_xticklabels():
        item.set_rotation(90)

    plt.subplots_adjust(top=0.95, bottom=0.2, left=0.04, right=0.98)
    plt.show()


def choose_bar_map():
    print('There are 4 comparison maps to choose from, they compare the current values of:')
    print('Option 1: Average Rent')
    print('Option 2: Average rent per M^2')
    print('Option 3: Number of contracts')
    print('Option 4: Average area of the apartments')
    choice = input('Which one do you want?(any other key to quit):')
    if choice == '1':
        draw_bars('average_rent', title='Average Monthly Rent - 1st Trimester of 2017', y_label='Rent(€)')
    elif choice == '2':
        draw_bars('average_rent_per_m2', title='Average Rent per M^2 - 1st Trimester of 2017', y_label='Rent per M^2(€)')
    elif choice == '3':
        draw_bars('number_contracts', title='Number of new contracts - 1st Trimester of 2017', y_label='New Contracts')
    elif choice == '4':
        draw_bars('average_area', title='Average area of apartments - 1st Trimester of 2017', y_label='Area(M^2')

