import os
from sys import exception

import piexif
from PIL import ExifTags, Image, IptcImagePlugin


class exifTools:
    def __init__(self):
        self.image_file = input("Image : ")
        self.main_menu()

    def main_menu(self):
        print("""
            ========EXIF TOOLS========

            1. Show Exif Data
            2. Strip Exif Data

            ==========================
            """)

        ask_user = input("Option : ")

        if ask_user == "1":
            self.get_data(self.image_file)
        elif ask_user == "2":
            self.strip_data()
        else:
            print("\nWrong Option")

    def get_data(self, image):
        with Image.open(image) as im:
            exif_bytes = im.info.get("exif")

            if exif_bytes:
                exif_dict = piexif.load(exif_bytes)

                ifd0 = exif_dict["0th"]
                subifd = exif_dict["Exif"]
                gps = exif_dict["GPS"]

                data: dict = {
                    "Image Width": (ifd0.get(256)),
                    "Image Length": (ifd0.get(257)),
                    "Make": (ifd0.get(271)),
                    "Model": (ifd0.get(272)),
                    "Software": (ifd0.get(305)),
                    "Orientation": (ifd0.get(274)),
                    "Date Time": (ifd0.get(306)),
                    "X Resolution": (ifd0.get(282)),
                    "Y Resolution": (ifd0.get(283)),
                    "Resolution Unit": (ifd0.get(296)),
                    "YCbCr Positioning": (ifd0.get(531)),
                    "Exposure Time": (subifd.get(33434)),
                    "FNumber": (subifd.get(33437)),
                    "Date Time Original": (subifd.get(36867)),
                    "Offset Time Original": (subifd.get(36881)),
                    "Date Time Digitized": (subifd.get(36868)),
                    "Offset Time Digitized": (subifd.get(36882)),
                    "Shutter Speed Value": (subifd.get(37377)),
                    "Aperture Value": (subifd.get(37378)),
                    "Brightness Value": (subifd.get(37379)),
                    "Exposure Bias Value": (subifd.get(37380)),
                    "Max Aperture Value": (subifd.get(37381)),
                    "Metering Mode": (subifd.get(37383)),
                    "Flash": (subifd.get(37385)),
                    "GPS Version": (gps.get(0)),
                    "Latitude Ref": (gps.get(1)),
                    "Latitude": (gps.get(2)),
                    "Longtitude Ref": (gps.get(3)),
                    "Longtitude": (gps.get(4)),
                    "Altitude Ref": (gps.get(5)),
                    "Altitude": (gps.get(6)),
                    "GPS Timestamp": (gps.get(7)),
                    "Degree of Precision": (gps.get(11)),
                    "Processing Method": (gps.get(27)),
                    "GPS Date Stamp": (gps.get(29)),
                }

                for key_tag, value_tag in data.items():
                    print(f"{key_tag}   : {value_tag}")

    def strip_data(self):
        output_folder = "stripped image"
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, self.image_file)

        img = Image.open(self.image_file)

        exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

        exif_bytes = piexif.dump(exif_dict)

        img.save(output_path, "jpeg", exif=exif_bytes)


if __name__ == "__main__":
    run_menu = exifTools()
