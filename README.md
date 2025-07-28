# Adobe Hackathon 2025 – Round 1A: PDF Outline Extractor (Multilingual)

## 🚀 Project Overview

This project is built for **Round 1A** of Adobe's "Connecting the Dots" Hackathon.

The goal is to extract a structured **outline** from a PDF by identifying:
- ✅ The document **Title**
- ✅ Headings: **H1**, **H2**, **H3**
- ✅ Page numbers for each heading
- ✅ Language of each heading (Multilingual support)

---

## 🧠 Key Features

- Extracts document structure from any PDF up to 50 pages
- Uses **font-size-based heuristics** to classify heading levels
- Supports **bilingual and multilingual content** using `langdetect`
- Outputs a **clean JSON file** per PDF
- Runs fully **offline**, no external API calls
- Compatible with **AMD64 (x86_64)** architecture
- Lightweight, CPU-only, Dockerized setup

---

## 🧱 Tech Stack

- Python 3.10
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF parsing
- [langdetect](https://pypi.org/project/langdetect/) for language detection
- Docker (for isolation, architecture compatibility)

---

## 📁 Project Structure

adobe-pdf-outline-extractor/
├── main.py # Main script to extract outline
├── requirements.txt # Python dependencies
├── Dockerfile # Docker setup (offline + CPU)
├── README.md # This file
├── input/ # Input folder to place your PDFs
└── output/ # Output folder where JSON results are stored


---

## 🐳 Docker Build & Run Instructions

### Step 1: Build the Docker Image (on AMD64 architecture)

```docker build --platform linux/amd64 -t mysolution:multilang . ```

### Step 2: Run the Container (No Internet Access Allowed)

✅ PowerShell (Windows):

``` docker run --rm -v "${PWD}\input:/app/input" -v "${PWD}\output:/app/output" --network none mysolution:multilang ```

✅ Git Bash/Linux/macOS:

``` docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" --network none mysolution:multilang ```

🧪 Sample Output JSON Format

```json```
{
  "title": "Understanding AI",
  "outline": [
    {
      "level": "H1",
      "text": "Introduction",
      "page": 1,
      "language": "en"
    },
    {
      "level": "H2",
      "text": "人工知能の歴史",
      "page": 2,
      "language": "ja"
    }
  ],
  "detected_languages": ["en", "ja"]
}

```

📦 Dependencies (from requirements.txt)

PyMuPDF
langdetect
