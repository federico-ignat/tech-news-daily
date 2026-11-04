import json
import os
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

# Cartella output
os.makedirs("reports", exist_ok=True)

today = datetime.now().strftime("%d/%m/%Y")

pdf_path = "reports/latest_news.pdf"

# Legge le notizie
with open("news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

doc = SimpleDocTemplate(pdf_path, pagesize=A4)

styles = getSampleStyleSheet()

# Stile personalizzato per i titoli
news_title = ParagraphStyle(
    "NewsTitle",
    parent=styles["Heading1"],
    fontSize=22,
    leading=26
)

story = []

# COPERTINA

story.append(
    Paragraph(
        "TECH NEWS DAILY",
        styles["Title"]
    )
)

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        f"Edizione del {today}",
        styles["Heading2"]
    )
)

story.append(Spacer(1, 40))

story.append(
    Paragraph(
        "Le principali notizie tecnologiche del giorno",
        styles["Heading1"]
    )
)

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        f"Articoli inclusi: {len(news)}",
        styles["Heading3"]
    )
)

story.append(Spacer(1, 30))

story.append(
    Paragraph(
        "🤖 AI • 💻 Software • 🖥 Hardware • 🎮 Gaming • 🌐 Web",
        styles["Normal"]
    )
)

# PAGINE ARTICOLI

for articolo in news:

    story.append(PageBreak())

    story.append(
        Paragraph(
            f"📰 {articolo['categoria']}",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            articolo["titolo"],
            news_title
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            articolo["descrizione"],
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 30))

    story.append(
        Paragraph(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            styles["Normal"]
        )
    )

# CREA PDF

doc.build(story)

print("PDF generato!")
