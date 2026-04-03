from reportlab.pdfgen import canvas

def create_menu(dishes):

    pdf = canvas.Canvas("menu.pdf")

    y = 800

    for dish in dishes:

        pdf.drawString(100, y, dish["name"])
        pdf.drawString(400, y, dish["price"])

        y -= 50

    pdf.save()

    return "menu.pdf"