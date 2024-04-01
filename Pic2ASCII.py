from PIL import Image

# Get the path of the picture that do you want transform to Ascii art
path = input('Write the picture path, ideally the relative path: ')

# Open picture
picture = Image.open(path)

# Resize picture
picture_x_size = picture.size[0]
picture_y_size = picture.size[1]
scale_y = 0.1
scale_x = 0.095
new_y_size = int(picture_y_size * scale_y)
new_x_size = int(picture_x_size * scale_x)
picture_resized = picture.resize((new_x_size, new_y_size))

# Convert the picture to gray scale
picture_grayscale = picture_resized.convert("L")

# ASCII characters for mapping gray tones
ascii_characters = '@%#*+=-:. '
ascii_characters_v2 = ' .:-=+*#%@'

# Function to encapsule the draw logic
def draw_character(y_size, x_size, ascii_chars):
    ascii_art = ''
    
    for y in range(y_size):
        for x in range(x_size):
            intensity = picture_grayscale.getpixel((x,y))
            character_index = intensity * (len(ascii_chars) - 1) // 255 # we use the // operator to get an int value
            ascii_art += ascii_chars[character_index]
        ascii_art = ascii_art + '\n'
        
    return ascii_art

# Draw the character with both strings version to see which is better
draw_1 = draw_character(new_y_size, new_x_size, ascii_characters)
draw_2 = draw_character(new_y_size, new_x_size, ascii_characters_v2)
info = '''So now you have it, you can use it for anything you want, who knows, make a little surprise to your gf or bf, hahaha.
If you want to make some changes or modify something you can do it.'''

# Save or display the ASCII art
with open('ascii_art.txt', 'w') as file:
    file.write(draw_1)
    file.write('\n')
    file.write(draw_2)
    file.write('\n')
    file.write(info)
    




