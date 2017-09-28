import pandas as pd
import os
import re


os.chdir('c:\\precourse\project\project_github\data')


def evolution_column(file):
    data = pd.read_csv(str(file) + '.csv', encoding='latin1', na_values='nd', decimal=',')

    data.drop(['Unnamed: 0', 'Dte.'], inplace=True, axis=1)

    columns = ['Barris', '1st Tri 2014', '2nd Tri 2014', '3rd Tri 2014', '4th Tri 2014', '1st Tri 2015',
               '2nd Tri 2015', '3rd Tri 2015', '4th Tri 2015', '1st Tri 2016', '2nd Tri 2016',
               '3rd Tri 2016', '4th Tri 2016', '1st Tri 2017']

    data.columns = columns

    # even using Pandas to read the decimals as ',' it fails to do that for every column and doesnt convert to float
    # using any different type of csv.Dialect when reading the file also fails
    # even trying to convert astype gives us a ValueError for some files
    try:
        data['1st Tri 2014'] = data['1st Tri 2014'].astype('float')
        data['1st Tri 2017'] = data['1st Tri 2017'].astype('float')
    except ValueError:
        # will try to replace the ',' for '.' using regular expressions and then convert to float
        # replace ',' for '.'
        repl = lambda x: re.sub(r',', '.', str(x))
        # replace '.' for ','
        repl2 = lambda x: re.sub(r'\.', '', str(x), count=1)
        # still gives an error trying to convert to float because of some 'nd.' values that pandas didnt parse
        repl_nd = lambda x: re.sub(r'nd.', '0', str(x))
        columns = ['1st Tri 2014', '1st Tri 2017']
        for column in columns:
            data[column] = data[column].apply(repl2)
            data[column] = data[column].apply(repl)
            data[column] = data[column].apply(repl_nd)

    finally:

        data['Evolution'] = (data['1st Tri 2017'].astype('float') - data['1st Tri 2014'].astype('float')) \
                            / data['1st Tri 2014'].astype('float') * 100

    data.to_csv(str(file)+'2.csv')
    return data


# WORKS FOR THESE 2 DATASETS:
contracts = evolution_column('number_contracts')
area = evolution_column('average_area')


# FOR AVERAGE RENT PER M2:
rent_m2 = pd.read_csv('average_rent_per_m2.csv', encoding='latin1', na_values='nd', decimal=',')

rent_m2.drop(['Unnamed: 0', 'Dte.'], inplace=True, axis=1)

columns = ['Barris', '1st Tri 2014', '2nd Tri 2014', '3rd Tri 2014', '4th Tri 2014', '1st Tri 2015',
           '2nd Tri 2015', '3rd Tri 2015', '4th Tri 2015', '1st Tri 2016', '2nd Tri 2016',
           '3rd Tri 2016', '4th Tri 2016', '1st Tri 2017']
rent_m2.columns = columns

# need to replace ',' for '.' but only in the 2017 column, 2014 works fine without changing
repl = lambda x: re.sub(r',', '.', str(x))
rent_m2['1st Tri 2017'] = rent_m2['1st Tri 2017'].apply(repl)

# need to replace now a different expression 'n.d.' for empty values
repl_nd = lambda x: re.sub(r'n.d.', '0', str(x))
rent_m2['1st Tri 2017'] = rent_m2['1st Tri 2017'].apply(repl_nd)
rent_m2['1st Tri 2014'] = rent_m2['1st Tri 2014'].apply(repl_nd)

rent_m2['Evolution'] = (rent_m2['1st Tri 2017'].astype('float') - rent_m2['1st Tri 2014'].astype('float')) \
                            / rent_m2['1st Tri 2014'].astype('float') * 100

rent_m2.to_csv('average_rent_per_m22.csv')

# FOR AVERAGE RENT:
rent = pd.read_csv('average_rent.csv', encoding='latin1', na_values='nd', decimal=',', skiprows=[1])
rent.drop(['Unnamed: 0', 'Dte.'], inplace=True, axis=1)

columns = ['Barris', '1st Tri 2014', '2nd Tri 2014', '3rd Tri 2014', '4th Tri 2014', '1st Tri 2015',
           '2nd Tri 2015', '3rd Tri 2015', '4th Tri 2015', '1st Tri 2016', '2nd Tri 2016',
           '3rd Tri 2016', '4th Tri 2016', '1st Tri 2017']
rent.columns = columns


# replace '.' for ',', but now only for 2014
repl2 = lambda x: re.sub(r'\.', '', str(x), count=1)
rent['1st Tri 2014'] = rent['1st Tri 2014'].apply(repl2)
# need to replace ',' for '.' but only in the 2014 column, 2017 works fine without changing
repl = lambda x: re.sub(r',', '.', str(x))
rent['1st Tri 2014'] = rent['1st Tri 2014'].apply(repl)

rent['Evolution'] = (rent['1st Tri 2017'].astype('float') - rent['1st Tri 2014'].astype('float')) \
                            / rent['1st Tri 2014'].astype('float') * 100

rent.to_csv('average_rent2.csv')


# will append the evolution columns to the comparison data file
comparison = pd.read_csv('comparison_data.csv', encoding='latin1', skiprows=[1])


final = pd.concat([comparison, area.Evolution, rent_m2.Evolution, contracts.Evolution, rent.Evolution], axis=1)
columns = ['Unnamed: 0', 'Dte.', 'Barris', 'average_area', 'average_rent', 'average_rent_per_m2',
           'number_contracts', 'area_evol', 'rent_m2_evol', 'contracts_evol', 'rent_evol']

final.columns = columns

final.to_csv('comparison2.csv')

