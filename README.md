# 📦 PulseCart Predictive Intelligence

A beginner-friendly **Big Data Analytics & Predictive Intelligence** project built
around a rare, portfolio-friendly e-commerce idea: combining customer recency,
engagement, revenue and repeat-purchase prediction in one small analytics lab.

> **Dataset note:** All customer data in this repository is synthetic and created
> for education/demo purposes.

## ✨ What makes it different
Instead of a common "sales dashboard", PulseCart focuses on a simple question:

**"Which customer signals appear connected to the next purchase?"**

It combines:
- customer behavior analytics
- SQL
- a small SQLite database
- Logistic Regression for repeat-purchase probability
- Linear Regression as a revenue benchmark
- Streamlit dashboard
- Power BI-ready CSV
- beginner-friendly documentation

## 📁 Folder structure

```text
pulsecart_predictive_intelligence/
├── data/
│   ├── raw/
│   │   └── pulsecart_customers.csv
│   └── processed/
│       ├── pulsecart_clean.csv
│       └── pulsecart.db
├── dashboard/
│   └── app.py
├── docs/
│   ├── ARCHITECTURE.md
│   └── POWER_BI_GUIDE.md
├── notebooks/
│   └── 01_pulsecart_analysis.ipynb
├── reports/
│   ├── PROJECT_REPORT.md
│   ├── repeat_purchase_model.joblib
│   └── revenue_model.joblib
├── sql/
│   └── analysis_queries.sql
├── src/
│   ├── preprocess.py
│   ├── train_models.py
│   └── predict.py
├── requirements.txt
└── README.md
```

## 🛠️ Setup

### 1. Install Python
Use Python 3.10+.

### 2. Open terminal in the project folder

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

### 3. Install packages

```bash
pip install -r requirements.txt
```

### 4. Prepare the data

```bash
python src/preprocess.py
```

### 5. Train the models

```bash
python src/train_models.py
```

### 6. Launch the dashboard

```bash
streamlit run dashboard/app.py
```

Then open the local address shown in the terminal.

## 🧠 What to explain in a viva/interview

**Q: Why did you choose Logistic Regression?**  
A: It is simple, fast and easy to explain for a beginner classification problem.

**Q: What is the target?**  
A: `repeat_purchase_30d`, which indicates whether a customer made a repeat purchase.

**Q: Is this real customer data?**  
A: No. It is synthetic data created for learning and portfolio demonstration.

**Q: What is the business value?**  
A: The workflow helps identify behavior patterns, compare customer segments and
experiment with retention-oriented analytics.

## 📊 Power BI
Use `data/processed/pulsecart_clean.csv` with the steps in
`docs/POWER_BI_GUIDE.md`.

## ⚠️ Important
Do not describe the synthetic results as real company findings. Do not upload
private customer information to GitHub.

## 👤 Portfolio description
**PulseCart Predictive Intelligence — Beginner Big Data Analytics Project**

Built an end-to-end e-commerce analytics workflow using Python, pandas, SQL,
scikit-learn and Streamlit. Analyzed customer behavior, created KPI dashboards,
and trained simple predictive models for repeat-purchase probability and revenue.
