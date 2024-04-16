#Ice Cream Combination

flavors = ['Cherry', 'Cinnamon Apple', 'Pistachio', 'Green Tea', 'Coffee Bean']

for flavor_1 in flavors:
    for flavor_2 in flavors:
        if flavor_1 == flavor_2:
            print('Double', flavor_1)
        else:
      # I was trying to figure out on how to slice it or remove 2 'flavors' from the list with the same index. But I don't think it would be a correct way. This is how I was thinking.
      # if flavor_1[0] and flavor_2[1] == flavor_2[1] and flavor_1[0]:
            print(flavor_1, flavor_2)