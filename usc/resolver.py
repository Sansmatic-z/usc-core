from .payload import PayloadHandler

class USCResolver:
    def __init__(self, document):
        self.document = document
        self.payload_handler = PayloadHandler()

    def resolve_all(self) -> str:
        """Returns the document text with symbols resolved."""
        result = self.document.raw_content
        
        # Sort symbols by length descending to avoid partial matches
        sorted_identifiers = sorted(self.document.symbols.keys(), key=len, reverse=True)
        
        for identifier in sorted_identifiers:
            symbol = self.document.symbols[identifier]
            resolved_value = self.resolve_symbol(symbol)
            result = result.replace(identifier, resolved_value)
            
        return result

    def resolve_symbol(self, symbol) -> str:
        if symbol.is_disabled:
            return symbol.identifier
            
        if symbol.mode == "inline":
            return symbol.data if symbol.data is not None else symbol.identifier
            
        if symbol.mode == "external":
            payload = self.payload_handler.get_payload(symbol)
            return payload if payload is not None else symbol.identifier
            
        # symbolic mode or fallback
        return symbol.identifier
