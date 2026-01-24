import sys
import argparse
from usc.parser import USCParser
from usc.resolver import USCResolver

def main():
    parser = argparse.ArgumentParser(description="USC CLI v0.1")
    subparsers = parser.add_subparsers(dest="command")

    # view command
    view_parser = subparsers.add_parser("view", help="View the resolved USC document")
    view_parser.add_argument("file", help="Path to .usc file")

    # symbols command
    sym_parser = subparsers.add_parser("symbols", help="List all symbols in the document")
    sym_parser.add_argument("file", help="Path to .usc file")

    # extract command
    ext_parser = subparsers.add_parser("extract", help="Extract a specific symbol's payload")
    ext_parser.add_argument("symbol", help="Symbol identifier")
    ext_parser.add_argument("file", help="Path to .usc file")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        with open(args.file, 'r') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Error: File {args.file} not found.")
        sys.exit(1)

    parser_engine = USCParser()
    doc = parser_engine.parse(raw_text)

    if args.command == "view":
        resolver = USCResolver(doc)
        print(resolver.resolve_all())

    elif args.command == "symbols":
        if not doc.symbols:
            print("No symbols found.")
        else:
            print(f"{'SYMBOL':<20} {'MODE':<10} {'TYPE':<20}")
            print("-" * 50)
            for sym in doc.symbols.values():
                print(f"{sym.identifier:<20} {sym.mode:<10} {sym.mime_type:<20}")

    elif args.command == "extract":
        if args.symbol in doc.symbols:
            symbol = doc.symbols[args.symbol]
            if symbol.mode == "inline":
                print(symbol.data)
            elif symbol.mode == "external":
                from usc.payload import PayloadHandler
                print(PayloadHandler.get_payload(symbol))
            else:
                print(f"Symbol '{args.symbol}' has no payload (symbolic mode).")
        else:
            print(f"Error: Symbol '{args.symbol}' not found.")

if __name__ == "__main__":
    main()
