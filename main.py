from PIL import Image

# Mapeo de caracteres ASCII según la intensidad de píxel
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert('L')

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def write_ascii_in_file(ascii_img):
    with open('ascii_art.txt', 'w') as file:
        file.write(ascii_img)

def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)
    
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ''
    
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + '\n'
    
    print(ascii_img)
    write_ascii_in_file(ascii_img)

# Ruta a la imagen
image_name = input('Enter the image file name (incluede the extension): ')
image_path = f'.//images//{image_name}'
main(image_path)