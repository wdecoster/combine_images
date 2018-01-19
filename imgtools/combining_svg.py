"""
based on https://neuroscience.telenczuk.pl/?p=331
"""

from svg import Svg
import svgutils.transform as sg


def rescale(svgs):
    """Change the dimensions of the images to the desired combinations."""
    svgs['B'].scale_width_to_reference(svgs['A'].width)
    svgs['C'].scale_width_to_reference(svgs['A'].width)
    svgs['D'].scale_width_to_reference(svgs['A'].width)
    assert svgs['A'].width == svgs['B'].width == svgs['C'].width == svgs['D'].width

    svgs['E'].scale_width_to_reference(svgs['F'].width)
    assert svgs['E'].width == svgs['F'].width

    left_height = sum([svgs[i].height for i in ['A', 'B', 'C', 'D']])
    right_height = sum([svgs[i].height for i in ['E', 'F', ]])
    scalings_factor = right_height / left_height
    svgs['A'].scale_by_factor(scalings_factor)
    svgs['B'].scale_by_factor(scalings_factor)
    svgs['C'].scale_by_factor(scalings_factor)
    svgs['D'].scale_by_factor(scalings_factor)
    assert sum([svgs[i].height for i in ['A', 'B', 'C', 'D']]
               ) == sum([svgs[i].height for i in ['E', 'F', ]])


def change_positions(svgs):
    """Move the images to the desired positions."""
    svgs['B'].move(0, svgs['A'].height)
    svgs['C'].move(0, svgs['A'].height + svgs['B'].height)
    svgs['D'].move(0, svgs['A'].height + svgs['B'].height + svgs['C'].height)
    svgs['E'].move(svgs['A'].width, 0)
    svgs['F'].move(svgs['A'].width, svgs['E'].height)


def letter_annotations(svgs):
    """Add letters based on the location of the images."""
    return [sg.TextElement(svg.x + 10, svg.y + 15, letter_annotation, size=15, weight="bold")
            for letter_annotation, svg in svgs.items()]


def files_to_svg_dict(files):
    """Convert a list of images to a dictionary.

    Mapping the image basename to the Svg class instance,
    setting the dimensions based on sizes and coordinates (0,0) by default
    """
    return {
        s.split('.')[0]: Svg(
            file=s,
            coords=(0, 0))
        for s in files}


def main():
    svgs = files_to_svg_dict(["A.svg", "B.svg", "C.svg", "D.svg", "E.svg", "F.svg"])
    rescale(svgs)
    change_positions(svgs)
    full_width = sum([svgs[i].width for i in ['A', 'E']])
    full_height = sum([svgs[i].height for i in ['A', 'B', 'C', 'D']])
    fig = sg.SVGFigure(full_width, full_height)
    text = letter_annotations(svgs)
    fig.append([s.data for s in svgs.values()])
    fig.append(text)
    fig.save("combined.svg")


if __name__ == '__main__':
    main()
