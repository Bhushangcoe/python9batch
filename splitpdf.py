from pypdf import PdfReader, PdfWriter

reader = PdfReader('bhushan-gangurde resume 2026.pdf')
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i + 1}.pdf", "wb") as file:
        writer.write(file)

print('done')