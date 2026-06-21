<div align="center">

# 🏦 Banking Risk & Fraud Transaction Analysis System

**An end-to-end data analytics platform for fraud detection, customer risk scoring, and business intelligence reporting.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Database-orange?logo=postgresql&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

[Overview](#-project-overview) • [Features](#-features) • [Architecture](#-architecture) • [Tech Stack](#-technology-stack) • [Setup](#️-installation--setup) • [API](#-api-endpoints) • [Roadmap](#-future-enhancements)

</div>

---

## 📌 Project Overview

The **Banking Risk & Fraud Transaction Analysis System** is an end-to-end data analytics project that identifies fraudulent transactions, profiles customer behavior, evaluates account-level risk, and surfaces actionable insights for business stakeholders.

It combines **Data Analytics**, **Business Intelligence**, and **API Development** into a single workflow — from raw transaction data to a live dashboard and a queryable API — using **Python, SQL, Power BI, FastAPI, and Streamlit**.

> 💡 This project is built as a portfolio piece to demonstrate practical, full-stack data analyst skills: data cleaning, SQL-driven analysis, fraud-detection logic, dashboarding, and API design.

---

## 🖼️ Preview

<div align="center">

| Dashboard | API Docs |
|---|---|
| _Add a screenshot of your Streamlit/Power BI dashboard here_ | _Add a screenshot of the FastAPI Swagger UI (`/docs`) here_ |

</div>

> Tip: drop screenshots/GIFs into an `assets/` folder and reference them here, e.g. `![Dashboard](assets/dashboard.png)`. Visuals are the first thing recruiters and reviewers look at.

---

## 🚀 Features

### 🔍 Fraud Detection
- High-value transaction monitoring
- Rapid/burst transaction detection (multiple transactions in a short window)
- Location-based anomaly detection (impossible-travel pattern)
- Automated fraud transaction reporting

### 👑 Customer Analytics
- Customer Lifetime Value (CLV) calculation
- High-value customer identification
- Transaction behavior segmentation

### ⚠️ Risk Analysis
- High-risk account detection
- Dormant and blocked account monitoring
- Loan risk evaluation

### 📊 Interactive Dashboard
- KPI cards for at-a-glance monitoring
- Transaction trend analysis over time
- Fraud and risk analytics views
- Merchant-level fraud analysis
- Dynamic filtering and drill-down

### 🌐 API Services
- Fraud Alerts API
- High-Risk Customers API
- Customer CLV API

---

## 🏗️ Architecture

```text
                ┌───────────────┐
                │   Raw Data    │
                │ (CSV sources) │
                └──────┬────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │  Data Cleaning &    │
            │  Transformation     │
            │  (Pandas / Jupyter) │
            └──────────┬──────────┘
                       │
                       ▼
            ┌─────────────────────┐
            │   SQL Database      │
            │  (Analysis Queries) │
            └──────────┬──────────┘
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
 ┌─────────────────┐       ┌─────────────────┐
 │   FastAPI        │       │  Streamlit /     │
 │   (REST API)     │       │  Power BI        │
 │  Fraud Alerts,   │       │  Dashboard       │
 │  CLV, Risk APIs  │       │  KPIs & Charts   │
 └─────────────────┘       └─────────────────┘
```

---

## 🛠️ Technology Stack

| Category         | Tools                  |
| ---------------- | ----------------------- |
| Programming      | Python                  |
| Data Processing  | Pandas, NumPy           |
| Database         | SQL (SQLite/PostgreSQL) |
| Visualization    | Power BI, Plotly        |
| Web Dashboard    | Streamlit               |
| API Development  | FastAPI                 |
| Version Control  | Git & GitHub            |

---

## 📂 Project Structure

```text
banking-risk-analysis/
│
├── data/
│   ├── customers.csv
│   ├── accounts.csv
│   ├── transactions.csv
│   └── loans.csv
│
├── api/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── sql/
│   └── analysis_queries.sql
│
├── notebooks/
│   └── data_cleaning.ipynb
│
├── assets/
│   └── (screenshots, dashboard exports, etc.)
│
├── cleaned_bank_data.csv
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🗂️ Data Schema (Overview)

| Table          | Key Columns                                                            |
| -------------- | ------------------------------------------------------------------------ |
| `customers`    | `customer_id`, `name`, `age`, `city`, `signup_date`                     |
| `accounts`     | `account_id`, `customer_id`, `account_type`, `status`, `balance`        |
| `transactions` | `transaction_id`, `account_id`, `amount`, `type`, `location`, `timestamp` |
| `loans`        | `loan_id`, `customer_id`, `loan_amount`, `status`, `risk_category`      |

> Update this table to match your actual column names — it gives reviewers a fast way to understand your data model without opening the CSVs.

---

## 📈 Dashboard KPIs

- Total Transactions
- Total Transaction Amount
- Fraud Transactions
- Fraud Rate
- Average Transaction Value
- High-Risk Accounts
- Active Customers

---

## 📊 Dashboard Visualizations

- Transaction Trend Analysis
- Fraud Transactions by City
- Debit vs Credit Analysis
- Top Fraud Merchants
- Risk Account Distribution
- Fraud Transaction Details
- High-Risk Accounts Report

---

## 🚨 Fraud Detection Rules

A transaction is flagged as suspicious when:

1. The transaction amount exceeds a predefined threshold.
2. Multiple transactions occur within a short time interval.
3. Transactions originate from different locations within a short duration (impossible-travel pattern).
4. Other high-risk behavioral patterns are detected.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/banking-risk-analysis.git
cd banking-risk-analysis
```

### 2. Create a Virtual Environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and update values such as database connection strings or API keys (if applicable):

```bash
cp .env.example .env
```

---

## ▶️ Running the Project

### Run the Streamlit Dashboard

```bash
cd frontend
streamlit run app.py
```

### Run the FastAPI Server

```bash
cd api
uvicorn main:app --reload
```

API docs will be available at `http://127.0.0.1:8000/docs`.

---

## 🌐 API Endpoints

### Home
```http
GET /
```
Health check / welcome route.

### Fraud Alerts
```http
GET /fraud-alerts
```
Returns suspicious transactions detected by the fraud engine.

### High-Risk Customers
```http
GET /high-risk-customers
```
Returns customers associated with blocked or dormant accounts.

### Customer Lifetime Value
```http
GET /customer-clv/{customer_id}
```
Returns the customer lifetime value for the specified customer.

---

## 🎯 Business Impact

- Improves fraud detection efficiency
- Enhances customer segmentation
- Supports risk-based decision making
- Provides real-time analytics and reporting
- Reduces operational and financial risk

---

## 📚 Key Learnings

- Data cleaning and transformation
- SQL-based business analysis
- Fraud detection logic
- Dashboard development
- API development with FastAPI
- Data storytelling and visualization

---

## 🔮 Future Enhancements

- [ ] Machine Learning–based fraud prediction
- [ ] Real-time transaction monitoring
- [ ] PostgreSQL integration
- [ ] Cloud deployment (AWS/Azure/GCP)
- [ ] User authentication
- [ ] Alert notification system (email/SMS)
- [ ] Docker containerization

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Rakesh Pandey**
Aspiring Data Analyst | Data Engineer | Business Intelligence Enthusiast

[LinkedIn](#) • [GitHub](#) • [Portfolio](#)

---

<div align="center">

⭐ If you found this project useful, consider giving it a star on GitHub.

</div>
