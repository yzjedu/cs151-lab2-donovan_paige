# Programmers: Donovan and Paige
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement: Will determine the expected population in the future (a certain number of years away)
# for a country based on a current population amount if you are given (1) how often someone is born (in seconds),
# (2) how often someone dies (in seconds), and (3) how often a new immigrant joins the country (in seconds)
# Data In: How many second between each birth, how many seconds between each death, how many seconds between each
# immigration,the current population, how many years in the future
# Data Out: Whether the population increased or decreased
# Credits: Class resources

#purpose: the population in a certain amount of years and whether it increases or decreases

#ask user how many seconds between each birth, death, and immigrants
birth_secs = int(input("How many seconds between each birth?"))
death_secs = int(input("How many seconds between each birth?"))
immigrant_secs = int(input("How many seconds between immigrants?"))

#ask user what the current population is
population = int(input("What is the current population?"))

#ask user how many years in the future they want in order to see the expected population
future_years = int(input("How many years in the future?"))

secs_per_year = 31536000

#calculation to find the change in population
change_population = (secs_per_year/ birth_secs + secs_per_year / immigrant_secs - secs_per_year /
                     death_secs) * future_years

#calculation to find the future population
future_population = population + change_population

#outputs the population in the amount of years the user inputs
print("The population in", future_years, "years will be:", int(future_population))

#outputs if the population increased or decreased in the time amount of years the user input
if future_population > population:
    print ("Population increased")
elif future_population < population:
    print("Population decreased")
else:
    print ("Population stays the same")
