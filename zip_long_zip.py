from itertools import zip_longest

cities = ['Rio', 'Fortaleza', 'Belo Horizonte']

slugs_cities = ['RJ', 'FZ', 'BH']

new_dict = zip(cities, slugs_cities)

print(new_dict)

for key, value in new_dict:
    print('Key: ', key, ' Value: ', value)

# Wrong size list slugs
slugs_cities = ['RJ', 'FZ', 'BH', 'FL', 'ES']
new_dict = zip_longest(cities, slugs_cities, fillvalue='Estado')


for key, value in new_dict:
    print('Key: ', key, ' Value: ', value)