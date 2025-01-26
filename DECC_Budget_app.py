import streamlit as st

# Configure the Streamlit app
st.set_page_config(page_title="DECC Personal Financial Intelligence web app", layout="wide", initial_sidebar_state="expanded")

def main():
    # Title and Introduction
    st.title("Financial Intelligence web app")
    st.markdown("""
    Welcome to your personal financial intelligence web app! This app is designed to help military personnel, students, and professionals living in Europe manage their finances effectively by:
    - Predicting upcoming withdrawals like rent, utilities, or subscriptions.
    - Providing alerts for deposits to maintain balances multiple accounts.
    - Identifying savings opportunities based on your international spending patterns.

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

        st.warning("Ensure you have sufficient funds in your USAA checking and local German account to cover these expenses since that is where they are automatically paid.")

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

    # Personal Finance Insights Section
    elif selected_section == "Personal Finance Insights":
        st.subheader("Personal Finance Insights")
        st.markdown("""
        Get personalized financial advice:
        - Help me create a buget for my house in the US and Germany 
        - How much should I save for my move from Germany to Texas?
        - What is the best way to budget for tuition not covered by my post 9-11 GI Bill?
        - How can I reduce my utility bills when deployed or away from home for over two weeks?
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
    st.markdown("For support or feedback, contact us at [https://www.defcomcap.com](https://www.defcomcap.com).")
    st.markdown("© 2025 DECC | Personal financial intelligence.")

if __name__ == "__main__":
    main()
