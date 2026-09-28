from reportlab.pdfgen import canvas

pdf = canvas.Canvas('second.pdf')
pdf.drawString(10, 20, "amir khan ka beta junaid khan ")
pdf.save()

print('between heaven and hell')