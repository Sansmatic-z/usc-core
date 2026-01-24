import os

class PayloadHandler:
    @staticmethod
    def get_payload(symbol):
        if symbol.mode == "inline":
            return symbol.data
        elif symbol.mode == "external":
            return PayloadHandler._resolve_external(symbol.data)
        return None

    @staticmethod
    def _resolve_external(reference):
        if not reference:
            return None
        # Minimal implementation: treat reference as a local file path
        if os.path.exists(reference):
            try:
                with open(reference, 'r') as f:
                    return f.read()
            except Exception:
                return f"[Error: Could not read {reference}]"
        return f"[Error: External reference {reference} not found]"
