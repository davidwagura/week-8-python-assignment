# CORD-19 Data Explorer

A simple data analysis and Streamlit app exploring the **CORD-19 metadata dataset**.

## 📌 Project Overview
This project analyzes COVID-19 research metadata:
- Data loading & cleaning
- Basic statistics & missing value handling
- Visualizations (publications over time, top journals, word cloud of titles)
- Interactive Streamlit app for exploration

## 🗂 Repo Structure
```
Frameworks_Assignment/
│
├── data/              # Dataset (metadata.csv)
├── notebooks/         # Jupyter exploration
├── app.py             # Streamlit app
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

## 🚀 Installation & Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/Frameworks_Assignment.git
   cd Frameworks_Assignment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add the dataset:
   - Download `metadata.csv` from [CORD-19 Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)  
   - Place it inside `data/metadata.csv`

4. Run Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```

5. Run Streamlit App:
   ```bash
   streamlit run app.py
   ```

## 📊 Features
- Publications by year
- Top publishing journals
- Word cloud of paper titles
- Interactive filtering by year range

## 📖 Reflection
- **Challenges:** Handling missing values, dataset size.
- **Learnings:** Data cleaning, visualization, and building simple Streamlit dashboards.

---
