import markdown
import sys

try:
  with open(sys.argv[1], 'r', encoding='utf-8') as f:
      contents = f.read()
  with open(sys.argv[2], 'w', encoding='utf-8') as f:
      f.write(markdown.markdown(contents))
except FileNotFoundError:
  print(f"Error: '{sys.argv[1]}' のファイルは存在しません.")