# class Report:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#     def generate_pdf(self):
#         print("PDF generated")
#     def save_to_file(self, filename):
#         print(f"Saved {filename}")

from dataclasses import dataclass
import os

@dataclass()
class Data():
    """Хранит данные"""
    title: str
    content: str | list[str] | dict[str, str] | bytes

class PdfGenerator:
    """Генерирует PDF(условно)"""
    @staticmethod
    def generate(data):
        return {
            'title': data.title,
            'content': data.content
        }

class ReportSaver:
    """Сохраняет в файл(условно)"""
    @staticmethod
    def save_to_file(content, filename):
        print(f"Сохраняем {content} в {filename}")
        return os.path.abspath(filename)

data = Data(title="Annual Report", content="This is report content")
pdf = PdfGenerator.generate(data)
file = ReportSaver.save_to_file(pdf, 'report.pdf')
