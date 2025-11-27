from PythonSet import thisset

thisdict = {
    "brand" : "Frod",
    "model" : "Mustang",
    "year" : 1964,
    "year" : 2020,
    "colors" : ["red", "white", "blue"]
}

print(thisdict)
print(thisdict["brand"])

print(len(thisdict))
print(type(thisdict))

thisdict   = dict(name = "Mehedi", age = 21 , country = "Bangladesh")
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)
x = thisdict.keys()

thisdict["year"] = 2018
thisdict.update({"year": 2020})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)


