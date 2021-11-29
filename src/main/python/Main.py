import sys
import os
from tqdm import tqdm
from headerOCR import *
from metadata import metadata
from controllers.MainController import MainController
from fbs_runtime.application_context.PyQt5 import ApplicationContext
import configparser

config = configparser.ConfigParser()
config.read('..\\..\\..\\config.ini')
RECORDS_PATH = config['DEFAULT']['RECORDS_PATH']
OUT_PATH = config['DEFAULT']['OUT_PATH']
METADATA_PATH = config['DEFAULT']['METADATA_PATH']
tesseract_path = config['DEFAULT']['tesseract_path']

context = ApplicationContext()
controller = MainController()

def preprocess(image_path, csv_path):
    controller.setImageFile(image_path)
    controller.digitization(csv_path, 'Comma')
    controller.closeImageFile()


def preprocess_files(records_path=RECORDS_PATH, out_path=OUT_PATH, metadata_path=METADATA_PATH):
    images = os.listdir(records_path)
    if '.paperecg' in images:
        images.remove('.paperecg')
    for image in tqdm(images, colour='blue'):
        if os.path.isfile(records_path + image):
            file_name = image.split('.')[0]
            out_folder = out_path + '\\' + file_name + '\\'
            if not os.path.exists(out_folder):
                os.makedirs(out_folder)
            try:
                metadata(image, records_path, metadata_path)
                preprocess(records_path + image, out_folder + file_name + '.csv')
                ocr(records_path + image, out_folder, tesseract_path)
            except:
                print()
                print(f'Error in file {records_path+image}')
    return


if __name__ == "__main__":
    print('Processing...')
    preprocess_files()
    print('Done!')
    sys.exit(0)
