import streamlit as st
from pubmed_tool.pubmed_api import fetch_pubmed_articles
from pubmed_tool.filtering import has_non_academic_affiliation
import pandas as pd

st.title("PubMed Industry Author Finder")

query = st.text_input("Enter PubMed query:", "cancer immunotherapy")
max_results = st.slider("Max results", 1, 100, 20)

if st.button("Search"):
    with st.spinner("Fetching articles..."):
        articles = fetch_pubmed_articles(query, max_results)
    if not articles:
        st.warning("No articles found.")
    else:
        rows = []
        for art in articles:
            has_industry = has_non_academic_affiliation(art["Affiliations"])
            rows.append({
                "PMID": art["PMID"],
                "Title": art["Title"],
                "Authors": art["Authors"],
                "Journal": art["Journal"],
                "Year": art["Year"],
                "Has_NonAcademic_Author": has_industry,
                "Affiliations": "; ".join(art["Affiliations"]),
            })
        df = pd.DataFrame(rows)
        st.dataframe(df)
        st.download_button("Download CSV", df.to_csv(index=False), "results.csv")
