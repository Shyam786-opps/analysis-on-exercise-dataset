import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache
def load_data():
    df = pd.read_csv("gymData.csv")  # Ensure 'gymData.csv' is in the same directory as the app
    return df

# Title and Description
st.title("Gym Data Analysis App")
st.write("This app allows you to explore and visualize a gym dataset interactively.")

# Load Data
df = load_data()

# Show basic information about the dataset
st.header("Dataset Overview")
st.write("Number of Records:", df.shape[0])
st.write("Number of Columns:", df.shape[1])
st.write(df.head())

# Sidebar for user input
st.sidebar.header("Visualization Settings")
plot_type = st.sidebar.selectbox("Choose Plot Type", ["Histogram", "Scatter Plot"])

# User selection for histogram
if plot_type == "Histogram":
    column = st.sidebar.selectbox("Choose a column for the histogram", df.select_dtypes(include=['float64', 'int64']).columns)
    st.subheader(f"Histogram of {column}")
    fig = px.histogram(df, x=column, title=f"Distribution of {column}")
    st.plotly_chart(fig)

# User selection for scatter plot
elif plot_type == "Scatter Plot":
    x_col = st.sidebar.selectbox("X-axis", df.select_dtypes(include=['float64', 'int64']).columns)
    y_col = st.sidebar.selectbox("Y-axis", df.select_dtypes(include=['float64', 'int64']).columns)
    st.subheader(f"Scatter Plot of {x_col} vs {y_col}")
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs {y_col}")
    st.plotly_chart(fig)

# Additional Options
st.sidebar.header("Additional Analysis")
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(df.describe())
