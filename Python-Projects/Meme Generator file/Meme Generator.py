# Meme Generator

from PIL import Image, ImageDraw, ImageFont

def generate_meme(image_path, text, output_path):
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Resize the image if necessary
        max_width = 500
        if image.width > max_width:
            ratio = max_width / float(image.width)
            new_size = (max_width, int(image.height * ratio))
            image = image.resize(new_size, Image.ANTIALIAS)
        
        # Create a drawing object
        draw = ImageDraw.Draw(image)
        
        # Define the text properties
        font_path = "arial.ttf"  # Path to the font file
        font_size = 30
        font = ImageFont.truetype(font_path, font_size)
        text_color = (255, 255, 255)  # White color
        
        # Calculate the position to center the text
        text_width, text_height = draw.textsize(text, font=font)
        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2
        
        # Add the text to the image
        draw.text((x, y), text, font=font, fill=text_color)
        
        # Save the resulting meme
        image.save(output_path)
        print("Meme generated successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

# Test the meme generator
image_path = "meme_template.jpg"  # Path to the meme template image
text = "Hello World!"  # Custom text for the meme
output_path = "generated_meme.jpg"  # Path to save the generated meme

generate_meme(image_path, text, output_path)




'''
=================================
Test Case:
=================================

27: DeprecationWarning: textsize is deprecated and will be removed in Pillow 10 (2023-07-01). Use textbbox or textlength instead.
  text_width, text_height = draw.textsize(text, font=font)
Meme generated successfully!

'''