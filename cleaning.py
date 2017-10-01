import pandas as pd
import os
import re


os.chdir('c:\\precourse\project\project_github\data')


def average_area_data(save=False):
    """
    extracts the data for the four years(2014 until 2017), cleans, merges, calculates the evolution from 2014 until 2017
    saves to a csv file if save = True
    returns the data set
    """

    years = ['14', '15', '16', '17']
    files_name = ['average_area_' + x for x in years]

    # for 2014 and 2015 need to use a different encoding and will ignore the columns the accumulated values
    first = pd.read_csv(str(files_name[0]) + '.csv', encoding='latin1', na_values=['n.d.', 'n.d'],
                        usecols=[0, 1, 2, 3, 4, 5])

    second = pd.read_csv(str(files_name[1]) + '.csv', encoding='latin1', na_values=['n.d.', 'n.d'],
                         usecols=[0, 1, 2, 3, 4, 5])

    # will ignore a new column that was introduced in 2016 to avoid problems merging, also now use ',' as decimals
    third = pd.read_csv(str(files_name[2]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                        usecols=[0, 1, 2, 3, 4, 5], decimal=',')

    fourth = pd.read_csv(str(files_name[3]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                         usecols=[0, 1, 2], decimal=',')

    # merging the data
    merge_data = merging_data(first, second, third, fourth)

    # calculate the variation in %
    merge_data['evolution_area'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014'])\
                                    / merge_data['1st Trim 2014'] * 100

    # in case you want to save the data set to a csv file
    if save:
        merge_data.to_csv('new_area.csv')

    return merge_data


def average_rent_data(save=False):
    """
    extracts the data for the four years(2014 until 2017), cleans, merges, calculates the evolution from 2014 until 2017
    saves to a csv file if save = True
    returns the data set
    """

    years = ['14', '15', '16', '17']
    files_name = ['average_rent_' + x for x in years]

    first = pd.read_csv(str(files_name[0]) + '.csv', skiprows=[0, 2], na_values=['n.d.', 'n.d', 'nd'],
                        usecols=[0, 1, 2, 3, 4, 5], decimal=',')

    # Pandas cannot parse the data as numbers even using ',' as decimals, using different csv dialects also don't work
    # will remove the '.' used as thousands and then replace the ',' for '.' to be able to convert the data to float
    for column in first.columns[2:6]:
        first[column] = first[column].apply(lambda x: re.sub('\.', '', str(x)))
        first[column] = first[column].apply(lambda x: re.sub(',', '.', str(x)))
        first[column] = first[column].astype('float')

    second = pd.read_csv(str(files_name[1]) + '.csv', skiprows=[0, 2], na_values=['n.d.', 'n.d', 'nd'],
                         usecols=[0, 1, 2, 3, 4, 5], decimal=',')

    for column in first.columns[2:6]:
        second[column] = second[column].apply(lambda x: re.sub('\.', '', str(x)))
        second[column] = second[column].apply(lambda x: re.sub(',', '.', str(x)))
        second[column] = second[column].astype('float')

    third = pd.read_csv(str(files_name[2]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                        usecols=[0, 1, 2, 3, 4, 5], decimal=',')

    fourth = pd.read_csv(str(files_name[3]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                         usecols=[0, 1, 2], decimal=',')

    # merging the data and calculating the variation in %
    merge_data = merging_data(first, second, third, fourth)

    merge_data['evolution_rent'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014']) \
                                   / merge_data['1st Trim 2014'] * 100

    if save:
        merge_data.to_csv('new_rent.csv')

    return merge_data


def average_rent_m2_data(save=False):
    """
    extracts the data for the four years(2014 until 2017), cleans, merges, calculates the evolution from 2014 until 2017
    saves to a csv file if save = True
    returns the data set
    """

    years = ['14', '15', '16', '17']
    files_name = ['average_rent_per_m2_' + x for x in years]

    first = pd.read_csv(str(files_name[0]) + '.csv', na_values=['n.d.', 'n.d', 'nd'], encoding='latin1',
                        usecols=[0, 1, 2, 3, 4, 5])

    second = pd.read_csv(str(files_name[1]) + '.csv', na_values=['n.d.', 'n.d', 'nd'], encoding='latin1',
                         usecols=[0, 1, 2, 3, 4, 5])

    third = pd.read_csv(str(files_name[2]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                        usecols=[0, 1, 2, 3, 4, 5], decimal=',')

    fourth = pd.read_csv(str(files_name[3]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                         usecols=[0, 1, 2], decimal=',')

    # merging the data and calculating the variation in %
    merge_data = merging_data(first, second, third, fourth)

    merge_data['evolution_rent_m2'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014']) \
                                   / merge_data['1st Trim 2014'] * 100

    if save:
        merge_data.to_csv('new_rent_m2.csv')

    return merge_data


def contracts_data(save=False):
    """
    extracts the data for the four years(2014 until 2017), cleans, merges, calculates the evolution from 2014 until 2017
    saves to a csv file if save = True
    returns the data set
    """

    years = ['14', '15', '16', '17']
    files_name = ['number_contracts_' + x for x in years]

    first = pd.read_csv(str(files_name[0]) + '.csv', na_values=['n.d.', 'n.d', 'nd'], encoding='latin1', skiprows=[0],
                        usecols=[0, 1, 2, 3, 4, 5], skipfooter=1)

    second = pd.read_csv(str(files_name[1]) + '.csv', na_values=['n.d.', 'n.d', 'nd'], encoding='latin1',
                         usecols=[0, 1, 2, 3, 4, 5], skipfooter=1)

    third = pd.read_csv(str(files_name[2]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                        usecols=[0, 1, 2, 3, 4, 5], skipfooter=1)

    fourth = pd.read_csv(str(files_name[3]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                         usecols=[0, 1, 2], skipfooter=1)

    # merging the data and calculating the variation in %
    merge_data = merging_data(first, second, third, fourth)

    merge_data['evolution_contracts'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014']) \
                                   / merge_data['1st Trim 2014'] * 100

    if save:
        merge_data.to_csv('new_contracts.csv')

    return merge_data


def merging_data(first, second, third, fourth):
    """
    Merges the data of the four data sets
    :return: the merged data set
    """

    # trying to merge giver error or i lose most of the data, will need to use concat
    # first will drop the repeated columns and keep only the ones with the data
    second.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    third.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    fourth.drop(['Dte.', 'Barris'], inplace=True, axis=1)

    merge_data = pd.concat([first, second, third, fourth], axis=1)

    # giving easier names to the columns
    columns = ['Dte.', 'Barris', '1st Trim 2014', '2nd Trim 2014', '3rd Trim 2014', '4th Trim 2014', '1st Trim 2015',
               '2nd Trim 2015', '3rd Trim 2015', '4th Trim 2015', '1st Trim 2016', '2nd Trim 2016', '3rd Trim 2016',
               '4th Trim 2016', '1st Trim 2017']
    merge_data.columns = columns

    return merge_data


def comparison_data(save=False):
    """
    Gets the files of average area, average rent, average rent per m^2 and number of contracts of 2017
    merges them together in only one file, cleans the names of the barrios
    if finds the files with the evolution of the prices it also adds the evolution columns to the data
    saves if save=True
    :return: the merged data of 2017 with or without evolution columns
    """

    average_area = pd.read_csv('average_area_17.csv', usecols=[0, 1, 2], decimal=',', na_values=['n.d.', 'n.d', 'nd'],
                               skiprows=[1])
    average_rent = pd.read_csv('average_rent_17.csv', usecols=[2], decimal=',', na_values=['n.d.', 'n.d', 'nd'],
                               skiprows=[1])
    average_rent_per_m2 = pd.read_csv('average_rent_per_m2_17.csv', usecols=[2], decimal=',', na_values=['n.d.', 'nd'],
                                      skiprows=[1])
    number_contracts = pd.read_csv('number_contracts_17.csv', usecols=[2], decimal=',', na_values=['n.d.', 'n.d', 'nd'],
                                   skiprows=[1])

    comparison = pd.concat([average_area, average_rent, average_rent_per_m2, number_contracts], axis=1)

    columns = ['Dte.', 'Barris', 'average_area', 'average_rent', 'average_rent_per_m2', 'number_contracts']
    comparison.columns = columns

    # because it will be useful later will clean now the names of the barrios
    # will split the column with the names and discard the initial part example: "1. el Raval" <-- we want only the name
    # need to remove last column first, its not useful and gives us an index error
    comparison = comparison.iloc[1:-1]
    comparison['Barris'] = comparison['Barris'].apply(lambda x: str(x).split(' ', 1)[1])

    # will try to join the columns with the variation to this data set, if the files don't exist will return the
    # data without the columns with the evolution anyway and print a warning
    try:
        area = pd.read_csv('new_area.csv', encoding='latin1')
        rent = pd.read_csv('new_rent.csv', encoding='latin1')
        rent_m2 = pd.read_csv('new_rent_m2.csv', encoding='latin1')
        contracts = pd.read_csv('new_contracts.csv', encoding='latin1')

        comparison = pd.concat([comparison, area['evolution_area'], rent['evolution_rent'],
                                rent_m2['evolution_rent_m2'], contracts['evolution_contracts']], axis=1)
    except FileNotFoundError:
        print('Was not able to join the evolution data, please confirm that the files new_area.csv, new_rent.csv,'
              'new_rent_m2.csv and new_contracts.csv exists if you want that data.')

    if save:
        comparison.to_csv('new_comparison.csv')

    return comparison


# average_area_data()
# average_rent_data()
# average_rent_m2_data()
# contracts_data()

# comparison_data()
