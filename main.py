from pdf_reader import read_pdf, validate_text
from extractor import extract_info
import json


def main():

    pdf_path = input("PDF Path >> ")

    text = read_pdf(pdf_path)

    validate_text(text)

    data = extract_info(text)

    with open("resume.json", "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("Resume parsed successfully.")


if __name__ == "__main__":
    main()
