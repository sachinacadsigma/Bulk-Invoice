import streamlit as st

pages = {
    "Navigation Menu": [
        st.Page("invoice_extractor.py", title="Invoice Extractor"),
    ]
}

pg = st.navigation(pages)
pg.run()
