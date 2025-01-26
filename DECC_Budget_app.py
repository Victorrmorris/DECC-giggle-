import streamlit as st

# Configure the Streamlit app
st.set_page_config(page_title="Lifestyle Budget Optimizer", layout="wide", initial_sidebar_state="expanded")

# Title and Introduction
st.title("Lifestyle Budget Optimizer")
st.markdown("""
Welcome to the Lifestyle Budget Optimizer! This app is designed to help military personnel, students, and professionals living in Europe manage their finances effectively by:
- Predicting upcoming withdrawals like rent or tuition.
- Providing alerts for deposits to maintain balances.
- Identifying savings opportunities based on your spending patterns.
""")

# Sidebar for Navigation
st.sidebar.header("Navigation")
st.sidebar.markdown("Select a section to explore:")
sections = ["Overview", "Upcoming Withdrawals", "Savings Opportunities", "Chatbot Insights", "Budget Visualization"]
selected_section = st.sidebar.radio("Go to:", sections, index=0)

# Overview Section
if selected_section == "Overview":
    st.subheader("Overview")
    st.write("""
    This app helps you understand your finances at a glance:
    - View predicted upcoming withdrawals.
    - Analyze your spending patterns to uncover savings opportunities.
    - Chat with our AI to get personalized financial insights.
    """)

# Upcoming Withdrawals Section
elif selected_section == "Upcoming Withdrawals":
    st.subheader("Upcoming Withdrawals")
    st.markdown("### My Bills (All Linked Accounts)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Outstanding", "$0")
    col2.metric("Due in next 7 days", "$3,372.15 (€3,233.86)")
    col3.metric("Overdue", "$0")

    st.markdown("#### Next payment on 1st June")
    st.write("**Germany Rent Payment**: $1,800.00 Monthly")
    st.write("**O2 · Internet**: $39.99 Monthly")
    st.write("**REWAG · Utilities**: $30.00 Monthly")

    st.markdown("[View more](#)")
    st.warning("Ensure you have sufficient funds in your account to cover these expenses.")

# Savings Opportunities Section
elif selected_section == "Savings Opportunities":
    st.subheader("Savings Opportunities")
    st.markdown("""
    Based on your spending patterns, here are potential areas to save:
    - Reduce discretionary spending (e.g., dining out, entertainment).
    - Set a monthly savings goal and automate transfers.
    - Take advantage of lower-cost alternatives for recurring expenses.
    """)
    st.success("Tip: Use this section to identify where you can cut costs and save more annually.")

# Budget Visualization Section
elif selected_section == "Budget Visualization":
    st.subheader("Germany and US Household Budgeting")
    categories = ["Groceries", "Rent", "Entertainment", "Utilities", "Transportation"]
    amounts = [1200, 2500, 600, 400, 300]
    total_budget = 6000

    total_spent = sum(amounts)
    st.write(f"**Total Spent:** ${total_spent:,.2f}")

    for category, amount in zip(categories, amounts):
        st.write(f"{category}: ${amount:,.2f} spent out of ${total_budget}")
        st.progress(amount / total_budget)

# Chatbot Insights Section
elif selected_section == "Chatbot Insights":
    st.subheader("Chatbot Insights")
    st.markdown("""
    Ask our AI chatbot for personalized financial advice:
    - How much should I save for my next move?
    - What is the best way to budget for tuition?
    - How can I reduce my utility bills?
    """)

    user_input = st.text_area("Type your question here:", height=200, placeholder="Ask about your finances...")
    if st.button("Get Insights"):
        if user_input.strip():
            st.write(f"AI Response for: '{user_input}'")
        else:
            st.warning("Please enter a question to get insights.")

# Footer
st.markdown("---")
st.markdown("For support, contact us at [support@budgetoptimizer.com](mailto:support@budgetoptimizer.com).")
st.markdown("© 2025 Lifestyle Budget Optimizer.")
