from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def get_delay():

    if request.method=='POST':

        result=request.form
        Property_Type=result['Property-Type']
        beds=result['Beds']
        baths=result['Baths']
        sqft=result['sqft']
        year_built=result['year_built']
        basement=result['Basement']
        exterior_walls=result['exterior_walls']
        roof=result['roof']
        shopping=result['shopping']
        restaurants=result['restaurants']
        groceries=result['groceries']
        nightlife=result['nightlife']
        cafes=result['cafes']
        arts_enterntainment=result['arts_enterntainment']
        beauty_spas=result['beauty_spas']
        active_life=result['active_life']
        num_schools=result['num_schools']
        median_age=result['median_age']
        married=result['married']
        insurance=result['insurance']
        property_tax=result['property_tax']
        tx_year=result['tx_year']
        property_tax=result['property_tax']
        
        lst=[]
        
        lst.append(beds)
        lst.append(baths)
        lst.append(sqft)
        lst.append(Property_Type)
        lst.append(basement)
        lst.append(restaurants)
        lst.append(groceries)
        lst.append(nightlife)
        lst.append(cafes)
        lst.append(shopping)
        lst.append(arts_enterntainment)
        lst.append(beauty_spas)
        lst.append(active_life)
        lst.append(median_age)
        lst.append(married)
        lst.append(property_tax)
        lst.append(insurance)
        lst.append(num_schools)

        if beds == '1' and baths == '1':
        	two_and_two = '1'
        else:
        	two_and_two = '0' 

        lst.append(two_and_two)
        lst.append(int(tx_year) - int(year_built))

        lst.append(exterior_walls)
        lst.append(roof)

        df=pd.DataFrame(lst).T

        loaded_model = joblib.load('houseprediction.pkl')
        prediction = loaded_model.predict(df)

        p=[]

        for i in prediction:
        	i=round(int(i),-3)
        	s=str(i)
        	s1=s[:2]
        	p.append(s1)
        	prediction=np.asarray(p)
    return render_template('prediction.html',prediction=prediction)

    
if __name__ == '__main__':
    app.debug = True
    app.run()