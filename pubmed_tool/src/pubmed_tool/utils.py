def validate_email(email: str) -> bool:
    """
    Simple email validation for Entrez registration.
    """
    return "@" in email and "." in email 