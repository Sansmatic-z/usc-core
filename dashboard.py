import os
import json
import base64
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from usc.parser import USCParser
from usc.resolver import USCResolver
from usc.model import Symbol

# Define the template folder explicitly
app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/parse', methods=['POST'])
def parse_file():
    data = request.json
    path = data.get('path')
    if not os.path.exists(path):
        return jsonify({"error": "File not found"}), 404
    
    try:
        with open(path, 'r') as f:
            raw = f.read()
        
        parser = USCParser()
        doc = parser.parse(raw)
        
        symbols_data = {}
        for name, sym in doc.symbols.items():
            symbols_data[name] = {
                "identifier": sym.identifier,
                "mode": sym.mode,
                "mime_type": sym.mime_type,
                "encoding": sym.encoding,
                "data": sym.data
            }
            
        return jsonify({
            "raw_content": doc.raw_content,
            "symbols": symbols_data,
            "imports": doc.imports
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/encode', methods=['POST'])
def encode_media():
    # Helper to encode local media into USC blocks
    data = request.json
    file_path = data.get('path')
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    
    with open(file_path, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
    
    return jsonify({"base64": encoded})

if __name__ == '__main__':
    print("🚀 Moona's USC Dashboard starting on port 8765...")
    app.run(host='0.0.0.0', port=8765)
