from docxtpl import DocxTemplate

    

doc = DocxTemplate("demo.docx")
context = {
    "id": "title",
    "Document": "пока"
}
doc.render(context)

doc.save("generated.docx")