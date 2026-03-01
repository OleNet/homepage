#!/bin/bash
# build-article.sh - Convert Markdown to HTML for thinking articles
# Usage: ./build-article.sh <markdown-file>

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TEMPLATE="$SCRIPT_DIR/template.html"

if [ -z "$1" ]; then
    echo "Usage: ./build-article.sh <markdown-file>"
    echo "Example: ./build-article.sh drafts/my-article.md"
    exit 1
fi

INPUT="$1"
BASENAME=$(basename "$INPUT" .md)
OUTPUT="$SCRIPT_DIR/$BASENAME.html"

if [ ! -f "$INPUT" ]; then
    echo "Error: File not found: $INPUT"
    exit 1
fi

if [ ! -f "$TEMPLATE" ]; then
    echo "Error: Template not found: $TEMPLATE"
    exit 1
fi

echo "Converting: $INPUT -> $OUTPUT"

pandoc "$INPUT" \
    --template="$TEMPLATE" \
    --from=markdown \
    --to=html5 \
    --standalone \
    --output="$OUTPUT"

echo "Done! Generated: $OUTPUT"
echo ""
echo "Remember to update index.html with the new article link."
