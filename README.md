# Bank-Loan-Risk-Analysis-Dashboard
Tableau dashboard integrating SQL, Python, and logistic regression to analyze loan risk and generate automated system recommendations.


# Bank Loan Risk Analysis Dashboard
This Tableau dashboard provides a comprehensive view of bank loan applications segmented by risk level, funding patterns, and repayment behavior. It integrates multiple data sources and advanced analytics techniques to drive smarter decision-making in loan approval workflows.

# Key Features:

Real-time loan KPIs: Total applications, funded amounts, interest rates, and DTI (Debt-to-Income) ratios.
Risk Segmentation: Loans categorized into Low, Medium, and High Risk using predictive modeling.
System Recommendations: Auto-generated recommendations (e.g., ✅ Auto Approve, ⚠ Reassess DTI, ❌ Do Not Approve) based on borrower profiles and risk logic.

# Technical Implementation:

SQL Server was used to extract and transform structured loan records, calculate funding KPIs, and define core dimensions like loan purpose, grade, and verification status.

Python powered a Logistic Regression model to predict default probability based on key financial features (DTI, Interest Rate, Loan Amount). The results were exported and blended into Tableau for visualization.

# Tableau was used for:
Interactive dashboard creation and filtering (by grade, risk level, verification).
Visual encoding of model outputs and KPI trends.
Performance tuning via extract optimization and blending strategy adjustments.

# ⚙️ Outcome:
This dashboard empowers stakeholders with a dynamic decision-support tool that combines business metrics with machine learning insights — reducing manual effort, increasing approval efficiency, and mitigating financial risk.
