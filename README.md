# 🏠 Boston House Pricing Prediction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/badge/Pickle-Data%20Serialization-green?logo=database&logoColor=white&style=for-the-badge">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask&style=for-the-badge">
</p>

<h3 align="center">An ML project that predicts house prices in the Boston area!</h3>
<h5 align="center">The project is built with Python, scikit-learn, and deployed as a web app using Flask and Render.</h5>

<p align="center">
  <a href="https://bostonhousepricing-pxxt.onrender.com/">
    <img src="https://img.shields.io/badge/View%20Project%20on-Render-purple?logo=render&style=for-the-badge">
  </a>
</p>

<hr>

## 🚀 Project Workflow

1. **Exploratory Data Analysis (EDA)**
   - Visualized feature distributions to detect skewedness and outliers.
   - Identified strong correlations between features for feature selection.

2. **Feature Engineering**
   - Normalized data with StandardScaler to prevent more dominant features from having a strong influence during training.
   - Created a pipeline to streamline preprocessing and model training.

3. **Linear Regression Model**
   - Used linear regression as the baseline predictive model due to its interpretability and simplicity.
   - Trained baseline linear regression model on standardized features for better performance. 

4. **Model Persistence**
   - Saved the trained pipeline using Pickle for reusability, so the model can be easily loaded later without retraining.

5. **Deployment**
   - Deployed the model as a Flask app on Render, so that users can interact with the model via web app and/or API.
   - Exposed an API endpoint to predict house prices, enabling integration with other applications and real-time predictions for end-users. 

## 🛠️ Tech-Stack

| Layer | Tech |
|---|---|
| Data Analysis | [Python](https://www.python.org/), [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/), [Scikit-learn](https://scikit-learn.org/) |
| Backend | Python, [Pickle](https://docs.python.org/3/library/pickle.html) |
| Version Control | Git, Github |
| Deployment | [Render](https://render.com/) |

## ⚙️ Getting Started:

Clone the repository:

```bash
git clone https://github.com/Jagan515/BostonHousePricing
cd BostonHousePricing
````

Create a virtual environment (with conda):

```bash
conda create -p venv python==3.13 -y
conda activate venv/
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app locally:

```bash
python app.py
```

## 📊 Results + Model Performance

- **Mean Absolute Error (MAE):** 3.19  
- **Root Mean Squared Error (RMSE):** 4.93  
- **R² Score:** 0.67  

The linear regression model explains approximately **67% of the variance** in housing prices. On average, predictions deviate from the actual values by about **3–5** units.

While this provides a solid baseline, further improvements can be achieved by utilizing advanced models, such as **Random Forests** or **Gradient Boosting**, along with feature engineering and cross-validation.

<hr>

## 🌐 Deployment

The project is deployed on **Render**.
👉 [Live Demo](https://bostonhousepricing-pxxt.onrender.com/)

## 🤝 Contributing
We welcome contributions to make this project better! 🎉  

Please check the [CONTRIBUTING.md](CONTRIBUTING.md) guide for setup, workflow, and guidelines.  

## ✍️ Author

**Jagan Pradhan**
📧 [jaganp515@egmail.com](mailto:jaganp515@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/jaganpradhan) | [GitHub](https://github.com/Jagan515)

