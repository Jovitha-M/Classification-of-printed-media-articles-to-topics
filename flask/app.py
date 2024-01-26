from flask import Flask, render_template, request
import pickle
app = Flask(__name__, static_url_path='/static')
with open('text_clf_model.pkl', 'rb') as file:
    model = pickle.load(file)
v = {35: 'U.S. NEWS', 5: 'COMEDY', 22: 'PARENTING', 40: 'WORLD NEWS', 7:
'CULTURE & ARTS', 32: 'TECH', 28: 'SPORTS', 10: 'ENTERTAINMENT', 24:
'POLITICS', 37: 'WEIRD NEWS', 11: 'ENVIRONMENT', 9: 'EDUCATION', 6: 'CRIME',
27: 'SCIENCE', 38: 'WELLNESS', 3: 'BUSINESS', 30: 'STYLE & BEAUTY', 13: 'FOOD & DRINK', 20: 'MEDIA', 25: 'QUEER VOICES', 17: 'HOME & LIVING', 39: 'WOMEN',
2: 'BLACK VOICES', 34: 'TRAVEL', 21: 'MONEY', 26: 'RELIGION', 19: 'LATINO VOICES', 18: 'IMPACT', 36: 'WEDDINGS', 4: 'COLLEGE', 23: 'PARENTS', 1: 'ARTS & CULTURE', 29: 'STYLE', 15: 'GREEN', 31: 'TASTE', 16: 'HEALTHY LIVING', 33:
'THE WORLDPOST', 14: 'GOOD NEWS', 41: 'WORLDPOST', 12: 'FIFTY', 0: 'ARTS', 8:
'DIVORCE'}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_text = request.form['article']
        prediction = model.predict([input_text])[0]
        predicted_category = v[prediction]

        return render_template('index.html', prediction=predicted_category, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
