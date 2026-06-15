# Customer Churn Analysis  

## 📌 Project Overview  
This project analyzes customer churn for a telecom company using Python. It involves data manipulation, visualization, and predictive modeling to identify factors contributing to churn and help improve customer retention.  

## 📊 Dataset  
The dataset contains customer details such as tenure, monthly charges, contract type, payment method, and churn status.  

## 🛠️ Technologies Used  
- Python  
- Pandas & NumPy (Data Manipulation)  
- Matplotlib & Seaborn (Data Visualization)  
- Scikit-learn (Machine Learning)  

## 📌 Tasks Performed  
1. **Data Manipulation**  
   - Extracted specific columns and filtered records based on conditions.  
   - Counted churn occurrences.  

2. **Data Visualization**  
   - Created bar plots, histograms, scatter plots, and box plots.  

3. **Predictive Modeling**  
   - **Linear Regression**: Predicted `MonthlyCharges` based on `tenure`.  
   - **Logistic Regression**: Predicted `Churn` based on `MonthlyCharges` and `tenure`.  
   - **Decision Tree**: Classified customers based on `tenure`.  
   - **Random Forest**: Improved classification accuracy using `tenure` and `MonthlyCharges`.  

## 🚀 How to Run  
1. Clone the repository:  
   ```bash
   git clone <repository_url>

Install dependencies:

 pip install pandas numpy matplotlib seaborn scikit-learn
 pip install -r requirements.txt
 
Run the Jupyter Notebook or Python script.






Run the app:

streamlit run app.py






📌 Results
Identified key factors influencing churn.
Achieved a good accuracy score with Random Forest.


# Customer Churn Prediction App

A **Streamlit web app** that predicts customer churn using a **Random Forest model**.

## 🔗 Live Demo
[Try the app here](https://customer-churn-test.streamlit.app/)

## 📂 Features
- Single customer prediction (input `Tenure` and `Monthly Charges`).
- Batch prediction (upload a CSV file).
- Displays churn probability.

## 🛠️ How to Run Locally
1. Clone this repo:
   ```bash
   git clone https://github.com/surendiran-20cl/Customer-Churn.git

📩 Contact
For queries, reach out via [surendiran.shanmuga@gmail.com].
