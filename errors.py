class PDFEmptyError(Exception):
    """Raised when the PDF contains no readable text."""
    pass


class InvalidPDFError(Exception):
    """Raised when the PDF cannot be opened."""
    pass


class APIError(Exception):
    """Raised when the AI API request fails."""
    pass


class ExtractionError(Exception):
    """Raised when extracted data is invalid."""
    pass