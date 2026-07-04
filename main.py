from pdf_reader import read_pdf, validate_text
from extractor import extract_info

from logger import logger

import json


def main():
    logger.info("Application started")

    pdf_path = input("PDF Path >> ")

    text = read_pdf(pdf_path)

    validate_text(text)

    data = extract_info(text)

    logger.info("Saving output to resume.json")

    with open("resume.json", "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    logger.info("Resume parsed successfully")

    print("Resume parsed successfully.")


if __name__ == "__main__":
    main()

