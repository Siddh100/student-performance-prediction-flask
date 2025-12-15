import joblib
import numpy as np

# Load model
model = joblib.load("student_model.pkl")

print("Enter student details:")

study_hours = float(input("Study hours per day: "))
attendance = float(input("Attendance percentage: "))
previous_marks = float(input("Previous marks: "))
assignments_completed = int(input("Assignments completed: "))

input_data = np.array(
    [[study_hours, attendance, previous_marks, assignments_completed]])

prediction = model.predict(input_data)

if prediction[0] == 1:
    print("Prediction: Student will PASS ✅")
else:
    print("Prediction: Student may FAIL ❌")
