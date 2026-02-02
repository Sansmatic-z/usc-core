import sys
import os
import base64

def generate_usc_block(file_path, symbol_name):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    ext = os.path.splitext(file_path)[1].lower()
    mime_map = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.mp3': 'audio/mpeg',
        '.wav': 'audio/wav',
        '.py': 'text/python',
        '.json': 'application/json'
    }
    mime_type = mime_map.get(ext, 'application/octet-stream')

    with open(file_path, 'rb') as f:
        data = f.read()
        encoded = base64.b64encode(data).decode('utf-8')

    block = f"""@symbol {symbol_name}
@mode inline
@type {mime_type}
@encoding base64
@data <<
{encoded}
>>
"""
    return block

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 usc_encode.py <file_path> <symbol_name>")
    else:
        print(generate_usc_block(sys.argv[1], sys.argv[2]))
