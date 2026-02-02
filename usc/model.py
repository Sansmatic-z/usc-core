from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class Symbol:
    identifier: str
    mode: str  # inline, external, symbolic
    mime_type: Optional[str] = None
    encoding: Optional[str] = "none"
    data: Optional[str] = None
    is_disabled: bool = False

@dataclass
class USCDocument:
    symbols: Dict[str, Symbol] = field(default_factory=dict)
    imports: list = field(default_factory=list)
    raw_content: str = ""
