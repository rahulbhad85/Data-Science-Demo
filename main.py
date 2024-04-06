from flask import Flask , request ,render_template
import pickle



app = Flask(__name__)


@app.route("/")
def function():
    return render_template ("index.html")

@app.route ('/function_to_pull_data', methods=["post"])

def my_model_prediction():
    
    model = pickle.load(open(r'Project-House-Price-new.pkl', "rb"))
    
    
    data = request.form
    print(data)
    
    
    user_input = [[float(data['Avg. Area Income'])
                   ]]
    
    print(user_input)
    
    
    result = model.predict(user_input)
    print(result)
    
    a = str(result[0])
    
    return render_template("result.html", predictions_result = a )




if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=False, port=8080)
    
    #  Bigmart Store Location is in ==  {{predictions_result}}