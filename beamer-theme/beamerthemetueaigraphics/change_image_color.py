from PIL import Image
import numpy as np
import fire
from tueplots.constants.color import rgb


def transform_to_dark(img, base_color):
    dark = 1 - base_color
    arr = np.float32(np.array(img))
    im_rescaled = 1.0 - arr / 254  # / np.max(arr)
    im_projected = im_rescaled * dark.reshape([1, 1, 3])
    im_projected -= np.min(im_projected)
    im_projected /= np.max(im_projected)
    return Image.fromarray(np.uint8((1.0 - im_projected) * 254))


def make_dark(i, o=None, base_color=rgb.tue_ai_darkblue):
    """
    A little tool to match the tone of B/W images to the tue ai color theme.

    Usage from the CLI:
    python change_image_color.py -i "input_image.png" -o "output_image.png" --base_color=rgb.tue_ai_darkblue

    The base_color can be any color from the tueplots.constants.color.rgb module, or any other rgb triple.

    Philipp Hennig, 2026
    """
    if o == None:
        o = i

    inimg = Image.open(i)
    inimg = inimg.convert("RGB").convert("L").convert("RGB")
    transformed = transform_to_dark(inimg, base_color)
    transformed.show()
    transformed.save(o)


if __name__ == "__main__":
    fire.Fire(make_dark)
