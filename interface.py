import visual
import matplotlib.pyplot as plt


def main():
    barrios_to_draw = []
    while True:
        print('From which neighborhoods do you want to see the data? Press enter to show every barrio')
        barrio = input("If you don't want to add more write 'exit'")
        if barrio.lower() == 'exit':
            break
        barrios_list = visual.search_barrio(barrio)
        if not barrios_list:
            print("i didn't find any neighborhood with that name, try again.")
        else:
            print('I found some neighborhoods:')
            for i, j in barrios_list:
                print(i, j)
            while True:
                try:
                    index = int(input('What is the number of the neighborhood that you want?'))
                    break
                except ValueError:
                    print('please enter a number')
            barrios_to_draw.append(barrios_list[int(index)-1][1])
            print(barrios_to_draw)

    while True:
        print('Which information do you want to see?'
              '1 - Average Monthly Rent'
              '2 - Average Rent per M^2'
              '3 - Average Area'
              '4 - Number of New Contracts')





main()
# visual.draw_bars('average_rent', 'average rent 2017')