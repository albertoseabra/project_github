import pandas as pd
import os
import re


os.chdir('c:\\precourse\project\project_github\data')


def average_area_data():
    """
    extracts the data for the four years(2014 until 2017), cleans, merges and saves for a csv file
    also returns the data set
    """

    years = ['14', '15', '16', '17']
    files_name = ['average_area_' + x for x in years]

    first = pd.read_csv(str(files_name[0]) + '.csv', encoding='latin1', na_values=['n.d.', 'n.d'],
                        usecols=[0, 1, 2, 3, 4, 5])

    second = pd.read_csv(str(files_name[1]) + '.csv', encoding='latin1', na_values=['n.d.', 'n.d'],
                         usecols=[0, 1, 2, 3, 4, 5])

    third = pd.read_csv(str(files_name[2]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                        usecols=[0, 1, 2, 3, 4, 5], decimal=',')

    fourth = pd.read_csv(str(files_name[3]) + '.csv', skiprows=[1], na_values=['n.d.', 'n.d', 'nd'],
                         usecols=[0, 1, 2], decimal=',')

    second.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    third.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    fourth.drop(['Dte.', 'Barris'], inplace=True, axis=1)

    merge_data = pd.concat([first, second, third, fourth], axis=1)

    columns = ['Dte.', 'Barris', '1st Trim 2014', '2nd Trim 2014', '3rd Trim 2014', '4th Trim 2014', '1st Trim 2015',
               '2nd Trim 2015', '3rd Trim 2015', '4th Trim 2015', '1st Trim 2016', '2nd Trim 2016', '3rd Trim 2016',
               '4th Trim 2016', '1st Trim 2017']
    merge_data.columns = columns

    merge_data['evolution_area'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014'])\
                                    / merge_data['1st Trim 2014'] * 100

    # merge_data.to_csv('new_area.csv')

    return merge_data


def average_rent_data():
    """
    extracts the data for the four years(2014 until 2017), cleans, merges and saves for a csv file
    also returns the data set
    """

    years = ['14', '15', '16', '17']
    files_name = ['average_rent_' + x for x in years]

    first = pd.read_csv(str(files_name[0]) + '.csv', skiprows=[0, 2], na_values=['n.d.', 'n.d', 'nd'],
                        usecols=[0, 1, 2, 3, 4, 5], decimal=',')

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

    second.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    third.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    fourth.drop(['Dte.', 'Barris'], inplace=True, axis=1)

    merge_data = pd.concat([first, second, third, fourth], axis=1)

    columns = ['Dte.', 'Barris', '1st Trim 2014', '2nd Trim 2014', '3rd Trim 2014', '4th Trim 2014', '1st Trim 2015',
               '2nd Trim 2015', '3rd Trim 2015', '4th Trim 2015', '1st Trim 2016', '2nd Trim 2016', '3rd Trim 2016',
               '4th Trim 2016', '1st Trim 2017']
    merge_data.columns = columns

    merge_data['evolution_area'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014']) \
                                   / merge_data['1st Trim 2014'] * 100

    # merge_data.to_csv('new_rent.csv')

    return merge_data


def average_rent_m2_data():
    """
    extracts the data for the four years(2014 until 2017), cleans, merges and saves for a csv file
    also returns the data set
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

    second.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    third.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    fourth.drop(['Dte.', 'Barris'], inplace=True, axis=1)

    merge_data = pd.concat([first, second, third, fourth], axis=1)

    columns = ['Dte.', 'Barris', '1st Trim 2014', '2nd Trim 2014', '3rd Trim 2014', '4th Trim 2014', '1st Trim 2015',
               '2nd Trim 2015', '3rd Trim 2015', '4th Trim 2015', '1st Trim 2016', '2nd Trim 2016', '3rd Trim 2016',
               '4th Trim 2016', '1st Trim 2017']
    merge_data.columns = columns

    merge_data['evolution_area'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014']) \
                                   / merge_data['1st Trim 2014'] * 100

    # merge_data.to_csv('new_rent_m2.csv')

    return merge_data


def contracts_data():
    """
    extracts the data for the four years(2014 until 2017), cleans, merges and saves for a csv file
    also returns the data set
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

    second.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    third.drop(['Dte.', 'Barris'], inplace=True, axis=1)
    fourth.drop(['Dte.', 'Barris'], inplace=True, axis=1)

    merge_data = pd.concat([first, second, third, fourth], axis=1)

    columns = ['Dte.', 'Barris', '1st Trim 2014', '2nd Trim 2014', '3rd Trim 2014', '4th Trim 2014', '1st Trim 2015',
               '2nd Trim 2015', '3rd Trim 2015', '4th Trim 2015', '1st Trim 2016', '2nd Trim 2016', '3rd Trim 2016',
               '4th Trim 2016', '1st Trim 2017']
    merge_data.columns = columns

    merge_data['evolution_area'] = (merge_data['1st Trim 2017'] - merge_data['1st Trim 2014']) \
                                   / merge_data['1st Trim 2014'] * 100

    # merge_data.to_csv('new_contracts.csv')

    return merge_data


# average_area_data()
# average_rent_data()
# average_rent_m2_data()
# contracts_data()