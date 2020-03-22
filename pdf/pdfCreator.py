from reportlab.pdfgen import canvas

def generate_label(id,name,birthday,adress,phone_numer,doctor,insurancer):
    f = "files/" + str(id) + ".pdf"
    c = canvas.Canvas(f,pagesize=(97,42.3))
    c.setFontSize(6)
    c.drawString(2, 35, name)
    c.drawString(2, 29, birthday)
    c.drawString(2, 23, adress)
    c.drawString(2, 17, "Tel: " + phone_numer)
    c.drawString(2, 11, "Arzt: " + doctor)
    c.drawString(2, 5, insurancer)
    #c.showPage()
    c.save()
    return f
