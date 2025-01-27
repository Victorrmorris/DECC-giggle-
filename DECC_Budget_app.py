import streamlit as st
import matplotlib.pyplot as plt

# Configure the Streamlit app
st.set_page_config(page_title="DECC Personal Financial Intelligence Web App", layout="wide", initial_sidebar_state="expanded")

def main():
    # Title and Introduction
    st.title("Personal Financial Intelligence Web App")
    st.markdown("""
    Welcome to your personal financial intelligence web app! This app is designed to help military personnel, students, and professionals living in Europe manage their finances effectively by:
    - Predicting upcoming withdrawals like rent, utilities, or subscriptions.
    - Providing alerts for deposits to maintain balances across multiple accounts.
    - Identifying savings opportunities based on your international spending patterns.
    """)

    # Sidebar for Navigation
    st.sidebar.header("Navigation")
    st.sidebar.markdown("Select a section to explore:")
    sections = ["Home", "Recurring Payments", "Spending Analytics", "Personal Finance Insights"]
    selected_section = st.sidebar.radio("Go to:", sections, index=0)

    # Home Section
    if selected_section == "Home":
        st.subheader("Overview")
        st.write("""
        This app helps you understand your international finances at a glance:
        - View account balances across all accounts.
        - Analyze your spending patterns to uncover savings opportunities.
        - Chat with our AI to get personalized financial insights.
        """)

    # Recurring Payments Section
    elif selected_section == "Recurring Payments":
        st.subheader("Recurring Payments")
        st.markdown("""
        Stay on top of your recurring payments! Here are some examples of upcoming withdrawals you might need to plan for:
        - **Rent:** Due on the 1st of the month.
        - **Tuition:** Semester-based payments.
        - **Utilities:** Monthly payments for electricity, water, and internet.
        """)

        # Visualize upcoming withdrawals
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
        st.warning("Ensure you have sufficient funds in your USAA and local German account to cover these expenses.")

    # Spending Analytics Section
    elif selected_section == "Spending Analytics":
        st.subheader("Spending Analytics")
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

    # Budget data
    categories = ["Groceries", "Rent", "Entertainment", "Utilities", "Transportation"]
    amounts = [1200, 2500, 600, 400, 300]  # Example spending amounts
    total_budget = 6000  # Example total budget

    # Display total spending
    total_spent = sum(amounts)
    st.write(f"**Total Spent:** ${total_spent:,.2f}")

    # Display individual category spending with progress bars
    for category, amount in zip(categories, amounts):
        st.write(f"{category}: ${amount:,.2f} spent out of ${total_budget}")
        st.progress(amount / total_budget)

    # Display total spending
    total_spent = sum(amounts)
    st.write(f"**Total Spent:** ${total_spent:,.2f}")

    # Display individual category spending with progress bars
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

    # Large chatbot UI
    user_input = st.text_area("Type your question here:", height=200, placeholder="Ask about your finances, budgeting, or savings opportunities...")
    if st.button("Get Insights"):
        # Placeholder for chatbot integration: Replace this with API/model integration if available.
        if user_input.strip():
            st.write(f"AI Response for: '{user_input}'")  # Placeholder for chatbot response
        else:
            st.warning("Please enter a question to get insights.")

# Footer
st.markdown("---")
st.markdown("For support or feedback, contact us at [support@budgetoptimizer.com](mailto:support@budgetoptimizer.com).")
st.markdown("© 2025 Lifestyle Budget Optimizer | Your trusted financial companion.")
