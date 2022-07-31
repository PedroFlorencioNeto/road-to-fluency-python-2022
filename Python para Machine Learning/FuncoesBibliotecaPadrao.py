import re

palavra = r'Pedro Florencio'

print(re.search(r'edro', palavra).group(0))