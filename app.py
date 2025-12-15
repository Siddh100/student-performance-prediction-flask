from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("student_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        previous_marks = float(request.form["previous_marks"])
        assignments_completed = int(request.form["assignments_completed"])

        input_data = np.array(
            [[study_hours, attendance, previous_marks, assignments_completed]])
        result = model.predict(input_data)

        if result[0] == 1:
            prediction = "Student will PASS ✅"
        else:
            prediction = "Student may FAIL ❌"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
