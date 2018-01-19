"""
based on https://neuroscience.telenczuk.pl/?p=331
"""

import svgutils.transform as sg


class Svg(object):
    "svg files with a data object (the svg), width, height and coordinates"

    def __init__(self, svgfile, coords=(0, 0)):
        self.file = svgfile
        self.data = sg.fromfile(svgfile).getroot()
        self.dim = self.get_size()
        self.width = self.dim[0]
        self.height = self.dim[1]
        self.x = coords[0]
        self.y = coords[1]

    def scale_width_to_reference(self, reference_width):
        """Proportionally scale the image to a given width."""
        scalings_factor = reference_width / self.width
        self.data.moveto(0, 0, scale=scalings_factor)
        self.width = self.width * scalings_factor
        self.height = self.height * scalings_factor

    def scale_height_to_reference(self, reference_height):
        """Proportionally scale the image to a given height."""
        scalings_factor = reference_height / self.height
        self.data.moveto(0, 0, scale=scalings_factor)
        self.width = self.width * scalings_factor
        self.height = self.height * scalings_factor

    def scale_by_factor(self, scalings_factor):
        """Proportionally scale image by a scaling factor."""
        self.data.moveto(0, 0, scale=scalings_factor)
        self.width = self.width * scalings_factor
        self.height = self.height * scalings_factor

    def move(self, x, y):
        """Move the coordinates of an image."""
        self.data.moveto(x, y)
        self.x = x
        self.y = y

    def get_size(self):
        """Naively parse the svg text file to get the width and height."""
        with open(self.file) as svg:
            for line in svg:
                if line.startswith('<svg'):
                    paramdict = {e.split('="')[0]: e.split('="')[1] for e in line[5:-3].split('" ')}
                    break
        return (round(float(paramdict["width"].replace('pt', ''))),
                round(float(paramdict["height"].replace('pt', ''))))

    def save(self, newname):
        fig = sg.SVGFigure(self.width, self.height)
        fig.append(self.data)
        fig.save(newname)
