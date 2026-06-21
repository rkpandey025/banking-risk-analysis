from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load dataset
df = pd.read_csv("cleaned_bank_data.csv")

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.get("/")
def home():
    return {"message": "Banking Risk Analysis API Running"}

# -----------------------------
# FRAUD ALERTS API
# -----------------------------
@app.get("/fraud-alerts")
def fraud_alerts():

    fraud_df = df[df['fraud_flag'] == True]

    result = fraud_df[
        ['transaction_id', 'account_id', 'amount', 'location']
    ].head(20)

    return result.to_dict(orient="records")

# -----------------------------
# HIGH RISK CUSTOMERS API
# -----------------------------
@app.get("/high-risk-customers")
def high_risk_customers():

    risk_df = df[
        (df['account_status'].isin(['Blocked', 'Dormant']))
    ]

    result = risk_df[
        ['customer_id', 'account_id', 'account_status', 'balance']
    ].drop_duplicates()

    return result.to_dict(orient="records")

# -----------------------------
# CUSTOMER CLV API
# -----------------------------
@app.get("/customer-clv/{customer_id}")
def customer_clv(customer_id: str):

    customer_data = df[df['customer_id'] == customer_id]

    clv = customer_data['amount'].sum()

    return {
        "customer_id": customer_id,
        "customer_lifetime_value": int(clv)
    }