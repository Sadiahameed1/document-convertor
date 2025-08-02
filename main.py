"""
PDF to Word Converter Script
----------------------------
Converts a PDF file into a Word (.docx) document using the pdf2docx library.

Author: [Sadia Hameed]
Portfolio Project: PDF to Word Converter
"""

import os
from pdf2docx import Converter


def convert_pdf_to_docx(pdf_path: str, docx_path: str) -> None:
    """
    Converts a PDF file to DOCX format.

    :param pdf_path: Path to the input PDF file
    :param docx_path: Path to save the output DOCX file
    """
    if not os.path.exists(pdf_path):
        print(f"❌ Error: File not found - {pdf_path}")
        return

    try:
        print(f"🔄 Converting '{pdf_path}' to '{docx_path}'...")
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
        print(f"✅ Conversion complete! Word document saved as: {docx_path}")
    except Exception as e:
        print(f"❌ Failed to convert file: {e}")


if __name__ == "__main__":
    # Example usage
    input_pdf = "data-analyst-roadmap.pdf"
    output_docx = "data-analyst-roadmap.docx"

    convert_pdf_to_docx(input_pdf, output_docx)
