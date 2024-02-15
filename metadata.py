from PIL import Image
from PIL.ExifTags import TAGS
import os

# path to the image
metaimg = input("path to the image:")
# read the image data using PIL
image = Image.open(metaimg)

# extract EXIF data
exifdata = image.getexif()

# extract other basic metadata
print("__________________METADATA___________________")
info = {
    "Filename": os.path.basename(image.filename),
    "Image Size in MB": os.path.getsize(metaimg) / (1024*1024),# size in MB
    "Image Format": image.format,
    "Image Mode": image.mode
}

for label,value in info.items():
    print(f"{label:20}: {value}")

# Get the tag name, instead of human unreadable tag id
tag_needed=['DateTime','Make','Model','GPSInfo']
# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    # If the tag is one of the tags of interest
    if tag in tag_needed:
        data = exifdata.get(tag_id)
    # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:20}: {data}")

print("_____________________________________________")
