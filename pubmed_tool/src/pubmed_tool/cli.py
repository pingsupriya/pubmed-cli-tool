import typer
import pandas as pd
from pubmed_tool.pubmed_api import fetch_pubmed_articles
from pubmed_tool.filtering import has_non_academic_affiliation
from typing import List

app = typer.Typer(help="Fetch and filter PubMed research papers for non-academic authors.")

@app.command()
def main(
    query: str = typer.Option(..., help="Search query for PubMed (e.g., 'cancer immunotherapy')"),
    output: str = typer.Option(..., help="Output CSV file path"),
    max_results: int = typer.Option(20, help="Maximum number of results to fetch")
):
    """
    Fetch PubMed papers for a query and output filtered results to CSV.
    """
    typer.echo(f"Fetching PubMed articles for query: {query}")
    articles = fetch_pubmed_articles(query, max_results)
    typer.echo(f"Articles: {articles}")
    if not articles:
        typer.echo("No articles found.")
        raise typer.Exit(code=1)
    typer.echo(f"Fetched {len(articles)} articles. Filtering...")
    # Prepare data for CSV
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
    df.to_csv(output, index=False)
    typer.echo(f"Results written to {output}")

if __name__ == "__main__":
    app() 