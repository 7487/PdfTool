import os
from pdf_processor import convert_pdf_to_txt, convert_pdf_to_word, merge_columns_pdf


def batch_process(input_dir, output_dir, operation):
    """
    批量处理PDF文件
    :param input_dir: 输入目录
    :param output_dir: 输出目录
    :param operation: 操作类型（'merge', 'to_word', 'to_text'）
    """
    print("deal %s operation" % operation)
    print("output dir is %s \n" % output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            print("deal with file %s start" % filename)
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0])

            if operation == 'merge':
                merge_columns_pdf(input_path, output_path + '_merged.pdf')
                print("output path is %s_merged.pdf" % output_path)
            elif operation == 'to_word':
                convert_pdf_to_word(input_path, output_path + '.docx')
                print("output path is %s.docx" % output_path)
            elif operation == 'to_text':
                convert_pdf_to_txt(input_path, output_path + '.txt')
                print("output path is %s.txt" % output_path)

            print("deal with file %s done" % filename)

    print("%s finished \n" % operation)
