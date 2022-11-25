# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.


import json
dict_state={'Karnataka':'Banglore','Arunachal Pradesh':'Itanagar','Bihar':'Patna','Maharastra':'Mumbai','Sikkim':'Gangtok','Rajasthan':'Jaipur','Kerala':'Thiruvananthapuram'}
with open("states.json","w") as f:
  capitals=json.dump(dict_state,f)
  print('json file for states and their capitals is created')

# Output

# json file for states and their capitals is created