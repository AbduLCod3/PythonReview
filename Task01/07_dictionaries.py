print('')

# Dictionary
band = { "vocals" : "Plant", "guitar": "Page"}

# Creating dict with a constructor
band2 = dict (vocals = "Plant", guitar="Page")
print(band)
print(band2)
# print(type(band))
# print(type(band2))

# print(len(band))
# print(len(band2))

## Access items in dict ##
# print(band['vocals']) # OR
# print(band.get("guitar"))

## Access all keys ##
# print(band.keys())

## Access all values ##
# print(band2.values())

## Access key/values pairs as tuples ##
# print(band.items())

## Verify if a key exists in a dict ##
# print("guitar" in band)
# print("Triangle" in band)

### Update/change values or new pairs in adict

## Updates a value 
band["vocals"] = "Coverdale" 
## updates the dict by adding new a pair
band2.update({"bass" : "JPJ"}) 
## if key exists value is updated, if not a new pair is added to dict
band["drums"] = "Bonham" 

### Remove items
## pop('key') accepts key, remove pair from dict and returns the value
print(band2.pop("bass")) 
print(band)


### Remove last pair of dict
## returns pair removed as tuple
# print(band.popitem()) 

## Delete and clear dict
del band["drums"]

band2.clear()
print(band2)
del band2

### Copy dictionaires
## creates a references
# band2 = band 
# print(band)

# band2['drums'] = 'Dave'
# print(band)

## this creates an actual copy
# band2 = band.copy()
# band3 = dict(band)


### Nested a dictionaries

member1 = { 'name' : 'plant', 'instrument' : 'vocals'}
member2 = { 'name' : 'page', 'instrument' : 'guitar'}
band4 = { 'member1' : member1, 'member2' : member2}

print(band4)
print(band4["member1"]["name"])
print('')
print('')

