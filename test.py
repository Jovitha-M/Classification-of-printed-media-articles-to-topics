import pickle
with open('text_clf_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
data = ["The latest standoff began when Rahul Gandhi's march reentered Assam From Meghalaya today. The yatra was denied permission to enter Guwahati thoroughfares and was instead asked to take the national highway bypassing the city."]
predictions = loaded_model.predict(data)
v = {35: 'U.S. NEWS', 5: 'COMEDY', 22: 'PARENTING', 40: 'WORLD NEWS', 7: 'CULTURE & ARTS', 32: 'TECH', 28: 'SPORTS', 10: 'ENTERTAINMENT', 24: 'POLITICS', 37: 'WEIRD NEWS', 11: 'ENVIRONMENT', 9: 'EDUCATION', 6: 'CRIME', 27: 'SCIENCE', 38: 'WELLNESS', 3: 'BUSINESS', 30: 'STYLE & BEAUTY', 13: 'FOOD & DRINK', 20: 'MEDIA', 25: 'QUEER VOICES', 17: 'HOME & LIVING', 39: 'WOMEN', 2: 'BLACK VOICES', 34: 'TRAVEL', 21: 'MONEY', 26: 'RELIGION', 19: 'LATINO VOICES', 18: 'IMPACT', 36: 'WEDDINGS', 4: 'COLLEGE', 23: 'PARENTS', 1: 'ARTS & CULTURE', 29: 'STYLE', 15: 'GREEN', 31: 'TASTE', 16: 'HEALTHY LIVING', 33: 'THE WORLDPOST', 14: 'GOOD NEWS', 41: 'WORLDPOST', 12: 'FIFTY', 0: 'ARTS', 8: 'DIVORCE'}
print(v[predictions[0]]);