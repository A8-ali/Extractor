from pypdf import PdfReader
from errors import PDFEmptyError, InvalidPDFError


def read_pdf(path: str) -> str:
    """
    Read all readable text from a PDF file.

    Args:
        path: Path to the PDF file.

    Returns:
        Extracted text as a single string.

    Raises:
        InvalidPDFError: If the PDF cannot be opened or read.
    """

    try:
        reader = PdfReader(path)
    except Exception as e:
        raise InvalidPDFError(f"Cannot read PDF: {e}") from e

    pages = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            pages.append(page_text)

    return "\n".join(pages)


def validate_text(text: str) -> None:
    """
    Validate extracted text.

    Args:
        text: Text extracted from the PDF.

    Raises:
        PDFEmptyError: If no readable text exists.
    """

    if not text.strip():
        raise PDFEmptyError("The PDF contains no readable text.")


def load_pdf(path: str) -> str:
    """
    Read and validate a PDF.
    """

    text = read_pdf(path)
    validate_text(text)

    return text