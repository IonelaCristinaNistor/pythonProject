from pathlib import Path

# Absolute path
# Relative path

path = Path() # if we don't pass an argument here, this will reference to current directory
print(path.glob('*.py'))

for file in path.glob('*'):
    print(file)
