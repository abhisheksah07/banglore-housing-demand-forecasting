# 🏠 Bangalore House Price Prediction

This project predicts real estate prices in Bangalore based on features such as location, square footage, number of bathrooms, and BHK (bedrooms, halls, and kitchens). It uses Python for data preprocessing, exploratory data analysis (EDA), linear regression modeling, and deployment using Flask API.

---

## 📁 Project Structure

```
bangalore-house-price-prediction/
│
├── data/                      # Raw & cleaned CSV datasets
│   └── bangalore.csv
│
├── notebooks/                 # Jupyter Notebooks for EDA and model building
│   ├── eda.ipynb
│   └── model_building.ipynb
│
├── model/                     # Saved model and column data
│   ├── bangalore_home_prices_model.pkl
│   └── columns.json
│
├── client/                    # UI (HTML, CSS, JS) - optional Flask frontend
│
├── server/                    # Flask backend (API)
│   └── server.py
│
├── README.md                  # Project documentation
└── requirements.txt           # All required libraries
```

---

## 📌 Features

* Clean and preprocess real estate data
* Remove outliers and inconsistencies
* Visualize housing trends by location, sqft, and BHK
* Build and evaluate a Linear Regression model
* Save model using Pickle and deploy with Flask
* REST API for real-time price prediction

---

## 💠 Tech Stack

* **Languages:** Python
* **Libraries:** pandas, NumPy, matplotlib, seaborn, scikit-learn
* **Model:** Linear Regression (GridSearchCV for optimization)
* **Deployment:** Flask API

---

## 📊 Visualizations Included

* Top 10 expensive localities by avg price/sqft
* Scatter plots comparing 2BHK and 3BHK prices
* Outlier detection using sqft and bathroom filters
* Price distribution and residual error plots

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/bangalore-house-price-prediction.git
cd bangalore-house-price-prediction
```

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

### 3. Run Jupyter Notebooks

```bash
jupyter notebook notebooks/eda.ipynb
```

### 4. Start the Flask Server

```bash
cd server
python server.py
```

---

## 📈 Sample Prediction (via API)

Once Flask server is running, use a tool like Postman or curl:

```json
POST /predict_home_price

{
  "location": "Whitefield",
  "total_sqft": 1500,
  "bath": 3,
  "bhk": 3
}
```

Response:

```json
{
  "estimated_price": 92.3
}
```

---

## 🧐 Future Improvements

* Integrate other regression models (Lasso, RandomForest)
* Build Streamlit or React frontend for users
* Use geolocation clustering for more precise predictions
* Add live pricing updates via web scraping

---

## 👤 Author

**Abhishek Sah**
📧 [asah71513@gmail.com](mailto:asah71513@gmail.com)
📞 +91-9004432877
🔗 [LinkedIn](https://linkedin.com/in/abhisheksah25)
💻 [GitHub](https://github.com/abhisheksah07)

---

## ⭐️ Show Your Support

If you like this project, please ⭐️ the repo and share it. Your support helps me build more cool stuff!
