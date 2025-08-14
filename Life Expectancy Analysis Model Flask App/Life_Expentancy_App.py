from flask import Flask, render_template, request
import joblib

# Load model
model, feature_names = joblib.load("life_expectancy_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", feature_names=feature_names)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form inputs in correct order
    input_values = [float(request.form[feat]) for feat in feature_names]
    prediction = model.predict([input_values])[0]
    return render_template("index.html", feature_names=feature_names,
                           prediction_text=f"Predicted Life Expectancy: {prediction:.2f} years")

if __name__ == "__main__":
    app.run(debug=True)
