import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import data, img_as_float, exposure
from skimage.io import imread, imsave, imshow, show



import json
settings = {
    'path_in': 'galaxy.jpg',
    'path_out': 'out.jpg',
    'parameter': 0.5
}
with open('settings.json', 'w') as fp:
    json.dump(settings, fp)

def get_user_parameters():
    with open('settings.json') as json_file:
        json_data = json.load(json_file)
    parameters = {entry: json_data[entry] for entry in json_data.keys()}
    return parameters


def plot_img_and_hist(image, axes, bins=256):
    """Plot an image along with its histogram and cumulative histogram.

    """
    image = img_as_float(image)
    ax_img, ax_hist = axes
    ax_cdf = ax_hist.twinx()

    # Display image
    ax_img.imshow(image, cmap=plt.cm.gray)
    ax_img.set_axis_off()

    # Display histogram
    ax_hist.hist(image.ravel(), bins=bins, histtype='step', color='black')
    ax_hist.ticklabel_format(axis='y', style='scientific', scilimits=(0, 0))
    ax_hist.set_xlabel('Pixel intensity')
    ax_hist.set_xlim(0, 1)
    ax_hist.set_yticks([])

    # Display cumulative distribution
    img_cdf, bins = exposure.cumulative_distribution(image, bins)
    ax_cdf.plot(bins, img_cdf, 'r')
    ax_cdf.set_yticks([])

    return ax_img, ax_hist, ax_cdf

params = get_user_parameters()
input_path = params.get('path_in')
source_img = imread(input_path)

