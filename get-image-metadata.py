from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS, IFD
def get_image_metadata():
   for tag_id, value in exif_data.items():
       tag = TAGS.get(tag_id)
       image_metadata[tag] = value
       if isinstance(value, bytes):
           value = value.decode()
       print(f"{tag}: {value}")
   return image_metadata
def get_geo(exif):
   gps_info = exif.get_ifd(IFD.GPSInfo)
   gps_data = {}
   for key, value in gps_info.items():
       tag = GPSTAGS.get(key)
       gps_data[tag] = value
   return gps_data
def get_coordinates(gps_data):
   lat_ref = 1 if gps_data['GPSLatitudeRef'] == 'N' else -1
   long_ref = 1 if gps_data['GPSLongitudeRef'] == 'O' else -1
   latitude = gps_data['GPSLatitude']
   latitude = float(latitude[0] + (latitude[1]/60) + (latitude[2]/3600))
   longitude = gps_data['GPSLongitude']
   longitude = float(longitude[0] + (longitude[1]/60) + (longitude[2]/3600>
   return latitude*lat_ref, longitude*long_ref
if __name__ == "__main__":
   image_metadata ={}
   gps_data = {}
   # Se define la imagen a ser analizada
   image_name1 = "/home/tabatha/Image1.jpg"
   # Se lee la imagen con usando PIL
   image_object = Image.open(image_name1)
   exif_data = image_object.getexif()
   print("\n∞∞∞ Metadatos de la Imagen ∞∞∞")
   img_metadata = get_image_metadata()
   gps_results = get_geo(exif_data)
   if gps_results:
       print("\n∞∞∞ Datos GPS ∞∞∞")
       print(gps_results)

