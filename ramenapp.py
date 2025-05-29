import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("🍜 Ramen Ratings Data Explorer")

# Load data
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1jy8fZFfC1nEKe0-pDyPJOP7Ydd2mf5S6"
    df = pd.read_csv(url)
    return df

df = load_data()

# Clean numeric ratings
df_clean = df[df['Stars'] != 'Unrated'].copy()
df_clean['Stars'] = df_clean['Stars'].astype(float)

# Sidebar
st.sidebar.header("Navigation")
section = st.sidebar.radio("Jump to Section:", [
    "Size of the Data",
    "Understanding the Meaning",
    "Shape of the Variables",
    "Relationships Among Variables",
    "Comparing Variables",
    "Examining Trends in Variables"
])

# Plot 1: Distribution of Ratings (including Unrated)
if section == "Size of the Data":
    st.subheader("Number of Rows and Columns")

    # Get the number of rows and columns
    num_rows = df.shape[0]
    num_cols = df.shape[1]

    # Display the result in the Streamlit app
    st.write(f"Number of rows: {num_rows}")
    st.write(f"Number of columns: {num_cols}")

# Plot 2: Ratings by Style
elif section == "Understanding the Meaning":
    st.subheader("Ramen Ratings by Style")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_clean, x='Style', y='Stars', ax=ax)
    ax.set_title('Ratings by Style')
    ax.set_xlabel('Style')
    ax.set_ylabel('Stars')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 3: Average Rating by Country
elif section == "Shape of the Variables":
    st.subheader("Average Ramen Rating by Country")
    
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.barplot(data=df_clean, x='Country', y='Stars', estimator='mean', ci='sd', ax=ax)
    ax.set_title('Average Rating by Country')
    ax.set_xlabel('Country')
    ax.set_ylabel('Average Stars')
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Plot 4: Top Ramen by Year
elif section == "Relationships Among Variables":
    st.subheader("Top Ramen Products by Year")
    
    df_clean['Year'] = df_clean['Top Ten'].str.extract(r'(\d{4})')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(data=df_clean, x='Year', ax=ax)
    ax.set_title('Number of Ramen in Top Ten by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Count')
    st.pyplot(fig)

# Optional: add GitHub repo link or credits
st.sidebar.markdown("---")
st.sidebar.markdown("Made by [talia/natalie](https://github.com/talialewinger)")
