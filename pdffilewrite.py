from reportlab.pdfgen import canvas

pdf = canvas.Canvas('second.pdf')
pdf.setFont("Helvetica-Bold", 30)
pdf.drawString(10, 20, "what is pdf file handling")
pdf.setFont("Helvetica", 12)
pdf.drawString(50, 700, "Hello Bhushan")
pdf.save()

print('done')
