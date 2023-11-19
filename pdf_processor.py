import os
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2 import PageObject
from pdf2docx import Converter
import fitz


def batch_process(input_dir, output_dir, operation):
    """
    批量处理PDF文件
    :param input_dir: 输入目录
    :param output_dir: 输出目录
    :param operation: 操作类型（'merge', 'to_word', 'to_text'）
    """
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0])

            if operation == 'merge':
                merge_columns_pdf(input_path, output_path + '_merged.pdf')
            elif operation == 'to_word':
                convert_pdf_to_word(input_path, output_path + '.docx')
            elif operation == 'to_text':
                convert_pdf_to_txt(input_path, output_path + '.txt')


def convert_pdf_to_txt(pdf_file_path, txt_file_path):
    """
    pdf tool
    :param pdf_file_path:
    :param txt_file_path:
    :return:
    """
    # 打开PDF文件
    doc = fitz.open(pdf_file_path)

    # 创建一个空字符串来收集文本
    full_text = ""

    # 遍历每一页
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # 获取当前页面
        text = page.get_text()  # 提取页面文本
        full_text += text  # 将文本添加到全文中

    # 将提取的文本写入TXT文件
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(full_text)

    # 关闭PDF文档
    doc.close()


def convert_pdf_to_word(pdf_file_path, word_file_path):
    # 创建一个转换器实例
    cv = Converter(pdf_file_path)

    # 转换整个PDF
    cv.convert(word_file_path)

    # 关闭转换器
    cv.close()


def merge_columns_pdf(input_path, output_path):
    reader = PdfReader(input_path)  # 使用PdfReader读取指定路径的PDF文件
    writer = PdfWriter()  # 创建PdfWriter对象，用于写入修改后的PDF内容

    for page in reader.pages:
        # 获取每一页的原始尺寸（宽度和高度）
        original_width = page.cropbox.upper_right[0]
        original_height = page.cropbox.upper_right[1]

        # 创建一个新页面，宽度为原页面宽度的一半，高度为原页面的两倍
        new_page_left = PageObject.create_blank_page(width=original_width / 2, height=original_height)
        # 再创建一个新页面,宽度高度不变
        new_page_right = PageObject.create_blank_page(width=original_width, height=original_height)

        new_page_left.merge_page(page)
        new_page_right.merge_page(page)

        # 将修改后的新页面添加到PDF写入器中
        writer.add_page(new_page_left)
        new_page_right.cropbox.lower_left = [original_width / 2, 0]
        writer.add_page(new_page_right)

    # 将所有修改后的页面写入到新的PDF文件中
    with open(output_path, 'wb') as output_file:
        writer.write(output_file)

    return output_path

