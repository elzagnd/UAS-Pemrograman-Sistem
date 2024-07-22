import os

# Membuat direktori
directory = "C:\\Users\\YourUsername\\Documents\\NewDirectory"

try:
    os.makedirs(directory)
    print(f"Directory '{directory}' created successfully")
except FileExistsError:
    print(f"Directory '{directory}' already exists")
