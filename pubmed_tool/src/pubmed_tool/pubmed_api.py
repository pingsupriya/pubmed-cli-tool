from typing import List, Dict
from Bio import Entrez
import time

Entrez.email = "supriyawakchaure0@gmail.com"  # Replace with your email


def fetch_pubmed_articles(query: str, max_results: int = 20) -> List[Dict]:
    """
    Fetch articles from PubMed using Biopython's Entrez API.
    Args:
        query: Search query string.
        max_results: Maximum number of articles to fetch.
    Returns:
        List of article metadata dictionaries.
    """
    results = []
    try:
        # Search PubMed
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()
        id_list = record["IdList"]
        if not id_list:
            return []
        # Fetch details
        handle = Entrez.efetch(db="pubmed", id=",".join(id_list), rettype="medline", retmode="xml")
        records = Entrez.read(handle)
        handle.close()
        for article in records["PubmedArticle"]:
            try:
                medline = article["MedlineCitation"]
                pmid = medline.get("PMID", "")
                article_data = medline.get("Article", {})
                title = article_data.get("ArticleTitle", "")
                authors = []
                affiliations = []
                for author in article_data.get("AuthorList", []):
                    if "LastName" in author and "ForeName" in author:
                        authors.append(f"{author['ForeName']} {author['LastName']}")
                    if "AffiliationInfo" in author:
                        for aff in author["AffiliationInfo"]:
                            affiliations.append(aff.get("Affiliation", ""))
                journal = article_data.get("Journal", {}).get("Title", "")
                year = ""
                try:
                    year = article_data.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", "")
                except Exception:
                    pass
                results.append({
                    "PMID": str(pmid),
                    "Title": str(title),
                    "Authors": "; ".join(authors),
                    "Affiliations": affiliations,
                    "Journal": str(journal),
                    "Year": str(year),
                })
            except Exception as e:
                # Skip malformed articles
                continue
            time.sleep(0.34)  # Be nice to NCBI
    except Exception as e:
        print(f"Error fetching articles: {e}")
    return results 