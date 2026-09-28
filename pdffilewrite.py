from reportlab.pdfgen import canvas

pdf = canvas.Canvas('second.pdf')
pdf.drawString(10, 20, "what is file handling")
pdf.save()

print('done')