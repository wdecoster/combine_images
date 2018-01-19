from imgtools.svg import Svg
from argparse import ArgumentParser


def main():
    args = get_args()
    svgs = [Svg(f) for f in args.images]
    desired_size = min([i.__dict__[args.dimension] for i in svgs])
    if args.dimension == "width":
        [i.scale_width_to_reference(desired_size) for i in svgs]
    else:
        [i.scale_height_to_reference(desired_size) for i in svgs]
    save_all(svgs)


def save_all(svgs):
    for s in svgs:
        s.save(s.file.replace('.svg', '') + "_resized" + ".svg")


def get_args():
    parser = ArgumentParser(description="Make svg images the same size in one dimension.")
    general = parser.add_argument_group(title='General options')
    general.add_argument("-i", "--images",
                         help="images to change size of.",
                         nargs='+',
                         metavar="files",
                         required=True)
    general.add_argument("-d", "--dimension",
                         choices=['width', 'height'],
                         help="Which dimension to use.",
                         default='width')
    return parser.parse_args()


if __name__ == '__main__':
    main()
