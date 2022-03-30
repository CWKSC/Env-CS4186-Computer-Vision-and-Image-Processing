from PIL import Image

import Util.PillowUtil as PillowUtil

PillowUtil.mapPixel(
    Image.new("RGB", (250, 250), "black"), lambda pixel, x, y: (x, y, 100)
).show()
