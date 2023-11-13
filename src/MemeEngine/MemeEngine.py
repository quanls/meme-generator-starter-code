from PIL import Image, ImageDraw, ImageFont
import random
import os


class MemeEngine:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

    def make_meme(self, img_path: str, text: str, author: str, width=500):
        try:
            with Image.open(img_path) as img:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))

                img = img.resize((width, height))

                draw = ImageDraw.Draw(img)

                loc = (60, random.randint(30, img.size[0] - 50))

                draw.text(loc, text, fill='black')

                draw.text(loc, '\n- ' + author, fill='white')

                out_file = str(random.randint(1, 1000)) + '.png'
                img.save(os.path.normpath(self.output_dir + '/' + out_file))
                return os.path.normpath(self.output_dir + '/' + out_file)
        except:
            raise Exception('Image Path is not valid.')