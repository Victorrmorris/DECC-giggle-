import streamlit as st

# Configure the Streamlit app
st.set_page_config(page_title="Lifestyle Budget Optimizer", layout="wide", initial_sidebar_state="expanded")

def main():
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
    sections = ["Overview", "Upcoming Withdrawals", "Savings Opportunities", "Chatbot Insights"]
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
        st.markdown("""
        Stay on top of your recurring expenses! Here are some examples of upcoming withdrawals you might need to plan for:
        - **Rent:** Due on the 1st of the month.
        - **Tuition:** Semester-based payments.
        - **Utilities:** Monthly payments for electricity, water, and internet.
        """)

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

if __name__ == "__main__":
    main()
