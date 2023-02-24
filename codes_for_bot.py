from PIL import Image

def words_to_morze(string):
    morze = { 
            'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
            'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
            'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
            'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
            'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
            '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
            '8':'---..', '9':'----.'
    }

    answ = ''
    
    for i in string.upper():
        for key, value in morze.items():
            if i in key:
                answ += f'{value} '
    return answ

def resize_image(image_path, new_size):
    with Image.open(image_path) as image:
        image = image.resize(new_size)
        image.save("resized_image.jpg")

