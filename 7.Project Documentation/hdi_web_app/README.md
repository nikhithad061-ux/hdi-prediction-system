# Human Development Index (HDI) Predictor Web App

A modern, responsive Flask web application that predicts the Human Development Index (HDI) of a country or region based on key socio-economic indicators using Machine Learning (Linear Regression).

## 🌟 Features
- **Sleek UI**: Built with glassmorphism, responsive grid layout, and dark-mode styling.
- **Real-Time HDI Prediction**: Evaluates Life Expectancy, Expected Schooling, Mean Schooling, and GNI per Capita.
- **Visual Gauge & Classification**: Visualizes the predicted HDI score on a 0.0000 – 1.0000 gauge bar with developmental tier categorization (Very High, High, Medium, Low).
- **Production Ready**: Configured with `Procfile` and `requirements.txt` for deployment on platforms like Render, Heroku, or Railway.

---

## 📁 Project Structure

```
hdi_web_app/
│
├── app.py              # Main Flask Application
├── hdi_model.pkl       # Pre-trained Scikit-Learn Model
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment process file
├── runtime.txt         # Python runtime environment version
│
├── templates/
│   └── index.html      # Jinja2 HTML layout
│
└── static/
    └── css/
        └── style.css   # Custom styling and animations
```

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/hdi_web_app.git
   cd hdi_web_app
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 📊 Model & Input Parameters

- **Life Expectancy at Birth**: Range 20 – 85 years
- **Expected Years of Schooling**: Range 0 – 20 years
- **Mean Years of Schooling**: Range 0 – 15 years
- **GNI per Capita (PPP $)**: Range 100 – 75,000+

---

## 🚀 Deploying to Render.com

1. Push your code to GitHub.
2. Log into [Render.com](https://render.com) and click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Set the following configuration:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click **Create Web Service**. Render will automatically build and deploy your app!

