import re
from .model import Symbol, USCDocument

class USCParser:
    def __init__(self):
        self.symbol_regex = re.compile(r'^@symbol\s+(.+)$')
        self.mode_regex = re.compile(r'^@mode\s+(.+)$')
        self.type_regex = re.compile(r'^@type\s+(.+)$')
        self.encoding_regex = re.compile(r'^@encoding\s+(.+)$')
        self.import_regex = re.compile(r'^@import\s+(.+)$')
        self.data_start_regex = re.compile(r'^@data\s+<<$')
        self.data_end_regex = re.compile(r'^>>$')

    def parse(self, text: str) -> USCDocument:
        doc = USCDocument()
        lines = text.splitlines()
        content_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('@import'):
                match = self.import_regex.match(line)
                if match:
                    doc.imports.append(match.group(1).strip())
                i += 1
                continue

            if line.startswith('@symbol'):
                symbol_data = self._parse_directive_block(lines, i)
                if symbol_data:
                    symbol, next_index = symbol_data
                    doc.symbols[symbol.identifier] = symbol
                    i = next_index
                    continue
            
            content_lines.append(lines[i])
            i += 1
            
        doc.raw_content = "\n".join(content_lines)
        return doc

    def _parse_directive_block(self, lines, start_index):
        identifier = None
        mode = "symbolic"
        mime_type = "text/plain"
        encoding = "none"
        data = None
        
        i = start_index
        while i < len(lines):
            line = lines[i].strip()
            
            sym_match = self.symbol_regex.match(line)
            if sym_match:
                identifier = sym_match.group(1).strip()
                i += 1
                continue
                
            mode_match = self.mode_regex.match(line)
            if mode_match:
                mode = mode_match.group(1).strip()
                i += 1
                continue
                
            type_match = self.type_regex.match(line)
            if type_match:
                mime_type = type_match.group(1).strip()
                i += 1
                continue

            enc_match = self.encoding_regex.match(line)
            if enc_match:
                encoding = enc_match.group(1).strip()
                i += 1
                continue
                
            if self.data_start_regex.match(line):
                i += 1
                data_lines = []
                while i < len(lines):
                    if self.data_end_regex.match(lines[i].strip()):
                        i += 1
                        break
                    data_lines.append(lines[i])
                    i += 1
                data = "\n".join(data_lines)
                break
            
            if not line.startswith('@') and identifier:
                break
            
            if not line.startswith('@') and not data:
                 break
                
            i += 1

        if identifier:
            return Symbol(identifier, mode, mime_type, encoding, data), i
        return None, start_index + 1
