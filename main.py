# Programmers: Donovan and Paige
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement: Will determine the expected population in the future (a certain number of years away)
# for a country based on a current population amount if you are given (1) how often someone is born (in seconds),
# (2) how often someone dies (in seconds), and (3) how often a new immigrant joins the country (in seconds)
# Data In: How many second between each birth, how many seconds between each death, how many seconds between each immigration,
# the current population, how many years in the future
# Data Out: Whether the population increased or decreased
# Credits: class resources
Birth_secs = int(input("how many seconds between each birth? "))
Death_secs = int(input("how many seconds between each birth? "))
immigrant_secs = int(input("how many seconds between immigrants? "))
population = int(input("what is the current population? "))
future_years = int(input("how many years in the future? "))
secs_per_year = 31536000

change_population = (secs_per_year/ Birth_secs + secs_per_year / immigrant_secs - secs_per_year / Death_secs) * future_years
future_population = population + change_population

print("The US population in", future_years, "years will be", future_population)

if future_population > population:
    print ("population increased")
else:
    print ("population decreased")