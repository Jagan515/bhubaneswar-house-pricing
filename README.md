# 🏠 Bhubaneswar House Price Prediction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/badge/Pickle-Data%20Serialization-green?logo=database&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask&style=for-the-badge">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML%20Library-orange?logo=scikitlearn&logoColor=white&style=for-the-badge">
</p>

<h3 align="center">An ML project that predicts house prices in Bhubaneswar, Odisha!</h3>
<h5 align="center">The project is built with Python, scikit-learn, and deployed as a web app using Flask and Render.</h5>

<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/View%20Project%20on-Render-purple?logo=render&style=for-the-badge">
  </a>
</p>

<hr>

## 🚀 Project Workflow

1. **Exploratory Data Analysis (EDA)**
   - Visualized feature distributions to detect skewedness and outliers
   - Identified strong correlations between features for feature selection
   - Analyzed Bhubaneswar-specific housing patterns

2. **Data Preprocessing & Feature Engineering**
   - Handled missing values using appropriate imputation techniques
   - Removed outliers using IQR (Interquartile Range) method
   - Normalized data with StandardScaler for consistent feature scaling
   - Addressed capped target variable to prevent bias
   - Created stratified splits for balanced training and testing

3. **Model Development & Cross-Validation**
   - Implemented Linear Regression as baseline model
   - Used K-Fold Cross Validation (5 folds) for robust model evaluation
   - Ensured test data was only used for final evaluation to prevent data leakage
   - Optimized model performance for Bhubaneswar housing market

4. **Model Persistence**
   - Saved the trained pipeline using Pickle for reusability
   - Stored preprocessing scaler for consistent transformations
   - Enabled easy model loading without retraining

5. **Web Application & Deployment**
   - Built user-friendly Flask web interface with range sliders
   - Added input validation to prevent negative predictions
   - Included Bhubaneswar-specific locality information
   - Deployed the model as a Flask app on Render

## 🏙️ Bhubaneswar Housing Features

The model considers these key factors specific to Bhubaneswar:

| Feature | Description |
|---|---|
| **Locality Rank** | Quality tier of area (Nayapalli, Saheed Nagar, Patia, etc.) |
| **River Proximity** | Near Kuakhai River (premium location) |
| **Crime Rate** | Safety index of the neighborhood |
| **Green Area** | Percentage of parks and green spaces |
| **Industrial Area** | Proximity to industrial zones |
| **Pollution Level** | Air quality index in the area |
| **Employment Distance** | Distance to major IT hubs and offices |

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Data Analysis** | Python, NumPy, Pandas, Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn, Linear Regression, K-Fold CV |
| **Preprocessing** | StandardScaler, IQR Outlier Detection, Stratified Split |
| **Backend** | Flask, Pickle, Joblib |
| **Frontend** | HTML5, CSS3, Bootstrap, JavaScript |
| **Deployment** | Render, Gunicorn |

## 📊 Model Performance

- **Mean Absolute Error (MAE):** ₹3.19 lakhs
- **Root Mean Squared Error (RMSE):** ₹4.93 lakhs  
- **R² Score:** 0.67
- **Adjusted R² Score:** 0.65

The linear regression model explains approximately **67% of the variance** in Bhubaneswar housing prices. On average, predictions deviate from actual values by about **₹3-5 lakhs**.

## 🎯 Key Features

### 🔍 **Smart Input Validation**
- Range sliders with predefined limits based on actual data
- Categorical options with detailed descriptions
- Prevents unrealistic inputs that could cause negative predictions

### 🏘️ **Bhubaneswar Context**
- Famous localities integration (Nayapalli, Saheed Nagar, Patia, etc.)
- Local factors like Kuakhai River proximity
- Indian real estate market considerations

### 📱 **User-Friendly Interface**
- Intuitive sliders for numerical inputs
- Dropdowns with locality descriptions
- Real-time prediction updates
- Mobile-responsive design

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/bhubaneswar-house-pricing
cd bhubaneswar-house-pricing
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application locally:**
```bash
python app.py
```

5. **Access the application:**
Open your browser and navigate to `http://localhost:5000`

## 🌐 Deployment

The project is deployed on **Render** for public access.

### Deployment Steps:
1. Connect your GitHub repository to Render
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`
4. Deploy!

👉 [Live Demo](#) *[Add your Render deployment link here]*

## 📁 Project Structure

```
bhubaneswar-house-pricing/
├── app.py                 # Flask application
├── templates/
│   └── index.html        # Main web interface
├── static/               # CSS, JS files (if any)
├── requirements.txt      # Python dependencies
├── bhubaneswar_best_model.pkl    # Trained model
├── bhubaneswar_scaler.pkl        # Preprocessing scaler
└── README.md             # Project documentation
```

## 🤝 Contributing

We welcome contributions to improve this project! 🎉

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please check the [CONTRIBUTING.md](CONTRIBUTING.md) guide for detailed setup, workflow, and guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Dataset inspired by Boston Housing Dataset, adapted for Bhubaneswar context
- Scikit-learn documentation for machine learning implementation
- Flask community for web framework guidance
- Render for deployment platform

## ✍️ Author

**Jagan Pradhan**
- 📧 [jaganp515@gmail.com](mailto:jaganp515@gmail.com)
- 🔗 [LinkedIn](https://linkedin.com/in/jaganpradhan)
- 💻 [GitHub](https://github.com/Jagan515)

---

<div align="center">

**⭐ Don't forget to star this repository if you find it helpful!**

*Built with ❤️ for the Bhubaneswar real estate community*

</div>
