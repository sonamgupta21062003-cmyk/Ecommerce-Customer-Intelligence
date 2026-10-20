# Ecommerce-Customer-Intelligence
End-to-end e-commerce analytics using Python, SQL, Power BI, and Machine Learning, with an interactive Streamlit dashboard and profit prediction.
# Ecommerce Customer Intelligence

An end-to-end e-commerce analytics and customer intelligence project that combines data analysis, business intelligence, and machine learning to explore sales performance and predict profit.

## Project Overview

This project transforms e-commerce data into actionable business insights through Python-based analysis, SQL queries, Power BI visualizations, and an interactive Streamlit application.

## Key Features

- Interactive Streamlit dashboard with data filters
- E-commerce sales and business performance analysis
- Profit calculator and machine learning profit predictor
- Data analysis and exploratory data analysis using Python
- SQL queries for data analysis
- Power BI dashboard for business reporting
- Exportable filtered data and analysis results

## Technology Stack

- **Python:** Pandas, NumPy
- **Visualization:** Plotly, Power BI
- **Machine Learning:** Scikit-learn
- **Application:** Streamlit
- **Model Persistence:** Joblib
- **Database & Querying:** SQL
- **Development Tools:** VS Code, Jupyter Notebook, Git, GitHub

## Project Structure

```text
Ecommerce-Customer-Intelligence/
├── 04_Python/
├── 05_Streamlit_App/
│   ├── app.py
│   ├── requirements.txt
│   └── artifacts/
│       ├── model_metadata.json
│       ├── model_metrics.csv
│       └── profit_prediction_pipeline.joblib
├── ecommerce_clean_data.csv
├── ecommerce Dashboard.pbix
├── EDA on Ecommerce.ipynb
├── hypothesis testing.ipynb
├── Ecommerce Analystics.ipynb
├── SQL Work.sql
└── .gitignore
```

*The structure above highlights the main project files; additional files may be present.*

## Run the Streamlit Application Locally

1. Clone this repository.
2. Open a terminal in the project directory.
3. Create and activate a Python virtual environment.
4. Install the app dependencies.
5. Launch Streamlit.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies and launch the app:

```bash
pip install -r 05_Streamlit_App/requirements.txt
streamlit run 05_Streamlit_App/app.py
```

## Machine Learning

The project includes a saved profit prediction pipeline and model metadata. Predictions depend on the input features and the trained model.

## Business Value

The project is designed to help explore sales patterns, compare business performance, examine customer and product trends, and estimate profit under different input scenarios.

## Future Improvements

- Add an Excel dashboard
- Deploy the Streamlit application publicly
- Add further model evaluation and explainability
- Improve documentation with dashboard screenshots

## Author

**Sonam Gupta**

GitHub: [sonamgupta21062003-cmyk](https://github.com/sonamgupta21062003-cmyk)

LinkedIn: [Sonam Gupta](https://www.linkedin.com/in/sonam-gupta-a5a9b6402/)
