import os
import shutil
import random
import string
from functools import reduce
# Performs basic math operations (add/subtract/multiply/divide) on a list of numbers with error handling
def calculate(operation, numbers):
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else None
    }   
    try:
        nums = list(map(float, numbers))
        result = reduce(operations[operation], nums)
        return result
    except (ValueError, KeyError):
        raise ValueError("Invalid operation or numbers")
# Organizes files in a directory into subfolders based on their extensions, with error handling for missing directories or move failures  
def organize_files(directory, extensions):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directory not found")
            
        for file in os.listdir(directory):
            if any(file.endswith(ext) for ext in extensions):
                ext_folder = os.path.join(directory, ext_folder.strip('.'))
                os.makedirs(ext_folder, exist_ok=True)
                shutil.move(os.path.join(directory, file), ext_folder)
                
        return "Files organized successfully"
    except Exception as e:
        raise Exception(f"Error organizing files: {str(e)}")  
#  Generates a random password of specified length with optional special characters
def generate_password(length=12, use_special_chars=True):
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation
        
    password = [random.choice(chars) for _ in range(length)]
    return ''.join(password)
