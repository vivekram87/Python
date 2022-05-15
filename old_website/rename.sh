for file in *.html; do
  name=$(basename "$file" .html)
  mv "$file" "$name.HTM"
done
