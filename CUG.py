#Day 1 of 100 Days of code challenge
import random

print("Hello and Welcome to Crazy Username Generator!!!")
pets_name = input("What is your pets name?: ")
cool_verbs_table = ["Basher", "clobberer", "Ambusher", "Smiter", "Pulverizer", "Reinforcer", "Oscillator", "Stalker",
                    "Exalter", "Devastator, Grappler", "Killer", "Destroyer"]
random_numbers_table = ["69", "102", "54", "36", "89", "666", "0", "13", "99", "117", "1982", "1776", "10", "111",
                        "6969", "456"]
selected_verb = random.choice(cool_verbs_table)
selected_number = random.choice(random_numbers_table)
print(pets_name + selected_verb + selected_number)