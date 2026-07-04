import pytest

from pdf_reader import validate_text
from errors import PDFEmptyError

def test_validate_text_valide():
    validate_text("A8-ali")
def test_validate_text_empty():
    with pytest.raises(PDFEmptyError):
        validate_text("")
def test_validate_text_whitespace():
    with pytest.raises(PDFEmptyError):
        validate_text("     ")
def test_validate_text_newlines():
    with pytest.raises(PDFEmptyError):
        validate_text("\n\n")