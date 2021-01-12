from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

file="Finalized.pickle"
load_model=pickle.load(open(file,'rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method=="POST":
        GRE_Score = float(request.form["GRE_Score"])
        TOEFL_Score = float(request.form["TOEFL_Score"])
        university_rating = float(request.form["University_rating"])
        sop = float(request.form["SOP"])
        lor = float(request.form["LOR"])
        cgpa = float(request.form["CGPA"])
        is_research = request.form["Research"]
        if is_research == 'yes':
            research = 1
        else:
            research = 0
        result = load_model.predict([[GRE_Score, TOEFL_Score, university_rating, sop, lor, cgpa, research]])
        res={"result":round(result[0],2)}
    return render_template("predict.html",a=res)


if __name__ == "__main__":
    app.run(debug=True)