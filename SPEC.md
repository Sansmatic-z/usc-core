# USC Specification — Draft v0.1

## 1. Purpose
USC (Universal Semantic Container) defines a universal symbolic container capable of representing text, logic, media, and structured data within a single readable file.

---

## 2. Symbols
A symbol is any named identifier (e.g., `abcd`).
A symbol has **one identity** but **multiple roles**. The role is determined by the context of use, not the symbol itself.

### Roles:
- **Plain:** Rendered as literal text.
- **Embedded:** Holds media/data payload.
- **Logical:** Executes or expands into code/behavior.
- **Hybrid:** Simultaneously holds payload and logical instructions.

---

## 3. Payload Modes

### 3.1 Inline
Payload data is stored directly inside the `.usc` file, encoded in a dense symbolic block.
- **Size Limit:** 0 bytes – 100 MB.

### 3.2 External
Payload is referenced via a stable path, URL, or hash (e.g., `@embed external ./data.db`).

### 3.3 Symbolic-only
The symbol has no attached data; it exists purely for meaning or as a logical handle.

---

## 4. Resolution Rules (v0.1)
When the USC engine encounters a symbol, it resolves it using the following precedence:
1. **User Override:** If the user has explicitly disabled embedding for this instance.
2. **Local Payload:** If an inline payload is defined for the symbol.
3. **External Reference:** If an external path is provided.
4. **Symbolic Fallback:** Resolves to the symbol name itself (as text).

---

## 5. Safety Model
- **No execution by default.**
- **User-controlled activation:** The user must explicitly click/enable a symbol to trigger its logical or media role.

---

## 6. Versioning
All USC files must declare a version header.
```
@usc_version 0.1
```

---

## 7. Disclaimer
This specification is experimental and subject to change.