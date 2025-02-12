import streamlit as st
from analytics_ui import analytics_tab
from add_update_ui import add_update_tab



st.title('Expense Management System')

tab1, tab2 = st.tabs(["Add/update", "Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()



    