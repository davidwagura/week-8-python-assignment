import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Year filter
years = st.slider("Select Year Range", 2015, 2025, (2019, 2021))
df_filtered = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]

# Publications by year
st.subheader("Publications by Year")
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = df_filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, ax=ax)
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# Word Cloud
st.subheader("Word Cloud of Titles")
title_text = " ".join(df_filtered['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(title_text)
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Show sample data
st.subheader("Sample Data")
st.write(df_filtered.head())
