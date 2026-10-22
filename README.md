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

## SQL Insights

##  SQL Analysis & Business Intelligence

SQL was used to transform relational e-commerce data into meaningful business insights. The analysis focuses on data quality validation, sales performance, profitability, customer behavior, product performance, and return trends using MySQL.

### Key SQL Tasks

-  **Relational Data Modeling & Joins** — Connected Customers, Products, Orders, OrderDetails, and Returns tables using primary keys, foreign keys, and multi-table joins.

-  **Data Quality & Validation** — Checked duplicate records, missing values, and orphan records to validate data consistency and referential integrity.

-  **Revenue & Profit Analysis** — Calculated total revenue, total profit, average order value (AOV), and category-level profit margins for delivered orders.

-  **Sales Trend Analysis** — Analyzed monthly revenue trends to understand changes in business performance over time.

-  **Regional Performance Analysis** — Compared revenue and profit across customer regions to identify high-performing markets.

-  **Product Performance Analysis** — Identified the top 10 products by revenue, units sold, and profit.

-  **Customer Revenue Analysis** — Ranked the top 10 customers by revenue and profit to understand customer-level business contribution.

-  **Payment Method Analysis** — Compared order volumes across payment methods.

-  **Product Return Analysis** — Examined return reasons and calculated the overall return rate to identify potential areas for improvement.

### SQL Concepts Applied

`SELECT` · `WHERE` · `GROUP BY` · `HAVING` · `ORDER BY` · `JOIN` · `LEFT JOIN` · `COUNT` · `SUM` · `AVG` · `MIN` · `MAX` · `COUNT(DISTINCT)` · Aggregate Functions · Primary Keys · Foreign Keys · Data Validation

###  Business Value

The SQL analysis provides a structured foundation for understanding sales performance, identifying profitable products and regions, comparing customer contributions, and monitoring product returns. These insights complement the Python analysis and Power BI dashboard to support data-driven business decisions.

###  SQL File
- **Database:** MySQL
- **Tables:** Customers, Products, Orders, OrderDetails, Returns

### POWER BI Insights

## 📊 Power BI Dashboard & Business Intelligence

Developed an interactive **E-commerce Performance Dashboard** using Microsoft Power BI to monitor sales performance, analyze profitability, evaluate product and regional performance, and identify business trends through data-driven visualizations.

### 🎯 Key Dashboard Features

- 💰 **Revenue & Profit Tracking** — Monitor total revenue, total profit, and profit margin to evaluate overall business performance.

- 🛒 **Sales KPI Monitoring** — Track total orders and average order value (AOV) through KPI cards for quick performance assessment.

- 📈 **Revenue & Profit Trends** — Analyze monthly performance to identify sales patterns, fluctuations, and changes in profitability.

- 🛍️ **Category-Wise Analysis** — Compare revenue across product categories to identify major contributors to sales.

- 🌍 **Regional Performance Analysis** — Evaluate revenue across geographical regions to understand market performance.

- 🏆 **Top 10 Products by Revenue** — Identify leading products based on revenue contribution and compare their relative performance.

- 🔄 **Return Reason Analysis** — Examine return reasons to identify recurring issues that may affect customer satisfaction and business performance.

- 🎛️ **Interactive Dashboard Filters** — Explore the data using slicers for date, region, category, and payment method.

### 🧰 Power BI Skills Applied

- Data visualization and dashboard design
- KPI development and business performance monitoring
- Data modeling and relationship management
- DAX measures and calculated metrics
- Power Query data transformation
- Interactive slicers and cross-filtering
- Sales, profitability, and product performance analysis

### 💡 Business Insights

The dashboard provides a consolidated view of e-commerce performance, helping users compare revenue and profit trends, identify high-performing categories and products, evaluate regional sales, and investigate return reasons.

### 🖥️ Dashboard Preview

<img width="1325" height="742" alt="image" src="https://github.com/user-attachments/assets/9bdef31e-2fd8-4e04-9002-8577a0debf2c" />


**Tools Used:** Microsoft Power BI · Power Query · DAX · Data Modeling · Data Visualization


## PYTHON Aplied

## 🐍 Python Analytics & Machine Learning

Python serves as the analytical foundation of this project, enabling data preparation, exploratory data analysis, statistical investigation, business performance analysis, and machine learning-based profit prediction.

### 🎯 Key Python Tasks

- 🧹 **Data Cleaning & Preprocessing** — Prepare e-commerce data for analysis by handling data quality issues and organizing datasets for downstream workflows.

- 🔍 **Exploratory Data Analysis (EDA)** — Investigate sales patterns, customer behavior, product performance, and business trends using structured data analysis.

- 📊 **Business Performance Analysis** — Analyze revenue, profit, order value, product categories, and regional performance to uncover actionable insights.

- 🧪 **Statistical Hypothesis Testing** — Apply statistical testing to investigate business-related questions and evaluate evidence for potential differences or relationships in the data.

- 🤖 **Machine Learning for Profit Prediction** — Build a predictive modeling workflow to estimate profit using the features supported by the trained model.

- ⚙️ **Model Evaluation & Persistence** — Store the trained prediction pipeline and model evaluation information for reuse in the Streamlit application.

- 📈 **Data Visualization** — Use analytical visualizations to explore patterns and communicate findings clearly.

- 🔗 **Analytics Integration** — Prepare analytical outputs and model artifacts for integration with the Power BI dashboard and Streamlit application.

### 🧰 Python Libraries & Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

### 📂 Python Analysis Files

| File | Purpose |
|---|---|
| `EDA on Ecommerce.ipynb` | Exploratory data analysis |
| `Ecommerce Analystics.ipynb` | E-commerce business analytics |
| `hypothesis testing.ipynb` | Statistical hypothesis testing |
| `04_Python/` | Python analysis and machine learning workflows |

### 💡 Business Value

Python connects data analysis with predictive analytics, helping transform raw e-commerce data into meaningful business insights and supporting profit estimation through a reusable machine learning pipeline.

### ML Algorothm Overview

## 🤖 Machine Learning & Profit Prediction

This project integrates Machine Learning into e-commerce analytics to estimate product-level profit and support data-driven business decisions. A trained prediction pipeline is saved for reuse within the interactive Streamlit application.

### 🎯 Machine Learning Objectives

- 💰 **Profit Prediction** — Estimate profit using the input features supported by the trained model.
- ⚙️ **Data Preprocessing** — Prepare input features in the format required by the prediction pipeline.
- 🧠 **Predictive Modeling** — Train a regression model to learn patterns between input variables and numerical profit values.
- 📊 **Model Evaluation** — Evaluate predictive performance using appropriate regression metrics.
- 📦 **Model Persistence** — Save the trained pipeline using Joblib for reuse without retraining every time the application runs.
- 🌐 **Application Integration** — Connect the trained model with Streamlit to make profit predictions accessible through an interactive interface.

### 🔬 Machine Learning Workflow

```text
Raw E-commerce Data
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Selection & Preparation
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Save Trained Pipeline
        ↓
Streamlit Profit Prediction
```

###  Algorithm & Modeling Approach

**Problem Type:** Supervised Learning — Regression

The objective is to predict a continuous numerical value: profit.

The exact algorithm should be documented according to the model stored in the trained pipeline.

###  Model Evaluation

Regression models can be evaluated using the following metrics, where applicable:

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted profit.
- **RMSE (Root Mean Squared Error):** Measures prediction error while penalizing larger errors more heavily.
- **R² Score:** Indicates how much of the variation in the target is explained by the model.

Actual metric values should be reported from the project's saved evaluation results.

## 🚀 Deployment & Execution

The E-Commerce Customer Intelligence project is designed to combine data analytics, machine learning, and interactive visualization in a unified workflow. The Streamlit interface provides a user-friendly way to explore insights and access the profit prediction functionality.

### 🛠️ Deployment Workflow

- **Data Layer:** Cleaned e-commerce data prepared for analysis.
- **Analytics Layer:** Python and SQL for data processing and business insights.
- **Visualization Layer:** Power BI dashboard for interactive business reporting.
- **Machine Learning Layer:** Trained pipeline for profit prediction.
- **Application Layer:** Streamlit interface for interactive exploration and predictions.

## 🚀 Deployment & Execution

The E-Commerce Customer Intelligence project is designed to combine data analytics, machine learning, and interactive visualization in a unified workflow. The Streamlit interface provides a user-friendly way to explore insights and access the profit prediction functionality.

### 🛠️ Deployment Workflow

- **Data Layer:** Cleaned e-commerce data prepared for analysis.
- **Analytics Layer:** Python and SQL for data processing and business insights.
- **Visualization Layer:** Power BI dashboard for interactive business reporting.
- **Machine Learning Layer:** Trained pipeline for profit prediction.
- **Application Layer:** Streamlit interface for interactive exploration and predictions.

###  Run Locally

## 🌐 How to Use the Live Application

1. **Open the Live App:** Click the deployed application link to access the project directly in your web browser.
2. **Explore the Dashboard:** View interactive visualizations and key e-commerce business insights.
3. **Analyze Business Performance:** Explore available sales, revenue, customer, product, and profitability insights.
4. **Predict Profit:** Navigate to the profit prediction section and enter the required input values.
5. **Generate Prediction:** Click the prediction button to obtain the model's estimated profit.
6. **Explore the Results:** Review the displayed prediction and available visualizations to understand business performance.

**No local installation is required to use the live application.** Simply open the deployed link in your browser.

> Note: The features available depend on the deployed version of the application.

### 📊 Power BI Dashboard

Open the Power BI `.pbix` file in Power BI Desktop to explore the interactive dashboard and business performance insights.

### 🔐 Configuration & Requirements

- Python and the dependencies listed in the project requirements file.
- MySQL configuration, if running the SQL database workflow.
- Trained model artifacts, if required by the prediction application.
- Power BI Desktop to view the dashboard.

> **Note:** Local execution instructions are provided here. Add a public live-demo link only after the application has been successfully deployed and tested.

### 💻 Run Locally

**1. Clone the repository**
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Ecommerce-Customer-Intelligence
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**

Use the requirements file that contains your Streamlit application's dependencies:

```bash
pip install -r 05_Streamlit_App/requirements-app.txt
```

**4. Launch the Streamlit application**

```bash
streamlit run path/to/your_app.py
```

Replace `path/to/your_app.py` with the actual path to your Streamlit entry-point file.

### 📊 Power BI Dashboard

Open the Power BI `.pbix` file in Power BI Desktop to explore the interactive dashboard and business performance insights.

### 🔐 Configuration & Requirements

- Python and the dependencies listed in the project requirements file.
- MySQL configuration, if running the SQL database workflow.
- Trained model artifacts, if required by the prediction application.
- Power BI Desktop to view the dashboard.

> **Note:** Local execution instructions are provided here. Add a public live-demo link only after the application has been successfully deployed and tested.

###  Model Artifacts

| File | Purpose |
|---|---|
| `profit_prediction_pipeline.joblib` | Saved machine learning pipeline |
| `model_metadata.json` | Model metadata and configuration |
| `model_metrics.csv` | Stored model evaluation metrics |

###  Business Value

The predictive component complements historical sales and profitability analysis by allowing users to explore estimated profit under different supported input scenarios. It connects analytical insights with an interactive application for practical business exploration.

### STREAMLIT APlied

## 🌐 Interactive Streamlit Application

Built an interactive web application using **Streamlit** to bring e-commerce analytics and machine learning-based profit prediction into a single, user-friendly interface. The application is designed to help users explore business performance, understand key metrics, and generate profit estimates using a trained machine learning pipeline.

### 🚀 Key Application Features

- 📊 **Interactive Analytics Dashboard** — Present e-commerce performance metrics and business insights through an interactive interface.

- 💰 **Profit Prediction Interface** — Allow users to enter supported input values and generate profit estimates using the saved machine learning pipeline.

- 🎛️ **Dynamic User Inputs** — Use interactive controls to explore different input scenarios and understand their predicted outcomes.

- 📈 **Data Visualization** — Display analytical results and business trends through clear, easy-to-understand charts.

- 🤖 **Machine Learning Integration** — Load the trained prediction pipeline and use it to generate predictions without retraining the model for every request.

- ⚙️ **Reusable Model Artifacts** — Organize the trained pipeline, model metadata, and evaluation metrics for application use.

- 🧭 **User-Friendly Interface** — Organize analytics and prediction workflows to make the application easier to navigate.

### 🛠️ Technologies Used

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-4B5563?style=for-the-badge)

### 🔄 Application Workflow

```text
User Opens Streamlit App
          ↓
Explore E-commerce Analytics
          ↓
Enter Prediction Inputs
          ↓
Load Trained ML Pipeline
          ↓
Generate Profit Estimate
          ↓
Display Prediction & Insights
```

###  Business Value

The Streamlit application connects data analytics with predictive modeling in an accessible interface. It helps users explore historical business performance and test supported scenarios using profit estimates generated by the trained model.

###  Run the Application Locally


**Framework:** Streamlit  
**Language:** Python  
**ML Integration:** Scikit-learn and Joblib  
**Purpose:** Interactive E-commerce Analytics & Profit Prediction




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
