#!/bin/bash
source "`dirname "$0"`/config"

md="$contentsdir/templates/main.md"

pandoc --template="$viewdir/template.html" -f markdown_github+yaml_metadata_block "$md"

