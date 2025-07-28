import fitz  # PyMuPDF
import os
import json
from langdetect import detect, LangDetectException

MAX_PAGES = 50  # Maximum allowed pages per PDF

def extract_outline(file_path):
    doc = fitz.open(file_path)
    if len(doc) > MAX_PAGES:
        print(f"❌ Skipping '{os.path.basename(file_path)}': exceeds {MAX_PAGES} pages (has {len(doc)} pages).")
        return None

    outline = []
    title = os.path.basename(file_path).replace('.pdf', '')
    detected_languages = set()

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                    if not line_text:
                        continue

                    try:
                        language = detect(line_text)
                    except LangDetectException:
                        language = "unknown"

                    detected_languages.add(language)

                    font_sizes = [span["size"] for span in line["spans"] if "size" in span]
                    if not font_sizes:
                        continue

                    font_size = max(font_sizes)

                    # Heuristic for heading levels (adjust if needed)
                    if font_size > 20:
                        level = "H1"
                    elif 16 < font_size <= 20:
                        level = "H2"
                    elif 13 < font_size <= 16:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": line_text,
                        "page": page_num,
                        "language": language
                    })

    return {
        "title": title,
        "outline": outline,
        "detected_languages": list(detected_languages)
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            file_path = os.path.join(input_dir, filename)

            result = extract_outline(file_path)

            if result is None:
                continue

            output_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(output_dir, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
