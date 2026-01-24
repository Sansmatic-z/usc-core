# USC Specification (v0.1)

## 1. Introduction
USC (Universal Structured Container) is a format where **text is the primary surface**. It introduces **symbols** as first-class citizens that can carry **payloads** without obscuring the human-readable nature of the document.

## 2. Core Concepts

### 2.1 Symbols
A **symbol** is a unique identifier (e.g., `abcd`) used within the document.
- It is case-sensitive (default for v0.1).
- It can be embedded multiple times in the text.
- It resolves to a payload or literal text based on the resolution engine.

### 2.2 Payloads
A **payload** is data associated with a symbol.
- **Max Size:** 100 MB.
- **Type:** Defined by MIME type (e.g., `text/plain`, `image/png`, `application/json`).
- **Immutability:** Payloads are considered immutable by default in v0.1.

### 2.3 Payload Modes
1.  **Inline**: The data is stored directly within the `.usc` file, encoded in a dense block.
2.  **External**: The data is referenced via a stable descriptor (Path, URL, Hash).
3.  **Symbolic**: No payload exists; the symbol acts as a marker or variable.

## 3. File Format (v0.1)
The `.usc` file is a plain text file encoded in UTF-8.

### 3.1 Syntax
The format consists of **Directive Blocks** and **Content**.

#### Directive Block
Defines a symbol's properties. Must appear before the symbol is used or at the top of the scope.

```text
@symbol <identifier>
@mode <inline|external|symbolic>
@type <mime_type>
@data <<
<content>
>>
```

- `@symbol`: The identifier string.
- `@mode`: The storage mode.
- `@type`: MIME type of the content.
- `@data << ... >>`: The delimiter for inline content.

#### Content
The rest of the file is free-form text. Occurrences of the `<identifier>` are treated as symbolic references.

### 3.2 Example
```text
@symbol greeting
@mode inline
@type text/plain
@data <<
Hello, World!
>>

The system says: greeting
```

## 4. Resolution Rules (v0.1)
The resolution engine follows this strict order:

1.  **Disabled Check**: If the symbol is flagged as "disabled" (literal), return the symbol name string.
2.  **Inline Resolution**: If mode is `inline`, return the decoded content from the `@data` block.
3.  **External Resolution**: If mode is `external`, fetch/read the resource from the reference.
4.  **Symbolic Fallback**: If mode is `symbolic` (or no payload), return the symbol name string.

## 5. Non-Goals (v0.1)
- **Execution**: The engine does NOT execute code. It only retrieves it.
- **Compression**: No automatic compression of inline blocks.
- **Encryption**: No built-in encryption.
- **UI**: No graphical interface.
