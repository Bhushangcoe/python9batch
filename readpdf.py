from pypdf import PdfReader
reader=PdfReader('bhushan-gangurde resume 2026.pdf')
print(len('reader.pages'))
# for i in reader.pages:
#     text=i.extract_text()
#     print(text)

data=reader.pages[1]
print(data.extract_text())