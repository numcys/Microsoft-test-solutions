def safe_read(filename):
  try:
    with open(filename, 'r') as f:
      return f.read()
  except FileNotFoundError:
    return "File not found!"

print(safe_read("q3.py"))