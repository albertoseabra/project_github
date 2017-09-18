def extract_evolution_data(file_name):
    """
    extracts the data for the four years(2014 until 2017), cleans, merges and saves for a csv file
    also returns the data set
    """

    import pandas as pd
    import os

    os.chdir('c:\\precourse\project')
    years = ['14', '15', '16', '17']
    files_name = [str(file_name) + '_' + x for x in years]

    # going to read just the columns that matter to make it easier to re-use and it's cleaner
    first_year = pd.read_csv(str(files_name[0]) + '.csv', encoding='latin1', na_values='n.d.', usecols=[0, 1, 2, 3, 4, 5])

    second_year = pd.read_csv(str(files_name[1]) + '.csv', encoding='latin1', na_values='n.d.', usecols=[0, 1, 2, 3, 4, 5])

    # After 2016 we have a new row with the average of the city, all barrios together
    # its easier if we ignore that row when we open the file or it will give us trouble when trying to merge the data sets
    # will use the parameter skiprows that allows us to ignore the rows we want
    third_year = pd.read_csv(str(files_name[2]) + '.csv', skiprows=[1], na_values='n.d.', usecols=[0, 1, 2, 3, 4, 5])

    # the column names of this data set doesnt inform us of the year, its best to change the name in order to avoid mistakes
    columns = (['Dte.', 'Barris', '1r Trimestre 2016', '2n Trimestre 2016',
                '3r Trimestre 2016', '4rt Trimestre 2016'])
    third_year.columns = columns

    # for 2017 we only have data for the first trimester, we can ignore the remaining columns since they are empty
    fourth_year = pd.read_csv(str(files_name[2]) + '.csv', skiprows=[1], usecols=[0, 1, 2])
    fourth_year.columns = (['Dte.', 'Barris', '1r Trimestre 2017'])

    # for some reason we lose 6 rows trying to merge everything, the problem shows up merging between 2015 and 2016
    first_half = first_year.merge(second_year)
    second_half = third_year.merge(fourth_year)

    # will get rid of the first two columns in the second data set, will only keep the columns with the trimesters
    # and then concat both data sets
    second_half.drop(['Dte.', 'Barris'], axis=1, inplace=True)
    final_dataset = pd.concat([first_half, second_half], axis=1)

    final_dataset.to_csv(str(file_name)+'.csv', encoding='latin1')

    return final_dataset


def comparison_data():
    import pandas as pd
    average_area = pd.read_csv('average_area_17.csv', usecols=[0, 1, 2])
    average_rent = pd.read_csv('average_rent_17.csv', usecols=[2])
    average_rent_per_m2 = pd.read_csv('average_rent_per_m2_17.csv', usecols=[2])
    number_contracts = pd.read_csv('number_contracts_17.csv', usecols=[2])

    comparison = pd.concat([average_area, average_rent, average_rent_per_m2, number_contracts], axis=1)

    columns = ['Dte.', 'Barris', 'average_area', 'average_rent', 'average_rent_per_m2', 'number_contracts']
    comparison.columns = columns

    comparison.to_csv('comparison_data.csv', encoding='latin1')

    return comparison

# extract_evolution_data('average_rent')
# extract_evolution_data('average_area')
# extract_evolution_data('average_rent_per_m2')
# extract_evolution_data('average_area')

# data = comparison_data()


# MAKING THE COMPARISON DATA USING PYTHON READ_CSV
def comparison_csv():
    import csv

    data = []
    with open('average_area_17.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0:3])

    files = ['average_rent_17.csv', 'average_rent_per_m2_17.csv', 'number_contracts_17.csv']

    for file_name in files:

        with open(str(file_name), encoding='utf-8') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):

                # the file with number of contracts has one more row at the end
                # we can ignore that row and use exceptions to avoid the crash of the program
                try:
                    data[index].append(row[2])
                except IndexError:
                    continue
    data[0] = ['Dte.', 'Barris', 'average_area', 'average_rent', 'average_rent_per_m2', 'number_contracts']
    return data


# comparison = comparison_data()
# data = comparison_csv()
