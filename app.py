"""import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="CSV Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 CSV to Dashboard") 
st.write("Upload a CSV file and explore your data interactively.")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Dataset Preview
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Dataset Information
    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    # Column Names
    st.subheader("Columns")
    st.write(list(df.columns))

    # Missing Values
    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum().reset_index().rename(
        columns={
            "index": "Column",
            0: "Missing Values"
        }
    ))

    # Summary Statistics
    st.subheader("Summary Statistics")
    st.dataframe(df.describe(include="all"))

    # Data Cleaning
    st.subheader("🧹 Data Cleaning")

    clean_df = df.copy()

    col1, col2 = st.columns(2)

    with col1:
      if st.checkbox("Remove Duplicates"):
        before = clean_df.shape[0]
        clean_df = clean_df.drop_duplicates()
        removed = before - clean_df.shape[0]
        st.success(f"{removed} duplicate rows removed")

    with col2:
      if st.checkbox("Drop Missing Values"):
        before = clean_df.shape[0]
        clean_df = clean_df.dropna()
        removed = before - clean_df.shape[0]
        st.success(f"{removed} rows removed")

    df = clean_df


    # Sidebar Filters
    st.sidebar.header("Filters")

    filtered_df = df.copy()

    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for col in categorical_columns:
        options = st.sidebar.multiselect(
            f"Filter {col}",
            df[col].dropna().unique()
        )

        if options:
            filtered_df = filtered_df[
                filtered_df[col].isin(options)
            ]

    # Filtered Data
    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

    # Download Button
    csv = filtered_df.to_csv(index=False)

    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name="filtered_data.csv",
        mime="text/csv"
    )

    # Numeric Columns
    numeric_columns = filtered_df.select_dtypes(
        include="number"
    ).columns

    # Histogram
    st.subheader("Histogram")

    if len(numeric_columns) > 0:

        hist_column = st.selectbox(
            "Select Column for Histogram",
            numeric_columns,
            key="hist"
        )

        fig_hist = px.histogram(
            filtered_df,
            x=hist_column,
            title=f"Histogram of {hist_column}"
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )

        #

    # Box Plot
    st.subheader("📦 Box Plot")

    if len(numeric_columns) > 0:

     box_column = st.selectbox(
        "Select Column for Box Plot",
        numeric_columns,
        key="box"
    )

    fig_box = px.box(
        filtered_df,
        y=box_column,
        title=f"Box Plot of {box_column}"
    )

    st.plotly_chart(
        fig_box,
        use_container_width=True
    )
    # Scatter Plot
    st.subheader("Scatter Plot")

    if len(numeric_columns) >= 2:

        col1, col2 = st.columns(2)

        with col1:
            x_axis = st.selectbox(
                "X Axis",
                numeric_columns,
                key="x"
            )

        with col2:
            y_axis = st.selectbox(
                "Y Axis",
                numeric_columns,
                key="y"
            )

        fig_scatter = px.scatter(
            filtered_df,
            x=x_axis,
            y=y_axis,
            title=f"{x_axis} vs {y_axis}"
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )

    # Bar Chart
    st.subheader("Bar Chart")

    if len(categorical_columns) > 0:

        bar_column = st.selectbox(
            "Select Categorical Column",
            categorical_columns,
            key="bar"
        )

        bar_data = (
            filtered_df[bar_column]
            .value_counts()
            .reset_index()
        )

        bar_data.columns = [
            bar_column,
            "Count"
        ]

        fig_bar = px.bar(
            bar_data,
            x=bar_column,
            y="Count",
            title=f"Count of {bar_column}"
        )

        st.plotly_chart(
            fig_bar,
            use_container_width=True
        )

    #
    # Pie Chart
    st.subheader("🥧 Pie Chart")

    if len(categorical_columns) > 0:

      pie_column = st.selectbox(
        "Select Column for Pie Chart",
        categorical_columns,
        key="pie"
    )

    pie_data = (
        filtered_df[pie_column]
        .value_counts()
        .reset_index()
    )

    pie_data.columns = [
        pie_column,
        "Count"
    ]

    fig_pie = px.pie(
        pie_data,
        names=pie_column,
        values="Count",
        title=f"Distribution of {pie_column}"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    # Correlation Heatmap Data
    st.subheader("Correlation Matrix")

    if len(numeric_columns) >= 2:

        corr = filtered_df[numeric_columns].corr()

        st.dataframe(corr)

        #
    # Key Insights
    st.subheader("💡 Key Insights")

    if len(numeric_columns) > 0:

     insight_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
        key="insight"
    )

    st.write(
        f"Highest Value: {filtered_df[insight_column].max()}"
    )

    st.write(
        f"Lowest Value: {filtered_df[insight_column].min()}"
    )

    st.write(
        f"Average Value: {filtered_df[insight_column].mean():.2f}"
    )

    st.write(
        f"Median Value: {filtered_df[insight_column].median():.2f}"
    )

    st.write(
        f"Standard Deviation: {filtered_df[insight_column].std():.2f}"
    )

else:
    st.info("Please upload a CSV file to begin.")
    """ 

    

###################

import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------
# Page Congiguration
# -------------------------

st.set_page_config(
    page_title = "CSV Dashboard",
    page_icon = "📊",
    layout = "wide"
)

# --------------------------
# Title
# -------------------------

st.title("📊 CSV to Dashboard")
st.write("Uplod a CSV file and explore data interactively")

# --------------------------
# Uploaded CSV
# -------------------------

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type = ["csv"]
)

if uploaded_file is not None:
    
    # -----------
    # Read CSV
    # ----------

    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully")

    # -----------------
    # Dataset Preview
    # ----------------

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # --------------------
    #ataset inforamtion
    # -------------------

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns ", df.shape[1])

    # -----------------------
    # Columns name 
    # ----------------------

    st.subheader("Columns")
    st.write(list(df.columns))

    # ---------------
    # Missing values 
    # ---------------

    st.subheader("Missing values")
    st.dataframe(df.isnull().sum().reset_index().rename(
        columns={
            "index": "Column",
            0: "Missing Values"
        }
    ))

    # --------------------
    #summary statistics
    # -------------------

    st.subheader("Summary Statistics")
    st.dataframe(df.describe(include = "all"))

    ##########################

    # ----------------------------
    # Data Cleaning
    # ----------------------------
    
    st.subheader("🧹 Data Cleaning")

    clean_df = df.copy()

    col1, col2, = st.columns(2)

    with col1:
        if st.checkbox("Remove Duplicates"):
            before = clean_df.shape[0]
            clean_df = clean_df.drop_duplicates()
            removed = before - clean_df.shape[0]
            st.success(f"{removed} duplicates rows rremoved")
    with col2:
        if st.checkbox("Drop Missing values"):
            before = clean_df.shape[0]
            clean_df = clean_df.dropna()
            removed = before - clean_df.shape[0]
            st.success(f"{removed} rows removed")
    df = clean_df

    # -------------------------
    # Siderbar Filters
    # ------------------------
    st.sidebar.header("Filters")

    filtered_df = df.copy()


    categorical_columns = df.select_dtypes(
        include = ["object"]
    ).columns

    for col in categorical_columns:
        options = st.sidebar.multiselect(
            f"Filter {col}",
            df[col].dropna().unique()
        )

        if options:
            filtered_df = filtered_df[
                    filtered_df[col].isin(options)
            ]

    # Filterd Data
    st.subheader("Filtered Data")
    st.dataframe(filtered_df)

    # ----------------------
    # Download Button
    # ---------------------

    csv = filtered_df.to_csv(index = False)

    st.download_button(
        label = "Download Filterd Data",
        data = csv,
        file_name = "filtered_data.csv",
        mime = "text/csv"
    )

    # Numeric Columns 
    numeric_columns = filtered_df.select_dtypes(
        include = "number"
    ).columns

    # ----------------
    # Histogram
    # ----------------

    st.subheader("Histogram")

    if len(numeric_columns) > 0:
        hist_column = st.selectbox(
            "Select Column for Histogram",
            numeric_columns,
            key = "hist"
        )


        fig_hist = px.histogram(
            filtered_df,
            x = hist_column,
            title = f"Histogram of {hist_column}"
        )

        st.plotly_chart(
            fig_hist,
            use_container_width = True
        )

        ####################
        # ------------------------
        # Box Plot
        # ------------------------

        st.subheader("📦 Box Plot")

        if len(numeric_columns) > 0:

            box_column = st.selectbox(
                "select Column for box Plot",
                numeric_columns,
                key="box"
            )

            fig_box = px.box(
                filtered_df,
                y=box_column,
                title=f"Box Plot of {box_column}"
            )

            st.plotly_chart(
                fig_box,
                use_container_width=True
            )

        # ----------------------------
        # scatter Plot
        # ----------------------------

        st.subheader("Scatter Plot")

        if len(numeric_columns) >= 2:

            col1, col2, = st.columns(2)

            with col1:
                x_axis = st.selectbox(
                    "X Axis",
                    numeric_columns,
                    key = "x"
                )
                        
            with col2:
                y_axis = st.selectbox(
                    "Y axix",
                    numeric_columns,
                    key = "y"
                )
                
            fig_scatter = px.scatter(
                 filtered_df,
                 x = x_axis,
                 y = y_axis,
                 title= f"{x_axis} vs {y_axis}"
            )

            st.plotly_chart(
                fig_scatter,
                use_container_width = True
            )
            
        # --------------------------------
        # Bar Chart
        # --------------------------------

        st.subheader("Bar Chart")

        if len(categorical_columns) > 0:
                 
            bar_column = st.selectbox(
                "Slecet Categorical Column",
                categorical_columns,
                key = "bar"
            )

            bar_data = (
                filtered_df[bar_column]
                .value_counts()
                .reset_index()
            )

            bar_data.columns = [
                bar_column,
                "Count"
            ]

            fig_bar = px.bar(
                bar_data,
                x = bar_column,
                y = "Count",
                title = f"count of {bar_column}"
            )
        
        
            st.plotly_chart(
                fig_bar,
                use_container_width = True
            )

        # -------------------
        # Pie Chart
        # -------------------

        st.subheader("🥧 Pie Chart")
        
        if len(categorical_columns) > 0:

            pie_column = st.selectbox(
                "Select Column for Pie Chart",
                categorical_columns,
                key="pie"
            )

            pie_data = (
                filtered_df[pie_column]
                .value_counts()
                .reset_index()

            )

            pie_data.columns =[
                pie_column,
                "Count"
            ]

            fig_pie = px.pie(
                pie_data,
                names=pie_column,
                values="Count",
                title=f"Distruction of {pie_column}"
            )

            st.plotly_chart(
                fig_pie,
                use_container_width=True
            )

        # ---------------------------------
        # Correlation Heatmap data
        # ---------------------------------
        st.subheader("Correlation Matrix")

        if len(numeric_columns) >= 2:
            corr = filtered_df[numeric_columns].corr()
            st.dataframe(corr)

        ###############

        # ---------------------
        # Key insights
        # --------------------

        st.subheader("💡 key Insights")

        if len(numeric_columns) > 0:
            insight_column = st.selectbox(
                "Select Numeric olumn",
                numeric_columns,
                key="insights"
            )

            st.write(
                f"Highest Value: {filtered_df[insight_column].max()}"
            )

            st.write(
                f"Lowest Value: {filtered_df[insight_column].min()}"
            )

            st.write(
                f"Average Value: {filtered_df[insight_column].mean():.2f}"           
            )

            st.write(
                f"Median Value: {filtered_df[insight_column].median():.2f}"           
            )

            st.write(
                f"Standard Deviation: {filtered_df[insight_column].std():.2f}"           
            )

else:
    st.info("Please upload a CSV file to begin")

                
                
"""

######################

import streamlit as st
import pandas as pd
import plotly.express as px
from fpdf import FPDF
import tempfile

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Data Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

# =========================
# DARK MODE
# =========================
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

if dark_mode:
    bg = "#0e1117"
    text = "white"
    card = "#1c1f26"
else:
    bg = "#f5f7fa"
    text = "black"
    card = "white"

st.markdown(f"""
""" 
<style>
.main {{
    background-color: {bg};
    color: {text};
}}

div[data-testid="metric-container"] {{
    background-color: {card};
    border-radius: 12px;
    padding: 12px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}}
</style>
"""
""", unsafe_allow_html=True)

# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Upload & Overview", "EDA Dashboard", "Insights Engine", "Export Reports"]
)

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# =========================
# DATA CLEANING FUNCTION
# =========================
def clean_data(df):
    df = df.drop_duplicates()

    for col in df.select_dtypes(include="number").columns:
        df[col] = df[col].fillna(df[col].median())

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

# =========================
# PDF GENERATOR
# =========================
def generate_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, text)

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp_file.name)

    return tmp_file.name

# =========================
# MAIN APP
# =========================
if uploaded_file is not None:

    df = load_data(uploaded_file)
    df = clean_data(df)

    numeric_cols = df.select_dtypes(include="number").columns
    cat_cols = df.select_dtypes(include="object").columns

    # =========================
    # PAGE 1 - OVERVIEW
    # =========================
    if page == "Upload & Overview":

        st.title("📊 Dataset Overview")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Rows", df.shape[0])
        c2.metric("Columns", df.shape[1])
        c3.metric("Missing", df.isnull().sum().sum())
        c4.metric("Duplicates", df.duplicated().sum())

        st.subheader("Preview")
        st.dataframe(df.head())

    # =========================
    # PAGE 2 - EDA
    # =========================
    elif page == "EDA Dashboard":

        st.title("📈 Exploratory Data Analysis")

        col1, col2 = st.columns(2)

        if len(numeric_cols) > 0:

            with col1:
                c = st.selectbox("Histogram", numeric_cols)
                fig = px.histogram(df, x=c)
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                c = st.selectbox("Box Plot", numeric_cols, key="box")
                fig = px.box(df, y=c)
                st.plotly_chart(fig, use_container_width=True)

        if len(cat_cols) > 0:

            c = st.selectbox("Category Chart", cat_cols)
            data = df[c].value_counts().reset_index()
            data.columns = [c, "Count"]

            fig = px.pie(data, names=c, values="Count")
            st.plotly_chart(fig)

        if len(numeric_cols) > 1:

            st.subheader("Correlation Heatmap")
            corr = df[numeric_cols].corr()

            fig = px.imshow(corr, text_auto=True, color_continuous_scale="Blues")
            st.plotly_chart(fig, use_container_width=True)

    # =========================
    # PAGE 3 - INSIGHTS ENGINE
    # =========================
    elif page == "Insights Engine":

        st.title("🤖 AI Insights Engine")

        if len(numeric_cols) > 0:

            col = numeric_cols[0]

            insight = f"""
""" 
DATA INTELLIGENCE REPORT

Dataset Size:
- Rows: {df.shape[0]}
- Columns: {df.shape[1]}

Key Column Analysis: {col}

Statistics:
- Max: {df[col].max()}
- Min: {df[col].min()}
- Mean: {df[col].mean():.2f}
- Median: {df[col].median():.2f}

Business Insight:
This dataset shows measurable variation in {col}, which may indicate strong operational or financial trends depending on domain context. """ 
"""

            st.text_area("Generated Insight", insight, height=300)

    # =========================
    # PAGE 4 - EXPORT
    # =========================
    elif page == "Export Reports":

        st.title("📦 Export Center")

        csv = df.to_csv(index=False)

        st.download_button(
            "⬇ Download CSV",
            data=csv,
            file_name="clean_dataset.csv",
            mime="text/csv"
        )

        if st.button("Generate PDF Report"):

            report_text = f"""
""" 
DATA REPORT

Rows: {df.shape[0]}
Columns: {df.shape[1]}
Missing Values: {df.isnull().sum().sum()}

Numeric Columns:
{list(numeric_cols)}

Categorical Columns:
{list(cat_cols)}
"""

"""pdf_file = generate_pdf(report_text)

            with open(pdf_file, "rb") as f:
                st.download_button(
                    "⬇ Download PDF Report",
                    f,
                    file_name="report.pdf"
                )

else:
    st.title("📊 Data Intelligence Platform")
    st.info("Upload a CSV file from sidebar to begin analysis")"""

