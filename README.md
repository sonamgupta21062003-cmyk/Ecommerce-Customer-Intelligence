# Ecommerce-Customer-Intelligence

##  Tech Stack & Skills

###  Programming & Database
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![SQL](https://img.shields.io/badge/SQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

### Data Analytics & Visualization
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

###  Machine Learning & Prediction
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)![Machine Learning](https://img.shields.io/badge/Machine%20Learning-8A2BE2?style=flat-square)![Profit Prediction](https://img.shields.io/badge/Profit%20Prediction-16A34A?style=for-the-badge)![Feature Engineering](https://img.shields.io/badge/Feature%20Engineering-DB2777?style=flat-square)

###  Dashboard & Deployment
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

###  Data Preparation & Business Intelligence
![Data Cleaning](https://img.shields.io/badge/Data%20Cleaning-0891B2?style=flat-square)![EDA](https://img.shields.io/badge/EDA-6366F1?style=flat-square)![KPI Analysis](https://img.shields.io/badge/KPI%20Analysis-CA8A04?style=flat-square)![Business Insights](https://img.shields.io/badge/Business%20Insights-0D9488?style=flat-square)

# Ecommerce Customer Intelligence

An end-to-end e-commerce analytics and customer intelligence project that combines data analysis, business intelligence, and machine learning to explore sales performance and predict profit.

## Project Overview

Analyze Sales & Revenue Performance — Track total revenue, profit, order volume, average order value, and profit margins to evaluate overall business performance.

Monitor Profitability & Margins — Identify profitable products and categories, compare revenue against profit, and understand the key drivers of business profitability.

Discover Sales Trends & Patterns — Analyze monthly sales performance and identify changes in revenue, profit, and customer purchasing behavior.

Evaluate Regional & Category Performance — Compare business performance across geographical regions and product categories to uncover growth opportunities.

Identify Top-Performing Products — Rank products by revenue, profit, and sales volume to support product-level business decisions.

Understand Product Returns — Examine return rates and return reasons to identify potential issues affecting customer satisfaction and profitability.

Build a Machine Learning Profit Predictor — Develop a predictive pipeline to estimate profit based on supported input features and explore potential business scenarios.

Perform Data Analysis Using Python — Apply data cleaning, exploratory data analysis (EDA), statistical analysis, and hypothesis testing to extract meaningful insights.

Leverage SQL for Business Intelligence — Query, join, validate, and aggregate relational data to answer business questions and calculate key performance indicators.

Develop an Interactive Power BI Dashboard — Present key metrics and business trends through visualizations, KPI cards, and interactive filters for effective reporting.

Create a Streamlit Analytics Application — Provide an interactive interface for exploring business data, filtering results, reviewing insights, and using the profit prediction functionality.

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
