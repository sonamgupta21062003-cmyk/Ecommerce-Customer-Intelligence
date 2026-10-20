
from pathlib import Path
import json
import warnings

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


# ==========================================================
# 1. APP CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="S.G's E-Commerce Customer Intelligence",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

APP_DIR = Path(__file__).resolve().parent
ROOT_DIR = APP_DIR.parent
DATA_PATH = ROOT_DIR / "ecommerce_clean_data.csv"
ARTIFACTS_DIR = APP_DIR / "artifacts"

MODEL_PATH = ARTIFACTS_DIR / "profit_prediction_pipeline.joblib"
METRICS_PATH = ARTIFACTS_DIR / "model_metrics.csv"
METADATA_PATH = ARTIFACTS_DIR / "model_metadata.json"

COLORS = [
    "#4169E1", "#12B8A6", "#F59E0B",
    "#8B5CF6", "#EF476F", "#64748B"
]


# ==========================================================
# 2. PROFESSIONAL UI STYLING
# ==========================================================


st.markdown("""
<style>
/* Main application background */
.stApp {
    background-color: #F4F7FB;
    color: #1E293B;
}

/* Main headings */
h1, h2, h3, h4 {
    color: #17365D !important;
}

/* Normal text and labels */
p, label, li,
.stMarkdown,
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"] {
    color: #1E293B !important;
}

/* KPI metric cards */
[data-testid="stMetric"] {
    background-color: #FFFFFF;
    border: 1px solid #DCE5F0;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 3px 10px rgba(23, 54, 93, 0.07);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #E8EFF8;
}

[data-testid="stSidebar"] * {
    color: #17365D;
}

/* Input fields and dropdowns */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
[data-baseweb="select"] > div {
    background-color: #FFFFFF;
    color: #1E293B;
    border-color: #CBD5E1;
}

/* Data tables */
[data-testid="stDataFrame"],
[data-testid="stTable"] {
    background-color: #FFFFFF;
}

/* Buttons */
.stButton > button {
    background-color: #1769AA;
    color: #FFFFFF !important;
    border: none;
    border-radius: 8px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #124F82;
    color: #FFFFFF !important;
}

/* Alerts and captions */
[data-testid="stCaptionContainer"] {
    color: #475569;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 3. HELPER FUNCTIONS
# ==========================================================

def page_heading(title, subtitle):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def money(value):
    return f"₹{float(value):,.2f}"


def number(value):
    return f"{float(value):,.0f}"


def find_col(df, candidates):
    """Return the first matching column name."""
    for candidate in candidates:
        if candidate in df.columns:
            return candidate
    return None


def sum_col(df, column):
    if column is None or column not in df.columns:
        return 0.0
    return pd.to_numeric(
        df[column], errors="coerce"
    ).fillna(0).sum()


def unique_count(df, column):
    if column is None or column not in df.columns:
        return len(df)
    return df[column].nunique(dropna=True)


def chart_layout(fig, height=360):
    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(l=15, r=15, t=45, b=15),
        font=dict(family="Arial", color="#334155"),
        legend_title_text="",
    )
    return fig


def show_empty(message):
    st.info(message)


# ==========================================================
# 4. LOAD DATA AND MODEL FILES
# ==========================================================

@st.cache_data(show_spinner="Loading your e-commerce dataset...")
def load_dataset(file_path, modified_time):
    df = pd.read_csv(file_path, low_memory=False)

    for col in ["OrderDate", "SignupDate"]:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col], errors="coerce"
            )

    numeric_columns = [
        "Quantity", "UnitPrice", "DiscountPct",
        "SalesAmount", "Profit", "CostPrice",
        "SellingPrice", "Age", "profitmarginPct"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col], errors="coerce"
            )

    return df


@st.cache_resource(show_spinner="Loading saved ML model...")
def load_pipeline(file_path, modified_time):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return joblib.load(file_path)


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError):
        return {}


# Keep the app visible even when the dataset path is incorrect.
if not DATA_PATH.exists():
    st.title("🛍️ E-Commerce Customer Intelligence")
    st.error("The cleaned dataset could not be found.")
    st.write("Expected dataset location:")
    st.code(str(DATA_PATH))
    st.write(
        "Check that ecommerce_clean_data.csv is in the "
        "main project folder, one level above 05_Streamlit_App."
    )
    st.stop()

try:
    df_original = load_dataset(
        str(DATA_PATH), DATA_PATH.stat().st_mtime
    )
except Exception as error:
    st.title("🛍️ E-Commerce Customer Intelligence")
    st.error("The dataset could not be read.")
    st.exception(error)
    st.stop()


# ==========================================================
# 5. COLUMN MAPPING
# ==========================================================

ORDER = find_col(df_original, ["OrderID", "OrderId", "Order ID"])
DATE = find_col(df_original, ["OrderDate", "Order_Date"])
CUSTOMER = find_col(
    df_original, ["CustomerID", "CustomerId", "Customer ID"]
)
PRODUCT = find_col(
    df_original, ["ProductName", "ProductID", "ProductId"]
)
CATEGORY = find_col(df_original, ["Category", "ProductCategory"])
REGION = find_col(df_original, ["Region"])
SALES = find_col(
    df_original, ["SalesAmount", "Sales", "Revenue"]
)
PROFIT = find_col(df_original, ["Profit", "NetProfit"])
QUANTITY = find_col(df_original, ["Quantity"])
UNIT_PRICE = find_col(df_original, ["UnitPrice", "SellingPrice"])
COST = find_col(df_original, ["CostPrice", "UnitCost"])
DISCOUNT = find_col(df_original, ["DiscountPct", "Discount"])
PAYMENT = find_col(df_original, ["PaymentMethod"])
STATUS = find_col(df_original, ["OrderStatus"])
CITY = find_col(df_original, ["City"])


# ==========================================================
# 6. SIDEBAR AND GLOBAL FILTERS
# ==========================================================

with st.sidebar:
    st.markdown("# 🛍️ E-Commerce")
    st.caption("CUSTOMER INTELLIGENCE PLATFORM")
    st.divider()

    selected_page = st.radio(
        "NAVIGATION",
        [
            "Executive Dashboard",
            "Sales & Product Analytics",
            "Customer Intelligence",
            "Profit Calculator",
            "ML Profit Predictor",
            "Model Performance",
            "Data Explorer",
        ],
        key="page_navigation",
    )

    st.divider()
    st.markdown("### Dashboard Filters")

    st.caption(
        "These filters apply to the analytics pages. "
        "The profit calculator uses its own inputs."
    )

    filtered = df_original.copy()

    if REGION:
        region_values = sorted(
            filtered[REGION].dropna().astype(str).unique().tolist()
        )
        chosen_regions = st.multiselect(
            "Region",
            region_values,
            default=region_values,
            key="global_regions",
        )
        if chosen_regions:
            filtered = filtered[
                filtered[REGION].astype(str).isin(chosen_regions)
            ]
        else:
            filtered = filtered.iloc[0:0]

    if CATEGORY:
        category_values = sorted(
            filtered[CATEGORY].dropna().astype(str).unique().tolist()
        )
        chosen_categories = st.multiselect(
            "Category",
            category_values,
            default=category_values,
            key="global_categories",
        )
        if chosen_categories:
            filtered = filtered[
                filtered[CATEGORY].astype(str).isin(chosen_categories)
            ]
        else:
            filtered = filtered.iloc[0:0]

    if DATE:
        valid_dates = filtered[DATE].dropna()

        if not valid_dates.empty:
            date_selection = st.date_input(
                "Order date range",
                value=(
                    valid_dates.min().date(),
                    valid_dates.max().date(),
                ),
                key="global_date_range",
            )

            if (
                isinstance(date_selection, (tuple, list))
                and len(date_selection) == 2
            ):
                start_date = pd.Timestamp(date_selection[0])
                end_date = (
                    pd.Timestamp(date_selection[1])
                    + pd.Timedelta(days=1)
                )
                filtered = filtered[
                    filtered[DATE].ge(start_date)
                    & filtered[DATE].lt(end_date)
                ]

    st.divider()
    st.caption(f"Source rows: {len(df_original):,}")
    st.caption(f"Filtered rows: {len(filtered):,}")
    st.caption("Currency displayed: INR (₹)")


# Common metrics from the filtered data.
revenue = sum_col(filtered, SALES)
profit = sum_col(filtered, PROFIT)
orders = unique_count(filtered, ORDER)
customers = unique_count(filtered, CUSTOMER)
units_sold = sum_col(filtered, QUANTITY)
margin = (profit / revenue * 100) if revenue else 0.0


# ==========================================================
# PAGE 1: EXECUTIVE DASHBOARD
# ==========================================================

if selected_page == "Executive Dashboard":

    page_heading(
        "Executive Dashboard",
        "A real-time view of sales, profitability, orders, and business performance.",
    )

    if filtered.empty:
        st.warning("No rows match your current sidebar filters.")
        st.stop()

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Net Sales", money(revenue))
    c2.metric("Total Profit", money(profit))
    c3.metric("Orders", number(orders))
    c4.metric("Customers", number(customers))
    c5.metric("Profit Margin", f"{margin:.2f}%")

    st.divider()

    left, right = st.columns([1.55, 1])

    with left:
        st.subheader("📈 Monthly Sales Trend")

        if DATE and SALES:
            trend = filtered.dropna(subset=[DATE]).copy()
            trend["Month"] = trend[DATE].dt.to_period("M").astype(str)

            metrics = [SALES]
            if PROFIT:
                metrics.append(PROFIT)

            monthly = (
                trend.groupby("Month")[metrics]
                .sum()
                .reset_index()
                .sort_values("Month")
            )

            fig = px.line(
                monthly,
                x="Month",
                y=metrics,
                markers=True,
                color_discrete_sequence=COLORS,
            )
            st.plotly_chart(
                chart_layout(fig, 370),
                use_container_width=True,
            )
        else:
            show_empty("OrderDate and SalesAmount are required.")

    with right:
        st.subheader("💰 Profit by Category")

        if CATEGORY and PROFIT:
            category_profit = (
                filtered.groupby(CATEGORY, dropna=False)[PROFIT]
                .sum()
                .reset_index()
                .sort_values(PROFIT, ascending=True)
                .tail(12)
            )

            fig = px.bar(
                category_profit,
                x=PROFIT,
                y=CATEGORY,
                orientation="h",
                color=PROFIT,
                color_continuous_scale="Blues",
            )
            st.plotly_chart(
                chart_layout(fig, 370),
                use_container_width=True,
            )
        else:
            show_empty("Category or Profit column is unavailable.")

    left, right = st.columns(2)

    with left:
        st.subheader("🌍 Sales by Region")

        if REGION and SALES:
            regional = (
                filtered.groupby(REGION, dropna=False)[SALES]
                .sum()
                .reset_index()
                .sort_values(SALES, ascending=False)
            )

            fig = px.bar(
                regional,
                x=REGION,
                y=SALES,
                color=REGION,
                color_discrete_sequence=COLORS,
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(
                chart_layout(fig, 340),
                use_container_width=True,
            )
        else:
            show_empty("Region or sales column is unavailable.")

    with right:
        st.subheader("🏆 Top Products by Sales")

        if PRODUCT and SALES:
            top_products = (
                filtered.groupby(PRODUCT, dropna=False)[SALES]
                .sum()
                .nlargest(10)
                .sort_values()
                .reset_index()
            )

            fig = px.bar(
                top_products,
                x=SALES,
                y=PRODUCT,
                orientation="h",
                color=SALES,
                color_continuous_scale="Teal",
            )
            st.plotly_chart(
                chart_layout(fig, 340),
                use_container_width=True,
            )
        else:
            show_empty("Product and sales columns are unavailable.")

    st.subheader("Business Snapshot")

    summary = pd.DataFrame({
        "Metric": [
            "Total sales",
            "Total profit",
            "Orders",
            "Customers",
            "Units sold",
            "Profit margin",
        ],
        "Value": [
            money(revenue),
            money(profit),
            f"{orders:,}",
            f"{customers:,}",
            f"{units_sold:,.0f}",
            f"{margin:.2f}%",
        ],
    })

    st.dataframe(summary, use_container_width=True, hide_index=True)


# ==========================================================
# PAGE 2: SALES & PRODUCT ANALYTICS
# ==========================================================

elif selected_page == "Sales & Product Analytics":

    page_heading(
        "Sales & Product Analytics",
        "Discover which products and categories drive sales and profit.",
    )

    if filtered.empty:
        st.warning("No rows match your filters.")
        st.stop()

    a, b, c, d = st.columns(4)
    a.metric("Sales", money(revenue))
    b.metric("Profit", money(profit))
    c.metric("Units Sold", f"{units_sold:,.0f}")
    d.metric("Average Order Value", money(revenue / max(orders, 1)))

    left, right = st.columns(2)

    with left:
        st.subheader("Category Comparison")

        if CATEGORY and SALES:
            available_metrics = [SALES]
            if PROFIT:
                available_metrics.append(PROFIT)
            if QUANTITY:
                available_metrics.append(QUANTITY)

            chosen_metric = st.selectbox(
                "Select a metric",
                available_metrics,
                key="product_metric",
            )

            grouped = (
                filtered.groupby(CATEGORY, dropna=False)[chosen_metric]
                .sum()
                .reset_index()
                .sort_values(chosen_metric, ascending=False)
            )

            fig = px.bar(
                grouped,
                x=CATEGORY,
                y=chosen_metric,
                color=chosen_metric,
                color_continuous_scale="Blues",
            )
            st.plotly_chart(
                chart_layout(fig, 380),
                use_container_width=True,
            )

    with right:
        st.subheader("Payment Method Distribution")

        if PAYMENT:
            payment_data = (
                filtered[PAYMENT]
                .fillna("Unknown")
                .value_counts()
                .rename_axis("Payment Method")
                .reset_index(name="Records")
            )

            fig = px.pie(
                payment_data,
                names="Payment Method",
                values="Records",
                hole=0.55,
                color_discrete_sequence=COLORS,
            )
            st.plotly_chart(
                chart_layout(fig, 380),
                use_container_width=True,
            )
        else:
            show_empty("PaymentMethod is unavailable.")

    left, right = st.columns(2)

    with left:
        st.subheader("Order Status Distribution")

        if STATUS:
            status_data = (
                filtered[STATUS]
                .fillna("Unknown")
                .value_counts()
                .rename_axis("Order Status")
                .reset_index(name="Records")
            )

            fig = px.bar(
                status_data,
                x="Order Status",
                y="Records",
                color="Order Status",
                color_discrete_sequence=COLORS,
            )
            st.plotly_chart(
                chart_layout(fig, 350),
                use_container_width=True,
            )
        else:
            show_empty("OrderStatus is unavailable.")

    with right:
        st.subheader("Top 10 Products")

        if PRODUCT and SALES:
            top = (
                filtered.groupby(PRODUCT, dropna=False)[SALES]
                .sum()
                .nlargest(10)
                .sort_values()
                .reset_index()
            )

            fig = px.bar(
                top,
                x=SALES,
                y=PRODUCT,
                orientation="h",
                color=SALES,
                color_continuous_scale="Teal",
            )
            st.plotly_chart(
                chart_layout(fig, 350),
                use_container_width=True,
            )
        else:
            show_empty("Product or SalesAmount is unavailable.")

    st.subheader("Detailed Category Performance")

    if CATEGORY:
        agg = {}
        for col in [SALES, PROFIT, QUANTITY]:
            if col:
                agg[col] = "sum"

        if agg:
            category_table = (
                filtered.groupby(CATEGORY, dropna=False)
                .agg(agg)
                .reset_index()
                .sort_values(SALES, ascending=False)
                if SALES in agg
                else filtered.groupby(CATEGORY, dropna=False)
                .agg(agg)
                .reset_index()
            )

            st.dataframe(
                category_table,
                use_container_width=True,
                hide_index=True,
            )

            st.download_button(
                "Download category report",
                category_table.to_csv(index=False).encode("utf-8"),
                "category_performance.csv",
                "text/csv",
            )


# ==========================================================
# PAGE 3: CUSTOMER INTELLIGENCE
# ==========================================================

elif selected_page == "Customer Intelligence":

    page_heading(
        "Customer Intelligence",
        "Analyze customer value, purchasing frequency, and customer behavior.",
    )

    if filtered.empty:
        st.warning("No rows match your filters.")
        st.stop()

    if CUSTOMER:
        customer_summary = (
            filtered.groupby(CUSTOMER, dropna=False)
            .agg(
                order_count=(ORDER, "nunique") if ORDER else (CUSTOMER, "size"),
                customer_sales=(SALES, "sum") if SALES else (CUSTOMER, "size"),
                customer_profit=(PROFIT, "sum") if PROFIT else (CUSTOMER, "size"),
            )
            .reset_index()
        )

        repeat_customers = (
            customer_summary["order_count"] > 1
        ).sum()

        total_customers = len(customer_summary)
        repeat_rate = (
            repeat_customers / total_customers * 100
            if total_customers else 0
        )

        avg_customer_sales = (
            customer_summary["customer_sales"].mean()
            if total_customers else 0
        )

        a, b, c, d = st.columns(4)
        a.metric("Unique Customers", f"{total_customers:,}")
        b.metric("Repeat Customers", f"{repeat_customers:,}")
        c.metric("Repeat Purchase Rate", f"{repeat_rate:.2f}%")
        d.metric("Avg. Customer Sales", money(avg_customer_sales))

        customer_summary["Customer Segment"] = np.select(
            [
                customer_summary["order_count"] > 1,
                customer_summary["customer_sales"]
                >= customer_summary["customer_sales"].quantile(0.75),
            ],
            ["Repeat Customer", "High-Value One-Time Customer"],
            default="Standard One-Time Customer",
        )

        left, right = st.columns(2)

        with left:
            st.subheader("Customer Segment Distribution")

            segments = (
                customer_summary["Customer Segment"]
                .value_counts()
                .rename_axis("Segment")
                .reset_index(name="Customers")
            )

            fig = px.pie(
                segments,
                names="Segment",
                values="Customers",
                hole=0.55,
                color_discrete_sequence=COLORS,
            )
            st.plotly_chart(
                chart_layout(fig, 370),
                use_container_width=True,
            )

        with right:
            st.subheader("Top 10 Customers by Sales")

            top_customers = (
                customer_summary.nlargest(10, "customer_sales")
                .copy()
            )
            top_customers[CUSTOMER] = (
                top_customers[CUSTOMER].astype(str)
            )

            fig = px.bar(
                top_customers.sort_values("customer_sales"),
                x="customer_sales",
                y=CUSTOMER,
                orientation="h",
                color="customer_sales",
                color_continuous_scale="Teal",
            )
            st.plotly_chart(
                chart_layout(fig, 370),
                use_container_width=True,
            )

        st.subheader("Customer-Level Summary")

        st.dataframe(
            customer_summary.sort_values(
                "customer_sales", ascending=False
            ),
            use_container_width=True,
            hide_index=True,
        )

        st.download_button(
            "Download customer summary",
            customer_summary.to_csv(index=False).encode("utf-8"),
            "customer_intelligence.csv",
            "text/csv",
        )

    else:
        show_empty("CustomerID is not available in the dataset.")

    if "Age" in filtered.columns:
        st.subheader("Customer Age Distribution")
        ages = pd.to_numeric(filtered["Age"], errors="coerce").dropna()

        if not ages.empty:
            fig = px.histogram(
                ages,
                x="Age",
                nbins=20,
                color_discrete_sequence=["#4169E1"],
            )
            st.plotly_chart(
                chart_layout(fig, 300),
                use_container_width=True,
            )


# ==========================================================
# PAGE 4: PROFIT CALCULATOR
# ==========================================================

elif selected_page == "Profit Calculator":

    page_heading(
        "Profit Calculator",
        "Calculate profit from your pricing, cost, quantity, and discount inputs.",
    )

    st.markdown("### Business Formula")

    st.code(
        "Net Sales = Quantity × Unit Price × (1 - Discount % / 100)\n"
        "Total Cost = Quantity × Unit Cost\n"
        "Profit = Net Sales - Total Cost\n"
        "Profit Margin = Profit / Net Sales × 100"
    )

    left, right = st.columns(2)

    with left:
        st.subheader("Product Inputs")

        calc_quantity = st.number_input(
            "Quantity",
            min_value=1,
            value=4,
            step=1,
            key="calc_quantity",
        )

        calc_price = st.number_input(
            "Unit Selling Price (₹)",
            min_value=0.0,
            value=10018.0,
            step=100.0,
            key="calc_price",
        )

        calc_cost = st.number_input(
            "Unit Cost (₹)",
            min_value=0.0,
            value=5353.0,
            step=100.0,
            key="calc_cost",
        )

        calc_discount = st.slider(
            "Discount (%)",
            min_value=0.0,
            max_value=90.0,
            value=15.0,
            step=1.0,
            key="calc_discount",
        )

    net_sales = (
        calc_quantity * calc_price * (1 - calc_discount / 100)
    )
    total_cost = calc_quantity * calc_cost
    calculated_profit = net_sales - total_cost
    calculated_margin = (
        calculated_profit / net_sales * 100
        if net_sales else 0.0
    )

    with right:
        st.subheader("Calculated Results")

        st.metric("Net Sales", money(net_sales))
        st.metric("Total Cost", money(total_cost))

        st.metric(
            "Profit / Loss",
            money(calculated_profit),
            delta="Profit" if calculated_profit >= 0 else "Loss",
        )

        st.metric("Profit Margin", f"{calculated_margin:.2f}%")

        if calculated_profit >= 0:
            st.success("This scenario generates a positive profit.")
        else:
            st.error("This scenario generates a loss.")

    st.divider()
    st.subheader("Interactive What-If Analysis")

    scenario_discounts = [0, 5, 10, 15, 20, 25, 30]
    scenarios = []

    for discount_value in scenario_discounts:
        scenario_sales = (
            calc_quantity
            * calc_price
            * (1 - discount_value / 100)
        )
        scenario_cost = calc_quantity * calc_cost
        scenario_profit = scenario_sales - scenario_cost

        scenarios.append({
            "Discount (%)": discount_value,
            "Net Sales": scenario_sales,
            "Total Cost": scenario_cost,
            "Profit": scenario_profit,
            "Profit Margin (%)": (
                scenario_profit / scenario_sales * 100
                if scenario_sales else 0
            ),
        })

    scenario_df = pd.DataFrame(scenarios)

    fig = px.line(
        scenario_df,
        x="Discount (%)",
        y="Profit",
        markers=True,
        color_discrete_sequence=["#4169E1"],
    )
    st.plotly_chart(
        chart_layout(fig, 350),
        use_container_width=True,
    )

    st.dataframe(
        scenario_df.round(2),
        use_container_width=True,
        hide_index=True,
    )

    st.download_button(
        "Download what-if scenarios",
        scenario_df.to_csv(index=False).encode("utf-8"),
        "profit_scenarios.csv",
        "text/csv",
    )

    st.caption(
        "This calculator uses your entered cost and pricing values. "
        "Its result is formula-based, not an ML prediction."
    )


# ==========================================================
# PAGE 5: ML PROFIT PREDICTOR
# ==========================================================

elif selected_page == "ML Profit Predictor":

    page_heading(
        "ML Profit Predictor",
        "Use your trained machine-learning pipeline to estimate profit.",
    )

    st.warning(
        "The saved model uses Quantity, UnitPrice, DiscountPct, "
        "Category, Region, and PaymentMethod. CostPrice is not a model "
        "input. The prediction is an estimate, not the formula-based "
        "actual profit."
    )

    metadata = load_json(METADATA_PATH)
    expected_features = metadata.get(
        "features",
        [
            "Quantity",
            "UnitPrice",
            "DiscountPct",
            "Category",
            "Region",
            "PaymentMethod",
        ],
    )

    if not MODEL_PATH.exists():
        st.error("The saved ML model file is missing.")
        st.code(str(MODEL_PATH))
        st.stop()

    categories = (
        sorted(df_original[CATEGORY].dropna().astype(str).unique())
        if CATEGORY else ["Unknown"]
    )
    regions = (
        sorted(df_original[REGION].dropna().astype(str).unique())
        if REGION else ["Unknown"]
    )
    payments = (
        sorted(df_original[PAYMENT].dropna().astype(str).unique())
        if PAYMENT else ["Unknown"]
    )

    with st.form("profit_prediction_form"):
        st.subheader("Enter Product Information")

        c1, c2, c3 = st.columns(3)

        with c1:
            ml_quantity = st.number_input(
                "Quantity",
                min_value=1,
                value=2,
                key="ml_quantity",
            )

        with c2:
            ml_price = st.number_input(
                "Unit Price (₹)",
                min_value=0.0,
                value=1000.0,
                key="ml_price",
            )

        with c3:
            ml_discount = st.number_input(
                "Discount (%)",
                min_value=0.0,
                max_value=100.0,
                value=5.0,
                key="ml_discount",
            )

        c4, c5, c6 = st.columns(3)

        with c4:
            ml_category = st.selectbox(
                "Category", categories, key="ml_category"
            )

        with c5:
            ml_region = st.selectbox(
                "Region", regions, key="ml_region"
            )

        with c6:
            ml_payment = st.selectbox(
                "Payment Method", payments, key="ml_payment"
            )

        predict_clicked = st.form_submit_button(
            "Predict Profit",
            type="primary",
            use_container_width=True,
        )

    if predict_clicked:

        input_values = {
            "Quantity": ml_quantity,
            "UnitPrice": ml_price,
            "DiscountPct": ml_discount,
            "Category": ml_category,
            "Region": ml_region,
            "PaymentMethod": ml_payment,
        }

        try:
            pipeline = load_pipeline(
                str(MODEL_PATH), MODEL_PATH.stat().st_mtime
            )

            missing_features = [
                feature for feature in expected_features
                if feature not in input_values
            ]

            if missing_features:
                st.error(
                    "The model metadata lists unexpected features: "
                    + ", ".join(missing_features)
                )
                st.stop()

            model_input = pd.DataFrame(
                [{feature: input_values[feature]
                  for feature in expected_features}]
            )

            prediction = float(
                np.asarray(pipeline.predict(model_input)).reshape(-1)[0]
            )

            st.divider()
            st.subheader("Prediction Result")

            a, b = st.columns(2)

            a.metric("Estimated Profit", money(prediction))
            b.metric(
                "Estimated Profit Per Unit",
                money(prediction / ml_quantity),
            )

            formula_sales = (
                ml_quantity * ml_price * (1 - ml_discount / 100)
            )

            st.metric("Calculated Net Sales", money(formula_sales))

            st.caption(
                "Net Sales above are formula-calculated. The ML profit "
                "prediction is separate and should not be treated as "
                "guaranteed profit."
            )

            with st.expander("View model input"):
                st.dataframe(
                    model_input,
                    use_container_width=True,
                    hide_index=True,
                )

        except Exception as error:
            st.error(
                "The model could not generate a prediction. "
                "Check model compatibility and feature names."
            )
            st.exception(error)


# ==========================================================
# PAGE 6: MODEL PERFORMANCE
# ==========================================================

elif selected_page == "Model Performance":

    page_heading(
        "Model Performance",
        "Review saved model metrics and training information.",
    )

    metadata = load_json(METADATA_PATH)

    if METRICS_PATH.exists():

        try:
            metrics = pd.read_csv(METRICS_PATH)

            st.subheader("Evaluation Metrics")
            st.dataframe(
                metrics,
                use_container_width=True,
                hide_index=True,
            )

            model_column = find_col(
                metrics, ["Model", "model", "ModelName", "model_name"]
            )

            for metric_name in ["MAE", "RMSE", "R2"]:
                metric_column = find_col(
                    metrics,
                    [metric_name, metric_name.lower()],
                )

                if model_column and metric_column:
                    st.subheader(f"{metric_column} Comparison")

                    fig = px.bar(
                        metrics,
                        x=model_column,
                        y=metric_column,
                        color=model_column,
                        color_discrete_sequence=COLORS,
                    )

                    st.plotly_chart(
                        chart_layout(fig, 300),
                        use_container_width=True,
                    )

        except Exception as error:
            st.error("The metrics CSV could not be read.")
            st.exception(error)

    else:
        st.warning("The model_metrics.csv file was not found.")
        st.code(str(METRICS_PATH))

    if metadata:
        st.subheader("Training Metadata")

        a, b, c = st.columns(3)

        a.metric(
            "Training Rows",
            f"{metadata.get('training_rows', 0):,}",
        )

        b.metric(
            "Test Rows",
            f"{metadata.get('test_rows', 0):,}",
        )

        c.metric(
            "Target",
            str(metadata.get("target", "Not specified")),
        )

        st.write(
            "**Model features:**",
            ", ".join(metadata.get("features", [])),
        )

    st.info(
        "MAE and RMSE measure prediction error; lower is generally "
        "better. R² measures explained variation on the evaluated data. "
        "A high R² alone does not guarantee real-world accuracy. "
        "Check for leakage and validate on unseen data."
    )


# ==========================================================
# PAGE 7: DATA EXPLORER
# ==========================================================

elif selected_page == "Data Explorer":

    page_heading(
        "Data Explorer",
        "Search, inspect, profile, and download your filtered data.",
    )

    st.caption(
        f"Showing data after sidebar filters: {len(filtered):,} rows"
    )

    search_text = st.text_input(
        "Search across text columns",
        placeholder="Search product, customer, city, category, region...",
    )

    view = filtered.copy()

    if search_text.strip():
        text_columns = view.select_dtypes(
            include=["object", "string"]
        ).columns

        matches = pd.Series(False, index=view.index)

        for column in text_columns:
            matches |= view[column].astype(str).str.contains(
                search_text.strip(),
                case=False,
                na=False,
                regex=False,
            )

        view = view[matches]

    a, b, c = st.columns(3)
    a.metric("Rows", f"{len(view):,}")
    b.metric("Columns", f"{view.shape[1]:,}")
    c.metric("Duplicate Rows", f"{view.duplicated().sum():,}")

    st.subheader("Dataset Preview")

    st.dataframe(
        view.head(5000),
        use_container_width=True,
        hide_index=True,
    )

    st.download_button(
        "Download Filtered CSV",
        view.to_csv(index=False).encode("utf-8"),
        "ecommerce_filtered_data.csv",
        "text/csv",
        use_container_width=True,
    )

    with st.expander("Data Quality Profile"):

        profile = pd.DataFrame({
            "Column": view.columns,
            "Data Type": [
                str(view[col].dtype) for col in view.columns
            ],
            "Missing Values": [
                int(view[col].isna().sum())
                for col in view.columns
            ],
            "Missing Percentage": [
                round(view[col].isna().mean() * 100, 2)
                for col in view.columns
            ],
            "Unique Values": [
                int(view[col].nunique(dropna=True))
                for col in view.columns
            ],
        })

        st.dataframe(
            profile,
            use_container_width=True,
            hide_index=True,
        )

    with st.expander("Numerical Summary Statistics"):
        numeric_data = view.select_dtypes(include="number")

        if not numeric_data.empty:
            st.dataframe(
                numeric_data.describe().T,
                use_container_width=True,
            )
        else:
            show_empty("No numerical columns are available.")


# ==========================================================
# FOOTER
# ==========================================================

st.divider()
st.caption(
    "E-Commerce Customer Intelligence | Interactive Analytics, "
    "Formula-Based Profit Calculation & Machine Learning"
)
