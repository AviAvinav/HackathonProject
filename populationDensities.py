from typing import List, Any

import wikipedia
import chempy
from pip._vendor.distlib.compat import raw_input


def printSortedList(countries, countryDens, sortBy, incOrDec):
    # sorts alphabetically
    if (sortBy == 'a'):
        if (incOrDec == 'i'):
            ''' since the array is already in alphabetical order, there is no need to sort'''
        # sorts in decreasing order
        elif (incOrDec == 'd'):
                for i in range(len(countries)):
                    minIndex = i
                    for j in range(i + 1, len(countries) ):
                        if countries[j] > countries[minIndex]:
                            minIndex = j
                    countries[i], countries[minIndex] = countries[minIndex], countries[i]
                    countryDens[i], countryDens[minIndex] = countryDens[minIndex], countryDens[i]
    # sorts by population density
    elif (sortBy == 'p'):
        # sorts by increasing order
        if (incOrDec == 'i'):
            for i in range(len(countryDens)):
                minIndex = i
                for j in range(i + 1, len(countryDens)):
                    if countryDens[minIndex] > countryDens[j]:
                        minIndex = j
                countryDens[i], countryDens[minIndex] = countryDens[minIndex], countryDens[i]
                countries[i], countries[minIndex] = countries[minIndex], countries[i]
        # sorts in decreasing order
        elif (incOrDec == 'd'):
            for i in range(len(countryDens)):
                minIndex = i
                for j in range(i + 1, len(countryDens)):
                    if countryDens[j] > countryDens[minIndex]:
                        minIndex = j
                countryDens[i], countryDens[minIndex] = countryDens[minIndex], countryDens[i]
                countries[i], countries[minIndex] = countries[minIndex], countries[i]
    #print statement
    for i in range(len(countries)):
        print(countries[i], ":", countryDens[i])


def main():
    # creating Lists of countries and their corresponding population densities
    countries: List[str] = []
    countryDens: List[int] = []

    # opens file
    popDens = open("population_data.txt", "r")
    popDensLine = popDens.readlines()

    # filling the lists of countries and their corresponding population densities
    iteration = 0
    x: str
    for x in popDensLine:
        if iteration % 2 == 0:
            countries.append(x[:-1])
        elif iteration % 2 == 1:
            countryDens.append(int(x[:-1]))
        iteration += 1
    popDens.close()

    sortBy = raw_input('Would you like to sort alphabetically (type a), or by population density (type p): ')
    # escape function
    while (sortBy != 'a') and (sortBy != 'p'):
        print('you have entered a command that does not exist, please try again')
        sortBy = raw_input('Would you like to sort alphabetically (type a), or by population density (type p): ')

    incOrDec: str = raw_input('Would you like to sort in increasing (type i), or decreasing (type d): ')
    # escape function
    while (incOrDec != 'i') and (incOrDec != 'd'):
        print('you have entered a command that does not exist, please try again')
        incOrDec = raw_input('Would you like to sort in increasing (type i), or decreasing (type d): ')

    # prints sorted list of population densities based on user input
    printSortedList(countries, countryDens, sortBy, incOrDec)


if __name__ == "__main__":
    main()
