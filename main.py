import argparse
from pdf_processor import convert_pdf_to_txt, convert_pdf_to_word, merge_columns_pdf
from batch_processor import batch_process


def main():
    parser = argparse.ArgumentParser(description='PDF处理工具')
    subparsers = parser.add_subparsers(dest='command')

    # 子命令：merge
    merge_parser = subparsers.add_parser('merge', help='合并PDF')
    merge_parser.add_argument('--input', required=True, help='输入PDF文件路径')
    merge_parser.add_argument('--output', required=True, help='输出PDF文件路径')

    # 子命令：to_word
    to_word_parser = subparsers.add_parser('to_word', help='转换PDF为Word')
    to_word_parser.add_argument('--input', required=True, help='输入PDF文件路径')
    to_word_parser.add_argument('--output', required=True, help='输出Word文件路径')

    # 子命令：to_text
    to_text_parser = subparsers.add_parser('to_text', help='转换PDF为文本')
    to_text_parser.add_argument('--input', required=True, help='输入PDF文件路径')
    to_text_parser.add_argument('--output', required=True, help='输出文本文件路径')

    # 子命令：batch
    batch_parser = subparsers.add_parser('batch', help='批量处理PDF文件')
    batch_parser.add_argument('--input_dir', required=True, help='输入目录')
    batch_parser.add_argument('--output_dir', required=True, help='输出目录')
    batch_parser.add_argument('--operation', required=True, choices=['merge', 'to_word', 'to_text'], help='批量操作类型')

    args = parser.parse_args()

    if args.command == 'merge':
        merge_columns_pdf(args.input, args.output)
    elif args.command == 'to_word':
        convert_pdf_to_word(args.input, args.output)
    elif args.command == 'to_text':
        convert_pdf_to_txt(args.input, args.output)
    elif args.command == 'batch':
        batch_process(args.input_dir, args.output_dir, args.operation)


if __name__ == '__main__':
    main()
