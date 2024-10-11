from PIL import Image

def convert_to_ico(input_file, output_file):
    # Open the image file
    with Image.open(input_file) as img:
        # Convert to .ico
        img.save(output_file, format='ICO')

# Example usage
input_file = "C:/Users/goper/Downloads/biomch.png"  # Change this to your file path
output_file = 'your_icon.ico'  # Output file path
convert_to_ico(input_file, output_file)

print(f"Converted {input_file} to {output_file}")
