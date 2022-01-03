## The Best Way to Load An Image
So far the best way I know of is the following

```python
from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ImageOps import exif_transpose

INV_TAGS = {info: id_ for id_, info in TAGS.items()}
def pil_loader(path: Union[str, Path]):
    with open(path, "rb") as f:
        image = Image.open(f)
        exif_data = None
        try:
            exif_data = image._getexif()
        except:
            pass
        if exif_data:
            orientation = exif_data.get(INV_TAGS["Orientation"])
            if orientation:
                image = exif_transpose(image)
        # If RGB images are uniformly desired,
        # instead of inhomogeneous RGBA, gray-scale images,
        # then uncomment the next line
        #image = image.convert("RGB")
        return image
```

The lengthiness is due to consideration of Exif.

