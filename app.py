import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
from io import BytesIO

# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="Aqua Analytics",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# CUSTOM THEME - LIGHT PURPLE & NAVY BLUE
# -----------------------------------------

st.markdown("""
<style>

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(135deg, #F5F3FF, #EDE9FE, #F8FAFC);
    color: #263247;
}

/* HEADER */

[data-testid="stHeader"] {
    background: transparent;
}

/* MAIN CONTAINER */

[data-testid="stAppViewBlockContainer"] {
    max-width: 100%;
    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* MAIN TEXT */

.stApp p,
.stApp label,
.stApp li,
.stApp .stMarkdown {
    color: #263247;
}

/* HEADINGS */

h1, h2, h3, h4, h5, h6 {
    color: #172554;
}

/* SIDEBAR */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #172554, #1E3A8A);
    border-right: 1px solid #A5B4FC;
}

/* SIDEBAR TEXT */

[data-testid="stSidebar"] * {
    color: #FFFFFF;
}

/* SIDEBAR INPUT LABELS */

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] .stMarkdown {
    color: #FFFFFF !important;
}

/* MAIN TITLE */

.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #1E3A8A;
    margin-bottom: 5px;
}

/* SUBTITLE */

.subtitle {
    color: #475569;
    font-size: 16px;
    margin-bottom: 25px;
}

/* SECTION TITLE */

.section-title {
    font-size: 25px;
    font-weight: 750;
    color: #172554;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* INFORMATION CARD */

.info-card {
    background: linear-gradient(135deg, #EDE9FE, #DDD6FE);
    border: 1px solid #A78BFA;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 15px;
    color: #263247;
}

.info-card h3,
.info-card h4 {
    color: #172554 !important;
}

.info-card p {
    color: #263247 !important;
}

/* METRIC CARDS */

.metric-card {
    padding: 20px;
    border-radius: 15px;
    color: #FFFFFF;
    min-height: 130px;
    box-shadow: 0 5px 18px rgba(23, 37, 84, 0.15);
}

.metric-label {
    font-size: 14px;
    font-weight: 600;
    color: #FFFFFF;
    opacity: 0.95;
}

.metric-value {
    font-size: 27px;
    font-weight: 800;
    margin-top: 12px;
    color: #FFFFFF;
}

/* STREAMLIT METRICS */

div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #EDE9FE, #DDD6FE);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #C4B5FD;
}

div[data-testid="stMetric"] label,
div[data-testid="stMetric"] [data-testid="stMetricValue"],
div[data-testid="stMetric"] [data-testid="stMetricLabel"] {
    color: #172554 !important;
}

/* BUTTONS */

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(90deg, #0F9D9A, #2563EB);
    color: #FFFFFF !important;
    border: none;
    border-radius: 9px;
    font-weight: 650;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    background: linear-gradient(90deg, #2563EB, #0F9D9A);
    color: #FFFFFF !important;
    border: 1px solid #0F9D9A;
}

/* FILE UPLOADER */

[data-testid="stFileUploader"] {
    background: #263B70;
    border-radius: 12px;
    padding: 10px;
}

[data-testid="stFileUploader"] * {
    color: #FFFFFF !important;
}

/* INPUT FIELDS */

.stTextInput input,
.stNumberInput input,
.stDateInput input {
    background-color: #FFFFFF !important;
    color: #172554 !important;
    border: 1px solid #A78BFA !important;
}

/* SELECT BOX */

.stSelectbox div[data-baseweb="select"] > div,
.stMultiSelect div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #172554 !important;
    border-color: #A78BFA !important;
}

/* CHECKBOX */

.stCheckbox label,
.stRadio label {
    color: #263247 !important;
}

/* EXPANDER */

[data-testid="stExpander"] {
    background-color: #F5F3FF;
    border: 1px solid #C4B5FD;
    border-radius: 10px;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary span {
    color: #172554 !important;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border: 1px solid #C4B5FD;
    border-radius: 10px;
}

/* ALERTS */

[data-testid="stAlert"] {
    color: #172554;
}

/* DIVIDER */

hr {
    border-color: #C4B5FD;
}

/* ========= NEW: SIDEBAR ALL WHITE TEXT ========= */

[data-testid="stSidebar"],
[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* Info card in sidebar: dark background so white text is readable */
[data-testid="stSidebar"] .info-card {
    background: #263B70 !important;
    border: 1px solid #A5B4FC !important;
}

[data-testid="stSidebar"] .info-card h3,
[data-testid="stSidebar"] .info-card h4,
[data-testid="stSidebar"] .info-card p {
    color: #FFFFFF !important;
}

/* File uploader: dark box, white text */
[data-testid="stFileUploader"] section,
[data-testid="stFileUploaderDropzone"] {
    background: #263B70 !important;
}

[data-testid="stFileUploader"] button {
    background: #2563EB !important;
    color: #FFFFFF !important;
    border: none !important;
}

[data-testid="stFileUploaderFile"] {
    background: #1E3A8A !important;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------------
# HEADER
# -----------------------------------------

st.markdown(
    '<div class="main-title">💧 AQUA ANALYTICS DASHBOARD</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Universal Water Consumption Analytics Platform</div>',
    unsafe_allow_html=True
)
# -----------------------------------------
# SIDEBAR
# -----------------------------------------

with st.sidebar:

    st.markdown("## 💧 AQUA ANALYTICS")
    st.caption("WATER MANAGEMENT SYSTEM")

    st.divider()

    st.markdown("### 📂 Upload CSV / Excel Files")

    uploaded_files = st.file_uploader(
        "Upload one or multiple CSV or Excel files",
        type=["csv", "xlsx", "xls"],
        accept_multiple_files=True,
        help="Upload water consumption datasets"
    )

    st.divider()

    # TEMPLATES

    template_data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Building": ["Building A", "Building B"],
        "Consumption": [500, 750],
        "Unit": ["Litres", "Litres"],
        "Meter_ID": ["M001", "M002"]
    })

    template_csv = template_data.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV Template",
        data=template_csv,
        file_name="water_consumption_template.csv",
        mime="text/csv",
        use_container_width=True
    )

    template_excel_buffer = BytesIO()

    with pd.ExcelWriter(
        template_excel_buffer,
        engine="openpyxl"
    ) as writer:
        template_data.to_excel(
            writer,
            index=False,
            sheet_name="Water Data"
        )

    st.download_button(
        label="⬇️ Download Excel Template",
        data=template_excel_buffer.getvalue(),
        file_name="water_consumption_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

    st.divider()

    st.markdown("""
    <div class="info-card">
        <h4>💧 WATER MANAGEMENT SYSTEM</h4>
        <p>Upload one or multiple CSV or Excel files to analyse water consumption.</p>
        <p>📊 Building Analytics</p>
        <p>📈 Consumption Trends</p>
        <p>🔍 Unusual Usage Detection</p>
        <p>🧹 Advanced Data Cleaning</p>
    </div>
    """, unsafe_allow_html=True)


# -----------------------------------------
# DATA LOADING AND INITIAL CLEANING
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">📊 Dataset Overview</div>',
    unsafe_allow_html=True
)

if not uploaded_files:

    st.info(
        "👈 Please upload at least one CSV or Excel file from the sidebar "
        "to start water consumption analysis."
    )

    st.markdown("""
    <div class="info-card">
        <h3>Welcome to Aqua Analytics 💧</h3>
        <p>Upload your water consumption dataset to explore:</p>
        <p>📊 Dataset statistics</p>
        <p>🏢 Building-wise consumption</p>
        <p>📈 Daily, weekly and monthly trends</p>
        <p>🔍 Unusual consumption detection</p>
        <p>🧹 Advanced data cleaning</p>
    </div>
    """, unsafe_allow_html=True)

    st.stop()


# -----------------------------------------
# READ AND COMBINE CSV / EXCEL FILES
# -----------------------------------------

dataframes = []

for uploaded_file in uploaded_files:

    try:

        file_name = uploaded_file.name.lower()

        if file_name.endswith(".csv"):

            temp_df = pd.read_csv(uploaded_file)

            temp_df.columns = (
                temp_df.columns.astype(str).str.strip()
            )

            dataframes.append(temp_df)

        elif file_name.endswith((".xlsx", ".xls")):

            # read ALL sheets of the Excel file
            sheets = pd.read_excel(
                uploaded_file,
                sheet_name=None
            )

            for sheet_name, sheet_df in sheets.items():

                sheet_df.columns = (
                    sheet_df.columns.astype(str).str.strip()
                )

                dataframes.append(sheet_df)

    except Exception as e:

        st.error(
            f"Error reading {uploaded_file.name}: {e}"
        )


if not dataframes:

    st.error("No valid file could be loaded.")
    st.stop()


raw_df = pd.concat(
    dataframes,
    ignore_index=True
)

df = raw_df.copy()


# -----------------------------------------
# NORMALIZE COLUMN NAMES
# -----------------------------------------

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)


# -----------------------------------------
# AUTOMATIC COLUMN DETECTION
# -----------------------------------------

column_aliases = {

    "Date": [
        "date",
        "reading_date",
        "record_date",
        "timestamp",
        "datetime"
    ],

    "Building": [
        "building",
        "building_name",
        "block",
        "location",
        "area"
    ],

    "Consumption": [
        "consumption",
        "water_consumption",
        "usage",
        "water_usage",
        "litres",
        "liters",
        "quantity",
        "volume"
    ],

    "Meter_ID": [
        "meter_id",
        "meterid",
        "meter",
        "consumer_id",
        "consumerid",
        "id"
    ],

    "Unit": [
        "unit",
        "measurement_unit",
        "consumption_unit"
    ]
}


detected_columns = {}

for standard_name, aliases in column_aliases.items():

    for alias in aliases:

        if alias in df.columns:

            detected_columns[standard_name] = alias
            break


# -----------------------------------------
# CHECK REQUIRED COLUMNS
# -----------------------------------------

required_columns = [
    "Date",
    "Building",
    "Consumption"
]

missing_columns = [
    col for col in required_columns
    if col not in detected_columns
]


if missing_columns:

    st.error(
        "Required columns could not be detected: "
        + ", ".join(missing_columns)
    )

    st.warning(
        "Your file should contain Date, Building and "
        "Consumption columns. You can rename your "
        "headers or use our downloadable template."
    )

    st.write("Available columns:", list(df.columns))

    st.stop()


# -----------------------------------------
# RENAME DETECTED COLUMNS
# -----------------------------------------

rename_mapping = {
    actual_name: standard_name
    for standard_name, actual_name
    in detected_columns.items()
}

df = df.rename(columns=rename_mapping)
# -----------------------------------------
# ADD OPTIONAL COLUMNS IF MISSING
# -----------------------------------------

if "Meter_ID" not in df.columns:

    df["Meter_ID"] = [
        f"METER-{i+1:04d}"
        for i in range(len(df))
    ]


if "Unit" not in df.columns:

    df["Unit"] = "Litres"


# -----------------------------------------
# DATA TYPE CONVERSION
# -----------------------------------------

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Consumption"] = pd.to_numeric(
    df["Consumption"],
    errors="coerce"
)


# -----------------------------------------
# TEXT CLEANING
# -----------------------------------------

for col in ["Building", "Meter_ID", "Unit"]:

    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
    )


# -----------------------------------------
# INITIAL DATA QUALITY CHECK
# -----------------------------------------

original_records = len(df)

invalid_date_count = df["Date"].isna().sum()

invalid_consumption_count = (
    df["Consumption"].isna().sum()
)

missing_building_count = (
    df["Building"].isna().sum()
)


# Remove rows with missing required values

df = df.dropna(
    subset=[
        "Date",
        "Building",
        "Consumption"
    ]
).copy()


# Remove negative consumption values

negative_count = (
    df["Consumption"] < 0
).sum()

df = df[
    df["Consumption"] >= 0
].copy()

df.reset_index(
    drop=True,
    inplace=True
)


# -----------------------------------------
# DATA LOADING STATUS
# -----------------------------------------

st.success(
    f"✅ {len(uploaded_files)} file(s) uploaded successfully!"
)

st.success(
    f"✅ {len(df)} valid records loaded successfully!"
)

st.caption(
    f"Original records: {original_records} | "
    f"Invalid dates: {invalid_date_count} | "
    f"Invalid consumption: {invalid_consumption_count} | "
    f"Missing building: {missing_building_count} | "
    f"Negative readings: {negative_count}"
)


if df.empty:

    st.error(
        "No valid records are available after cleaning. "
        "Please check your data."
    )

    st.stop()


# -----------------------------------------
# DETECTED DATASET COLUMNS
# -----------------------------------------

with st.expander("🔎 View Detected Dataset Columns"):

    st.write(
        "Automatically detected columns:"
    )

    st.dataframe(
        pd.DataFrame({
            "Standard Column": list(detected_columns.keys()),
            "File Column": list(detected_columns.values())
        }),
        use_container_width=True,
        hide_index=True
    )


# -----------------------------------------
# DATASET STATISTICS
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">📊 Dataset Statistics</div>',
    unsafe_allow_html=True
)

total_records = len(df)
total_columns = len(df.columns)
missing_values = int(df.isna().sum().sum())
duplicate_rows = int(df.duplicated().sum())

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📋 Total Records",
        f"{total_records:,}"
    )

with col2:

    st.metric(
        "📊 Total Columns",
        f"{total_columns:,}"
    )

with col3:

    st.metric(
        "⚠️ Missing Values",
        f"{missing_values:,}"
    )

with col4:

    st.metric(
        "🔁 Duplicate Rows",
        f"{duplicate_rows:,}"
    )


# -----------------------------------------
# DATA PREVIEW
# -----------------------------------------

with st.expander("👀 View Dataset Preview"):

    st.dataframe(
        df.head(100),
        use_container_width=True,
        hide_index=True
    )


# -----------------------------------------
# DATA QUALITY REPORT
# -----------------------------------------

with st.expander("🔍 View Data Quality Report"):

    quality_report = pd.DataFrame({
        "Column": df.columns,
        "Data Type": [
            str(df[col].dtype)
            for col in df.columns
        ],
        "Missing Values": [
            int(df[col].isna().sum())
            for col in df.columns
        ],
        "Unique Values": [
            int(df[col].nunique())
            for col in df.columns
        ]
    })

    st.dataframe(
        quality_report,
        use_container_width=True,
        hide_index=True
    )


# -----------------------------------------
# ADVANCED DATA CLEANING
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">🧹 Advanced Data Cleaning</div>',
    unsafe_allow_html=True
)

st.write(
    "Select the cleaning operations you want to apply "
    "to your water consumption dataset."
)

clean_col1, clean_col2 = st.columns(2)

with clean_col1:

    remove_duplicates = st.checkbox(
        "🔁 Remove duplicate rows",
        value=False
    )

    remove_empty_columns = st.checkbox(
        "🗑️ Remove completely empty columns",
        value=False
    )

    remove_empty_rows = st.checkbox(
        "🧹 Remove completely empty rows",
        value=False
    )

with clean_col2:

    remove_extra_spaces = st.checkbox(
        "✂️ Remove unnecessary text spaces",
        value=False
    )

    remove_duplicate_ids = st.checkbox(
        "🆔 Remove duplicate Meter IDs (keep first)",
        value=False
    )


# -----------------------------------------
# MISSING VALUE TREATMENT
# -----------------------------------------

st.markdown("### ⚙️ Missing Value Treatment")

missing_treatment = st.selectbox(
    "Choose missing value treatment",
    [
        "Keep missing values",
        "Remove rows with missing values",
        "Fill numerical missing values with median",
        "Fill numerical missing values with zero"
    ]
)


# -----------------------------------------
# APPLY CLEANING
# -----------------------------------------

if st.button(
    "🚀 Apply Data Cleaning",
    use_container_width=True
):

    cleaned_df = df.copy()

    initial_count = len(cleaned_df)

    # Remove completely empty columns

    if remove_empty_columns:

        cleaned_df = cleaned_df.dropna(
            axis=1,
            how="all"
        )

    # Remove completely empty rows

    if remove_empty_rows:

        cleaned_df = cleaned_df.dropna(
            axis=0,
            how="all"
        )

    # Remove unnecessary spaces

    if remove_extra_spaces:

        for col in cleaned_df.select_dtypes(
            include=["object", "string"]
        ).columns:

            cleaned_df[col] = (
                cleaned_df[col]
                .astype("string")
                .str.strip()
            )

    # Remove duplicate rows

    if remove_duplicates:

        cleaned_df = cleaned_df.drop_duplicates()

    # Remove duplicate meter IDs

    if remove_duplicate_ids and "Meter_ID" in cleaned_df.columns:

        cleaned_df = cleaned_df.drop_duplicates(
            subset=["Meter_ID"],
            keep="first"
        )

    # Missing value treatment

    if missing_treatment == "Remove rows with missing values":

        cleaned_df = cleaned_df.dropna()

    elif missing_treatment == "Fill numerical missing values with median":

        numeric_cols = cleaned_df.select_dtypes(
            include=np.number
        ).columns

        for col in numeric_cols:

            median_value = cleaned_df[col].median()

            if pd.notna(median_value):

                cleaned_df[col] = cleaned_df[col].fillna(
                    median_value
                )

    elif missing_treatment == "Fill numerical missing values with zero":

        numeric_cols = cleaned_df.select_dtypes(
            include=np.number
        ).columns

        cleaned_df[numeric_cols] = (
            cleaned_df[numeric_cols].fillna(0)
        )

    cleaned_df = cleaned_df.reset_index(drop=True)

    # Save cleaned data in session state

    st.session_state["cleaned_water_data"] = cleaned_df

    removed_count = initial_count - len(cleaned_df)

    st.success(
        "✅ Data cleaning completed successfully!"
    )

    st.write(
        f"Original records: {initial_count:,}"
    )

    st.write(
        f"Final records: {len(cleaned_df):,}"
    )

    st.write(
        f"Records removed: {removed_count:,}"
    )


# -----------------------------------------
# USE CLEANED DATA
# -----------------------------------------

if "cleaned_water_data" in st.session_state:

    df = st.session_state["cleaned_water_data"]

    st.success(
        f"Current analysis dataset: {len(df):,} records"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )


# -----------------------------------------
# DUPLICATE METER ID DETECTION
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">🆔 Duplicate Meter ID Detection</div>',
    unsafe_allow_html=True
)

if "Meter_ID" in df.columns:

    meter_data = df.dropna(
        subset=["Meter_ID"]
    ).copy()

    duplicate_mask = meter_data.duplicated(
        subset=["Meter_ID"],
        keep=False
    )

    duplicate_id_data = meter_data[
        duplicate_mask
    ].sort_values("Meter_ID")

    total_meter_ids = meter_data["Meter_ID"].nunique()

    duplicate_id_count = (
        meter_data.loc[duplicate_mask, "Meter_ID"].nunique()
    )

    id_col1, id_col2, id_col3 = st.columns(3)

    with id_col1:

        st.metric(
            "Unique Meter IDs",
            f"{total_meter_ids:,}"
        )

    with id_col2:

        st.metric(
            "Duplicate Meter IDs",
            f"{duplicate_id_count:,}"
        )

    with id_col3:

        st.metric(
            "Records with Repeated IDs",
            f"{len(duplicate_id_data):,}"
        )

    if duplicate_id_count > 0:

        st.warning(
            "⚠️ Repeated Meter IDs found. "
            "Check whether these are duplicate records or "
            "multiple valid readings from the same meter."
        )

        with st.expander("🔎 View Duplicate Meter ID Records"):

            st.dataframe(
                duplicate_id_data,
                use_container_width=True,
                hide_index=True
            )

    else:

        st.success(
            "✅ No repeated Meter IDs detected."
        )

else:

    st.info("Meter ID column is not available.")
    # -----------------------------------------
# DASHBOARD FILTERS
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">🎛️ Dashboard Filters</div>',
    unsafe_allow_html=True
)

filter_col1, filter_col2 = st.columns(2)

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

with filter_col1:

    selected_dates = st.date_input(
        "📅 Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

with filter_col2:

    available_buildings = sorted(
        df["Building"].dropna().astype(str).unique().tolist()
    )

    selected_buildings = st.multiselect(
        "🏢 Select Buildings",
        options=available_buildings,
        default=available_buildings
    )


# -----------------------------------------
# APPLY FILTERS
# -----------------------------------------

filtered_df = df.copy()

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:

    start_date, end_date = selected_dates

    filtered_df = filtered_df[
        (filtered_df["Date"].dt.date >= start_date) &
        (filtered_df["Date"].dt.date <= end_date)
    ]

if selected_buildings:

    filtered_df = filtered_df[
        filtered_df["Building"].astype(str).isin(
            selected_buildings
        )
    ]

else:

    filtered_df = filtered_df.iloc[0:0]


if filtered_df.empty:

    st.warning(
        "No records found for the selected filters. "
        "Please change your date range or buildings."
    )

    st.stop()


st.success(
    f"Showing {len(filtered_df):,} records after applying filters."
)


# -----------------------------------------
# DASHBOARD OVERVIEW
# -----------------------------------------

st.markdown("---")
st.markdown(
    '<div class="section-title">📊 Dashboard Overview</div>',
    unsafe_allow_html=True
)

total_consumption = filtered_df["Consumption"].sum()
average_consumption = filtered_df["Consumption"].mean()
maximum_consumption = filtered_df["Consumption"].max()
minimum_consumption = filtered_df["Consumption"].min()

total_readings = len(filtered_df)
total_buildings = filtered_df["Building"].nunique()


# -----------------------------------------
# KPI CARDS
# -----------------------------------------

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown(
        """
        <div class="metric-card"
        style="background:linear-gradient(135deg,#0284C7,#06B6D4);">
            <div class="metric-label">💧 Total Consumption</div>
            <div class="metric-value">
        """
        + f"{total_consumption:,.2f}"
        + """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        """
        <div class="metric-card"
        style="background:linear-gradient(135deg,#4F46E5,#7C3AED);">
            <div class="metric-label">📊 Average Consumption</div>
            <div class="metric-value">
        """
        + f"{average_consumption:,.2f}"
        + """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        """
        <div class="metric-card"
        style="background:linear-gradient(135deg,#059669,#10B981);">
            <div class="metric-label">⬆️ Maximum Consumption</div>
            <div class="metric-value">
        """
        + f"{maximum_consumption:,.2f}"
        + """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with kpi4:
    st.markdown(
        """
        <div class="metric-card"
        style="background:linear-gradient(135deg,#EA580C,#F97316);">
            <div class="metric-label">⬇️ Minimum Consumption</div>
            <div class="metric-value">
        """
        + f"{minimum_consumption:,.2f}"
        + """
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------------
# CONSUMPTION SUMMARY
# -----------------------------------------

st.markdown("### 📌 Consumption Summary")

sum1, sum2, sum3 = st.columns(3)

with sum1:
    st.metric("Total Readings", f"{total_readings:,}")

with sum2:
    st.metric("Total Buildings", f"{total_buildings:,}")

with sum3:
    average_per_building = (
        total_consumption / total_buildings
        if total_buildings > 0 else 0
    )
    st.metric(
        "Average per Building",
        f"{average_per_building:,.2f}"
    )


# -----------------------------------------
# BUILDING ANALYTICS
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">🏢 Building Analytics</div>',
    unsafe_allow_html=True
)

building_chart_data = (
    filtered_df.groupby("Building", as_index=False)["Consumption"]
    .sum()
    .sort_values("Consumption", ascending=False)
)

building_fig = px.bar(
    building_chart_data,
    x="Building",
    y="Consumption",
    color="Building",
    title="Total Water Consumption by Building",
    text_auto=".2s",
    template="plotly_white"
)

building_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#172554"),
    showlegend=False,
    xaxis_title="Building",
    yaxis_title="Consumption",
    xaxis=dict(
        title_font=dict(color="#172554"),
        tickfont=dict(color="#263247")
    ),
    yaxis=dict(
        title_font=dict(color="#172554"),
        tickfont=dict(color="#263247"),
        gridcolor="#DDD6FE"
    )
)

st.plotly_chart(
    building_fig,
    use_container_width=True,
    key="building_analytics_chart"
)


# -----------------------------------------
# CONSUMPTION TRENDS
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">📈 Consumption Trends</div>',
    unsafe_allow_html=True
)

trend_option = st.selectbox(
    "Select Trend Period",
    ["Daily", "Weekly", "Monthly"],
    key="trend_period_selector"
)

trend_data = filtered_df.copy().set_index("Date")

if trend_option == "Daily":
    trend_data = (
        trend_data["Consumption"]
        .resample("D")
        .sum()
        .reset_index()
    )

elif trend_option == "Weekly":
    trend_data = (
        trend_data["Consumption"]
        .resample("W")
        .sum()
        .reset_index()
    )

else:
    trend_data = (
        trend_data["Consumption"]
        .resample("MS")
        .sum()
        .reset_index()
    )


trend_fig = px.line(
    trend_data,
    x="Date",
    y="Consumption",
    markers=True,
    title=f"{trend_option} Water Consumption Trend",
    template="plotly_white"
)

trend_fig.update_traces(
    line=dict(width=3, color="#0F9D9A"),
    marker=dict(size=8, color="#172554")
)

trend_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#172554"),
    xaxis_title="Date",
    yaxis_title="Consumption",
    xaxis=dict(
        title_font=dict(color="#172554"),
        tickfont=dict(color="#263247")
    ),
    yaxis=dict(
        title_font=dict(color="#172554"),
        tickfont=dict(color="#263247"),
        gridcolor="#DDD6FE"
    )
)

st.plotly_chart(
    trend_fig,
    use_container_width=True,
    key="consumption_trend_chart"
)


# -----------------------------------------
# CONSUMPTION DISTRIBUTION
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">🥧 Consumption Distribution</div>',
    unsafe_allow_html=True
)

pie_data = (
    filtered_df.groupby("Building", as_index=False)["Consumption"]
    .sum()
)

pie_fig = px.pie(
    pie_data,
    names="Building",
    values="Consumption",
    title="Water Consumption Distribution by Building",
    hole=0.45,
    template="plotly_white"
)

pie_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#172554"),
    legend=dict(
        font=dict(color="#263247")
    )
)

st.plotly_chart(
    pie_fig,
    use_container_width=True,
    key="consumption_distribution_chart"
)


# -----------------------------------------
# UNUSUAL WATER USAGE DETECTION
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">⚠️ Unusual Water Usage Detection</div>',
    unsafe_allow_html=True
)

q1 = filtered_df["Consumption"].quantile(0.25)
q3 = filtered_df["Consumption"].quantile(0.75)

iqr = q3 - q1

lower_limit = max(0, q1 - 1.5 * iqr)
upper_limit = q3 + 1.5 * iqr

unusual_usage = filtered_df[
    (filtered_df["Consumption"] < lower_limit) |
    (filtered_df["Consumption"] > upper_limit)
]

anomaly_col1, anomaly_col2, anomaly_col3 = st.columns(3)

with anomaly_col1:
    st.metric(
        "Unusual Readings",
        f"{len(unusual_usage):,}"
    )

with anomaly_col2:
    st.metric(
        "Lower Limit",
        f"{lower_limit:,.2f}"
    )

with anomaly_col3:
    st.metric(
        "Upper Limit",
        f"{upper_limit:,.2f}"
    )


if not unusual_usage.empty:

    st.warning(
        f"⚠️ {len(unusual_usage)} unusual water consumption "
        "readings detected!"
    )

    st.markdown("### Unusual Usage Records")

    st.dataframe(
        unusual_usage,
        use_container_width=True
    )

    anomaly_fig = px.scatter(
        filtered_df,
        x="Date",
        y="Consumption",
        color="Building",
        title="Unusual Water Consumption Detection",
        template="plotly_white"
    )

    anomaly_fig.add_hline(
        y=upper_limit,
        line_dash="dash",
        line_color="red",
        annotation_text="Upper Limit"
    )

    anomaly_fig.add_hline(
        y=lower_limit,
        line_dash="dash",
        line_color="#0F9D9A",
        annotation_text="Lower Limit"
    )

    anomaly_fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#172554"),
        xaxis_title="Date",
        yaxis_title="Consumption",
        xaxis=dict(
            title_font=dict(color="#172554"),
            tickfont=dict(color="#263247")
        ),
        yaxis=dict(
            title_font=dict(color="#172554"),
            tickfont=dict(color="#263247"),
            gridcolor="#DDD6FE"
        ),
        legend=dict(
            font=dict(color="#263247")
        )
    )

    st.plotly_chart(
        anomaly_fig,
        use_container_width=True
    )

else:

    st.success(
        "✅ No unusual water consumption readings detected!"
    )
    # -----------------------------------------
# DETAILED RECORDS
# -----------------------------------------

st.markdown("---")

st.markdown(
    '<div class="section-title">📋 Detailed Records</div>',
    unsafe_allow_html=True
)

search_query = st.text_input(
    "🔍 Search Records",
    placeholder="Search by Building or Meter ID..."
)

if search_query:

    search_df = filtered_df[
        filtered_df["Building"].astype(str).str.contains(
            search_query,
            case=False,
            na=False
        ) |
        filtered_df["Meter_ID"].astype(str).str.contains(
            search_query,
            case=False,
            na=False
        )
    ]

else:

    search_df = filtered_df


st.dataframe(
    search_df,
    use_container_width=True
)


# -----------------------------------------
# DOWNLOAD REPORTS
# -----------------------------------------

st.markdown("### 📥 Download Reports")

# CSV

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download CSV Report",
    data=csv_data,
    file_name="water_consumption_report.csv",
    mime="text/csv"
)

# EXCEL

excel_buffer = BytesIO()

with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:

    filtered_df.to_excel(
        writer,
        index=False,
        sheet_name="Water Data"
    )

    building_chart_data.to_excel(
        writer,
        index=False,
        sheet_name="Building Summary"
    )

    if not unusual_usage.empty:

        unusual_usage.to_excel(
            writer,
            index=False,
            sheet_name="Unusual Readings"
        )

st.download_button(
    label="📊 Download Excel Report",
    data=excel_buffer.getvalue(),
    file_name="water_consumption_report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


# -----------------------------------------
# PDF DOWNLOAD
# -----------------------------------------

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


pdf_buffer = BytesIO()

pdf_doc = SimpleDocTemplate(
    pdf_buffer,
    pagesize=landscape(letter)
)

elements = []

styles = getSampleStyleSheet()

elements.append(
    Paragraph(
        "Aqua Analytics - Water Consumption Report",
        styles["Title"]
    )
)

elements.append(Spacer(1, 0.3 * inch))


# PDF SUMMARY

pdf_summary = [
    ["Report Summary", "Value"],
    ["Total Readings", str(total_readings)],
    ["Total Buildings", str(total_buildings)],
    ["Total Consumption", f"{total_consumption:,.2f}"],
    ["Average Consumption", f"{average_consumption:,.2f}"],
    ["Unusual Readings", str(len(unusual_usage))]
]

summary_table = Table(pdf_summary)

summary_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#172554")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#263247")),
        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F5F3FF")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#C4B5FD")),
        ("PADDING", (0, 0), (-1, -1), 8),
    ])
)

elements.append(summary_table)

elements.append(Spacer(1, 0.3 * inch))


# PDF DETAILED DATA

elements.append(
    Paragraph(
        "Detailed Water Consumption Records",
        styles["Heading2"]
    )
)

pdf_table_data = [filtered_df.columns.tolist()]

pdf_table_data.extend(
    filtered_df.astype(str).values.tolist()
)

data_table = Table(
    pdf_table_data,
    repeatRows=1
)

data_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#172554")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor("#263247")),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#C4B5FD")),
        ("PADDING", (0, 0), (-1, -1), 5),
    ])
)

elements.append(data_table)

pdf_doc.build(elements)

pdf_buffer.seek(0)

st.download_button(
    label="📄 Download PDF Report",
    data=pdf_buffer,
    file_name="water_consumption_report.pdf",
    mime="application/pdf"
)


# -----------------------------------------
# FOOTER
# -----------------------------------------

st.markdown("""
<div style="background: linear-gradient(135deg, #172554, #1E3A8A); padding: 20px; border-radius: 12px; text-align: center; margin-top: 20px;">
<h4 style="color: white; margin-bottom: 8px;">💧 Aqua Analytics</h4>
<p style="color: #E0E7FF; margin: 0;">Smart Water Consumption Monitoring Dashboard</p>
<p style="color: #CBD5E1; font-size: 13px; margin-top: 8px;">Designed for efficient water usage analysis</p>
</div>
""", unsafe_allow_html=True)