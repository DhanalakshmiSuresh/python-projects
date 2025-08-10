# File Write and Read Example
with open("sample.txt", "w") as f:
    f.write("Hello, this is a file created with Python!\n")

with open("sample.txt", "r") as f:
    content = f.read()

print("File Content:")
print(content)