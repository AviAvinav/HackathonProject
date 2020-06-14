from typing import List, Any

import wikipedia
import chempy


def main():
    # creating Lists of countries and their corresponding population densities
    countries: List[str] = []
    countryDens: List[int] = []


    #opens file
    popDens = open("population_data.txt", "r")
    popDensLine = popDens.readlines()
    iteration = 0
    x: str
    for x in popDensLine:
        if iteration % 2 == 0:
            countries.append(x)
        if iteration % 2 == 1:
            countryDens.append(x)


    popDens.close()

if __name__ == "__main__":
    main()
