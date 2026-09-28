from pypdf import PdfWriter

write=PdfWriter()
for i in ['first.pdf','second.pdf']:
    write.append(i)

with open('mergepdf.pdf','wb') as file:
    write.write(file)   