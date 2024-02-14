import base64
import sys

def encode_to_base64(input_filename, output_filename):
    try:
        with open(input_filename, 'rb') as f:
            content = f.read()
            encoded_content = base64.b64encode(content)
            with open(output_filename, 'wb') as output_file:
                output_file.write(encoded_content)
        print(f"文件 {input_filename} 已转换并保存到 {output_filename}")
    except FileNotFoundError:
        print("文件未找到，请检查文件名和路径是否正确。")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法: python script.py <输入文件> <输出文件>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    encode_to_base64(input_filename, output_filename)

