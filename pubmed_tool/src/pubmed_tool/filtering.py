from typing import List

# Simple keyword lists for industry and academic affiliations
INDUSTRY_KEYWORDS = [
    "Inc", "Ltd", "LLC", "Corporation", "Corp", "Pharma", "Biotech", "Company", "Co.",
    "Pfizer", "Novartis", "AstraZeneca", "Merck", "Sanofi", "Roche", "GSK", "Johnson & Johnson"
]
ACADEMIC_KEYWORDS = [
    "University", "Institute", "Hospital", "College", "School", "Faculty", "Department"
]

def has_non_academic_affiliation(affiliations: List[str]) -> bool:
    """
    Determine if any affiliation in the list is non-academic (industry).
    Args:
        affiliations: List of author affiliation strings.
    Returns:
        True if any affiliation is non-academic, False otherwise.
    """
    for aff in affiliations:
        aff_lower = aff.lower()
        # Check for industry keywords
        for kw in INDUSTRY_KEYWORDS:
            if kw.lower() in aff_lower:
                return True
        # (Optional) Could check for academic keywords to be more robust
    return False 