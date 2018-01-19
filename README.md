## Make svg images the same size
I wrote a script called "same_size_svg" to make svg images the same side for a given dimension.

### INSTALLATION:

`pip install imgtools`

### USAGE
```
same_size_svg [-h] -i files [files ...] [--dimension {width,height}]
                     [--direction {largest,smallest}]

Make svg images the same size in one dimension.

optional arguments:
  -h, --help            show this help message and exit

General options:
  -i/--images files     images to change size of.
  --dimension           Which dimension to use: width (default) or height
```

### EXAMPLES
```
same_size_svg -i myimage1.svg myimage2.svg myimage3.svg
same_size_svg -i *.svg
same_size_svg -i *.svg -- height
```


## combine_images
A bit of Python code to resize and combine images in svg or png format.

See also these blog posts:
* [resizing and combining multiple png images](https://gigabaseorgigabyte.wordpress.com/2017/11/08/resizing-and-combining-multiple-png-images/)
* [resizing and combining multiple svg images](https://gigabaseorgigabyte.wordpress.com/2017/11/15/resizing-and-combining-multiple-svg-images/)



## Contributions welcome!
