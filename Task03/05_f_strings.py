person, coins  = 'Dave', 3

print('')

#print("\n" + person + " has " + str(coins) + " coins left.")

# message = "\n%s has %s coins left." % (person, coins)
# print(message)


# message2 = "\n{} has {} coins left.\n".format(person, coins)
# print(message2)

# message3 = "\n{0} has {1} coins left.\n".format(person, coins)
# print(message3)


# message4 = "\n{person} has {coins} coins left.\n".format(person=person, coins=coins)
# print(message4)


player = {'coins': 3, 'person':'Dave'}
# message5 = "\n{person} has {coins} coins left.\n".format(**player)
# print(message5)


### Newer FORMAT using f-strings formatting 


# message6 = f"\n{person} hass {coins} coins left."
# print(message6)

# message6 = f"\n{person} hass {285} coins left."
# print(message6)

# message6 = f"\n{person.lower()} hass {285} coins left."
# print(message6)

# message6 = f"\n{player['person'].lower()} hass {285} coins left."
# print(message6)


## Pass formatting options

num = 10
# print(f"\n 2.25 times {num} is {2.25 * num:.2f}")
# for num in range(1, 11):
#     print(f"\n 2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"\n {num} divide by 4.52 is  {num / 4.52:.2%}")