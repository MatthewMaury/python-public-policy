#!/bin/bash

set -e
set -x


DEST=public
rm -r "$DEST"
mkdir "$DEST"

cp -r scripts/templates/ppp/static public

for notebook in *.ipynb
do
  jupyter nbconvert --to html \
    --TemplateExporter.extra_template_basedirs=scripts/templates \
    --template ppp \
    --output-dir="$DEST" \
    "$notebook"
done
