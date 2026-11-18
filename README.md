🍷 Wine Quality Prediction using ANN



📌 Project Overview



This project predicts wine quality based on its physicochemical properties using an Artificial Neural Network (ANN).



A Streamlit web application is developed to allow users to enter wine characteristics and get a predicted quality score.



🎯 Project Objectives



\- Predict wine quality using ANN.

\- Understand Deep Learning regression.

\- Apply data preprocessing and feature scaling.

\- Build an interactive web application using Streamlit.



🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- TensorFlow / Keras

\- Scikit-learn

\- Matplotlib

\- Streamlit

\- Joblib

\- Jupyter Notebook



📊 Dataset Information



\- Dataset: Red Wine Quality

\- Total Records: 1143

\- Input Features: 11

\- Target Variable: Quality



🧠 Model Architecture



\- Input Layer: 11 features

\- Hidden Layer 1: 64 neurons (ReLU)

\- Hidden Layer 2: 32 neurons (ReLU)

\- Output Layer: 1 neuron

\- Optimizer: Adam

\- Loss Function: Mean Squared Error (MSE)

\- Early Stopping: Used to reduce unnecessary training.



📈 Model Performance



Metric| Result

MAE| 0.50727

R2 Score| 0.140838



The model achieved an MAE of 0.50727 on the test dataset.



🚀 How to Run the Project



1\. Clone this repository.

2\. Install the required libraries:



pip install -r requirements.txt



3\. Run the Streamlit application:



python -m streamlit run app/app.py



4\. Enter wine details and click on Predict Wine Quality.



📁 Project Structure



Wine-Quality-Prediction-ANN/

│

├── app/

│   └── app.py

│

├── data/

│   └── winequality-red.csv

│

├── models/

│   ├── wine\_quality\_model.keras

│   └── wine\_quality\_scaler.pkl

│

├── notebooks/

│   └── Wine\_Quality\_ANN.ipynb

│

├── requirements.txt

├── .gitignore

└── README.md



👩‍💻 Project Type



Deep Learning | Regression | Artificial Neural Network



📌 Conclusion



This project demonstrates how Artificial Neural Networks can be used for wine quality prediction and how a trained model can be deployed using Streamlit.

