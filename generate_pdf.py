import json
import os
import shutil
from datetime import datetime

from reportlab.lib.pagesize import A4
from reportlab.platypus import(
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PaageBreak
)
from reportlab.lib.styles import getSampleStyleSheet

os.makedirs("reports", exist_ok=True)

today = datetime.now().srttime("%d/%m/%Y")

pdf_path = "reports/latest_news.pdf"

with open("news.json", "r", encoding="utf-8") as f:
  news = json.load(f)

doc = SimpleDocTemplate(pdf_path, pagesize=A4)

styles = getSampleStyleSheet()

story = []

story.append(
  Paragraph(
    "TECH NEWS DAILY",
    style("Title")
  )
)

story.append(
  Paragraph(
    f"Edizione del {today}",
    styles["Heading2"]
  )
)

story.append(Spacer(1, 30))

story.append(
  Paragraph(
    f"Notizie del giorno: {len(news)}",
    styles["Heading3"]
  )
)

story.append(PageBreak())

for articolo in news:

  story.append(
    Paragraph(
      articolo["categoria"]
      styles["Heading1"]
    )
  )

story.append(
  Paragraph(
    articolo["titolo"]
    styles["Heading2"]
  )
)

story.append(
  Paragraph(
    articolo["descrizione"]
    styles["Normal"]
  )
)

story.append(Spacer(1, 20))

doc.build(story)

print("PDF generato!")
