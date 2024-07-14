import docx

def create_word_file(text):
    doc = docx.Document()
    doc.add_paragraph(text)

    filename = "output.docx"
    doc.save(filename)
    print(f"'{filename}' создан")

if __name__ == "__main__":
    text = input("Введите текст для создания Word-файла: ")
    create_word_file(text)