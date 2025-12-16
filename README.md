# 🎓 Student Performance Prediction using Machine Learning

This project predicts whether a student will **Pass or Fail** based on academic and behavioral parameters using **Machine Learning** and deploys the model using a **Flask web application**.

---

## 📌 Project Overview

The system takes student-related inputs such as:
- Study hours per day
- Attendance percentage
- Previous academic marks
- Assignments completed

Using these inputs, a **Logistic Regression** model predicts the student’s academic outcome.

---

## 🧠 Machine Learning Details

- **Type of Learning:** Supervised Learning  
- **Algorithm Used:** Logistic Regression  
- **Evaluation Metric:** Accuracy Score  
- **Output Classes:**  
  - `1` → Pass  
  - `0` → Fail  

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML & CSS

---

## 📁 Project Structure

Student-Performance-Flask/
│
├── student_data.csv
├── train_model.py
├── student_model.pkl
├── app.py
├── requirements.txt
│
├── templates/
│ └── index.html
│
└── static/
└── style.css


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/USERNAME/student-performance-prediction-flask.git
cd student-performance-prediction-flask

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Train the Model
python train_model.py

4️⃣ Run the Flask App
python app.py


Open browser and go to:

http://127.0.0.1:5000

🖥️ Web Application Features

User-friendly input form

Real-time prediction

ML model integrated with backend

Simple and clean UI

📊 Sample Input
    Feature	               Value
    Study_Hours 	         5
    Attendance	            75
    Previous_Marks	        60
    Assignments_Completed	 5

Prediction: Student will PASS ✅

🚀 Future Enhancements

Multi-class prediction (Excellent / Good / Average)

Student dashboard

Database integration

Deployment on cloud platforms (Render / Heroku)

👨‍🎓 Academic Use

This project is suitable for:

Minor Project

Machine Learning Lab

AI/ML Coursework

Flask Deployment Practice

📜 License

This project is for educational purposes only.