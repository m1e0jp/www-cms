#!/bin/bash
source "`dirname "$0"`/config"

md="$contentsdir/templates/main.md"

echo -e "Content-Type: text/html\n"
pandoc --template="$viewdir/template.html" -f markdown_github+yaml_metadata_block "$md"


