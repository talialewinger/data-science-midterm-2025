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
    url = "https://raw.githubusercontent.com/talialewinger/data-science-midterm-2025/main/ramen-ratings.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

# Clean numeric ratings
df_clean = df[df['Stars'] != 'Unrated'].copy()
df_clean['Stars'] = df_clean['Stars'].astype(float)

# Sidebar
st.sidebar.header("Navigation")
section = st.sidebar.radio("Jump to Section:", [
    "Distribution of Ratings",
    "Ratings by Style",
    "Ratings by Country",
    "Top Ten by Year"
])

# Plot 1: Distribution of Ratings (including Unrated)
if section == "Distribution of Ratings":
    st.subheader("Distribution of Ramen Ratings (Including Unrated)")
    ordered_stars = sorted(df['Stars'].dropna().unique(), key=lambda x: float(x) if x != 'Unrated' else -1)
    
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.countplot(data=df, x='Stars', order=ordered_stars, ax=ax)
    ax.set_title('Distribution of Ramen Ratings')
    ax.set_xlabel('Stars')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 2: Ratings by Style
elif section == "Ratings by Style":
    st.subheader("Ramen Ratings by Style")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=df_clean, x='Style', y='Stars', ax=ax)
    ax.set_title('Ratings by Style')
    ax.set_xlabel('Style')
    ax.set_ylabel('Stars')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Plot 3: Average Rating by Country
elif section == "Ratings by Country":
    st.subheader("Average Ramen Rating by Country")
    
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.barplot(data=df_clean, x='Country', y='Stars', estimator='mean', ci='sd', ax=ax)
    ax.set_title('Average Rating by Country')
    ax.set_xlabel('Country')
    ax.set_ylabel('Average Stars')
    plt.xticks(rotation=90)
    st.pyplot(fig)

# Plot 4: Top Ramen by Year
elif section == "Top Ten by Year":
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
