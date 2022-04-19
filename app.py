from flask import Flask , request , render_template
import pickle


# loading the envirenmental variables 
def load(path):
    with open(path,'rb') as f : 
        var = pickle.load(f)
    return(var)

le_r = load('./le_r.pickle')
le_s = load('./le_s.pickle')
le_sm = load('./le_sm.pickle')
model = load('./model.pickel')



# flask app 


# to run this program open your CMD.exe and cd into the folder 
# type in your cmd :   python app.exe     
# open your browser and open 127.0.0.1:5000

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def intro():
    # the template in a state of submitting
    if request.method =="POST":
        #if the fields are filled when submitting
        if request.form["age"] and request.form["sex"] and request.form["bmi"] and request.form["children"] and request.form["smoker"] and request.form["region"]:
            # getting the features and processing them
            age = float(request.form["age"])
            sex = le_s.transform([request.form["sex"]])
            bmi = float(request.form["bmi"])
            children = float(request.form["children"])
            smoker = le_sm.transform([request.form["smoker"]])
            region = le_r.transform([request.form["region"]])

            # creating the feature
            X = [[age,sex,bmi,children,smoker,region]]
            # predicting the charges
            pred = model.predict(X)[0]
            # open the template using the variables
            return render_template('base.html', pred=str(pred))
    # the template in initial state
    return render_template('base.html')




if __name__ == "__main__" :
    app.run(debug=True)
