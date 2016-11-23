import base64
import sys

if len(sys.argv) != 3:
    print 'Usage: bookmark.py <icon-filename> <website-address>'
else:
    icon_filename = sys.argv[1]
    url = sys.argv[2]
    with open(icon_filename, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())

    metatype = 'data:text/html;base64,'

    prefix = '<html><head><link rel="icon" href="data:image/png;base64,'
    infix = '" type="image/png" /></head><body><script>window.location.href="'
    suffix = '";</script></body></html>'

    print metatype + base64.b64encode(prefix + encoded_image + infix + url + suffix)
