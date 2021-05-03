import argparse

def blur_detector():
    ap = argparse.ArgumentParser()
    ap.add_argument("-if", "--image_folder", required=True, help="Folder where search should begin")
    ap.add_argument("-tf", "--trash_folder", required=True, help="Folder where trash images should end")
    ap.add_argument("-r", "--report", help="Store report operations in JSON file format. Use as: [name_of_your_file].json")
    args = ap.parse_args()
    print(args)

if __name__ == '__main__':
    blur_detector()