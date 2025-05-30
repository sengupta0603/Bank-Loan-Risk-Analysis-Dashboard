
# Bank Loan Risk Analysis Dashboard
Tableau dashboard integrating SQL, Python, and logistic regression to analyze loan risk and generate automated system recommendations.

This Tableau dashboard provides a comprehensive view of bank loan applications segmented by risk level, funding patterns, and repayment behavior. It integrates multiple data sources and advanced analytics techniques to drive smarter decision-making in loan approval workflows.

# Purpose
The dashboard is designed to assist credit analysts, risk teams, and loan officers in evaluating loan applications by analyzing key borrower indicators. It automates risk assessment and generates system-backed recommendations (e.g., Auto-Approve, Manual Review) based on data-driven modeling to reduce default rates and streamline loan approval workflows.

Dashboard Link : https://public.tableau.com/views/BankLoanReport_17476716667410/SUMMARY?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

# Key Features: 
- Interactive Risk Segmentation: Loans are automatically classified as Low, Medium, or High risk using logistic regression on financial indicators like DTI and Interest Rate.
- System Recommendations: Auto-generated recommendations based on risk thresholds (e.g., ✅ Auto Approve, Reduce Interest, Manual Review, ⚠ Reassess DTI, ❌ Do Not Approve).
- KPI Summary: Real-time metrics including Total Applications, Funded Amounts, Interest Rate Trends, and Debt-to-Income Ratio.
- Drill-down Filters: Filter applications by purpose, grade, verification status, and home ownership.

Loan Classification Dashboard:
- Visual segmentation of Good vs. Bad Loans.
- Performance overview by Loan Status, Employee Length, and Loan Term.
- Geographic breakdown by U.S. state.

# Technical Implementation:
- SQL Server: Data extraction, cleaning, transformation, and KPI calculation (DTI, Interest Rate, Loan Status Classification).
- Python (scikit-learn): Logistic regression model trained to predict default probability.
- Tableau: Dashboard creation, conditional formatting, dynamic filtering, and integrating Python-predicted scores with SQL KPIs for holistic risk intelligence.

# Preview
<p align="centre">
   <img src="https://github.com/user-attachments/assets/46916f35-7c37-4ca6-b016-ac3c42c346e2" width="30%" />
   <img src="https://github.com/user-attachments/assets/b9be805b-35d2-426a-be6a-ff5cb40afc53" width="30%" />
  <img src="https://github.com/user-attachments/assets/bcbb08b1-513c-40d8-bd00-8017c38459a5" width="30%" />
</p>

# 📂 How to Use
- Open the Tableau .twbx file or explore the published dashboard.
- Use filters on the left panel to segment by Grade, Purpose, and Risk Category.
- Navigate between tabs: Summary → Overview → Detailed Risk Table.

# 🎯 Outcome & Recommendations
This dashboard enables data-backed lending decisions by:
- Reducing manual underwriting overhead.
- Improving the precision of default prediction.
- Highlighting risky segments for intervention (e.g., High DTI with subprime interest).
- Suggesting real-time actions such as interest rate reduction or manual review.

Recommendation: Use this dashboard as a core tool in pre-approval workflows to minimize risk exposure and optimize portfolio health.

# 👤 Author
Priyanka Sengupta

