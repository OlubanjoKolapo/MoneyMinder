from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the data model
class FinanceData(BaseModel):
    income: float
    expenses: float
    risk_level: str  # "low", "medium", "high"

# Budget calculation & investment suggestion logic
def analyze_finances(income, expenses, risk_level):
    savings = income - expenses
    if savings < 0:
        return {"message": "You are spending more than you earn! Consider reducing expenses."}
    
    advice = f"You have ${savings} left after expenses. "
    
    if risk_level == "low":
        advice += "Consider a high-yield savings account or government bonds."
    elif risk_level == "medium":
        advice += "Look into index funds or diversified ETFs."
    elif risk_level == "high":
        advice += "You could explore stocks, crypto, or startups, but manage risk carefully."
    
    return {"savings": savings, "advice": advice}

@app.post("/analyze")
def analyze(finance_data: FinanceData):
    result = analyze_finances(finance_data.income, finance_data.expenses, finance_data.risk_level)
    return result

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Finance Copilot API!"}
