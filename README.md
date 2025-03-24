
# 💎 Diamond Price Prediction System

This project predicts the price of diamonds based on various attributes such as **carat, cut, color, clarity, depth, and table**. The model is trained using machine learning algorithms, and a web interface is built with **Streamlit**.

## 📚 **Project Overview**
- **Goal:** Predict diamond prices using a regression model.
- **Tech Stack:**
  - Python
  - Pandas, NumPy, Matplotlib, Plotly
  - Scikit-learn
  - Streamlit (for web UI)
  - PCA (for dimensionality reduction)

## 📊 **Dataset**
- Dataset used: Processed diamond dataset stored in `artifacts/processed_test_data.csv`.
- Features:
  - `carat`, `cut`, `color`, `clarity`, `depth`, `table`
- Target:
  - `price`

## ⚙️ **Model Pipeline**
1. **Data Preprocessing:** Cleaning, encoding, and feature scaling.
2. **Model Training:** Random Forest Regressor (or selected model).
3. **PCA Analysis:** Applied to visualize data in 2D space.
4. **Web Interface:** User inputs values and gets predictions.

## 🚀 **How to Run the Project**
### 1. Clone the Repository
```bash
git clone https://github.com/bhavin2004/Diamond-Price-Prediction.git
cd Diamond-Price-Prediction
```

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv
# Activate on Windows
venv\Scripts\activate
# Activate on Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Streamlit App
```bash
streamlit run app.py
```

## 🎯 **PCA Visualization**
- PCA is used to reduce high-dimensional data and display **PCA Component 1** and **PCA Component 2**.
- Visuals display transformed data trends.

## 📂 **Project Structure**
```
📦 Diamond-Price-Prediction
├── 📂 artifacts
│   ├── model.pkl
│   └── processed_test_data.csv
├── 📂 src
│   ├── exception.py
│   ├── logger.py
│   ├── prediction_pipeline.py
│   └── training_pipeline.py
├── app.py
├── requirements.txt
└── README.md
```

## 📈 **Model Evaluation**
- Metrics used: RMSE, MAE, R-squared
- PCA used for performance visualization

## 📝 **Future Scope**
- Add more advanced models for higher accuracy.
- Enhance Streamlit UI with dynamic graphs.
- Implement deployment using AWS or Docker.
