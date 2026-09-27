from reportlab.pdfgen import canvas
pdf=canvas.Canvas('first.pdf')
pdf.drawString(10,20,"Welcome to pdf file handling")
pdf.save()