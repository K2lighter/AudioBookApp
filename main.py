from gtts import gTTS
import pdfplumber
from art import tprint
from pathlib import Path


def pdf_to_mp3(file_path="test.pdf", language="ru"):
    """Проверка на существование файла, и если он имеет формат .pdf"""
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        # return "File exists!!!"

        print(f'Original file: {Path(file_path).name}')
        print(f'Processing...')

        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = " ".join(pages)

        # with open("text1.txt", 'w') as file:  # проверка как файл бы выглядел при обработке без replace("\n", " ")
        #     file.write(text)

        text = text.replace("\n", " ")  # нужен для того чтобы при проигрывание текста не было длительных пауз

        # with open("text2.txt", 'w') as file: # проверка как файл бы выглядел при обработке с replace("\n", " ")
        #     file.write(text)

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")

        return f"{file_name}.mp3 was saved successfully"
    else:
        return "File not exists((("


def main():
    tprint("PDF>>TO>>MP3", font="bulbhead")
    file_path = input("\nEnter a file's path: ")
    # C:\\Users\\lighter\\Desktop\\Люблю тебя.pdf
    # C:\\Users\\lighter\\Desktop\\Shine bright like a diamond.pdf
    language = input("Choose language 'en' or 'ru': ")
    # en , ru
    print(pdf_to_mp3(file_path, language))


if __name__ == "__main__":
    main()
