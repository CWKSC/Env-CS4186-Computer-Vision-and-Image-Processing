from PIL import Image

import Util.PillowUtil as PillowUtil

PillowUtil.ForEachPixels(
    Image.new("RGB", (250, 250), "black"), lambda x, y: (x, y, 100)
).show()
