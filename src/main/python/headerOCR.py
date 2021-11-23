import cv2
import pytesseract
import re


prog1 = re.compile('.*\D(\d+)\D*')
prog2 = re.compile('.*\D(\d+)\D+(\d+)\D*')
prog3 = re.compile('.*\D(\d+)\D+(\d+)\D+(\d+)\D*')


def process(string):
    extracted = ''
    if string.startswith('Heart'):
        result = prog1.match(string)
        extracted = 'Heart Rate: ' + result.group(1) + ' bpm'
    if string.startswith('PR'):
        result = prog1.match(string)
        extracted = 'PR int.: ' + result.group(1) + ' ms'
    if string.startswith('QR'):
        result = prog1.match(string)
        extracted = 'QRS dur.: ' + result.group(1) + ' ms'
    if string.startswith('QT'):
        result = prog2.match(string)
        extracted = 'QT/QTc: ' + result.group(1) + '/' + result.group(2) + ' ms'
    if string.startswith('P-R'):
        result = prog3.match(string)
        extracted = 'P-R-T axes: ' + result.group(1) + '-' + result.group(2) + '-' + result.group(3)
    return extracted


def ocr(file_path, out_path, tesseract_path, config='--psm 11'):
    image = cv2.imread(file_path)
    head = image[:222, :] # Based on dataset images
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    text = pytesseract.image_to_string(head, lang='eng', config=config)
    res = ''
    for line in text.split('\n'):
        if line.startswith('Heart') or line.startswith('PR') or line.startswith('QRS') or line.startswith(
                'QT') or line.startswith('P-R'):
            res = res + process(line) + '\n'

    f = open(out_path + 'raw.txt', 'w')
    f.write(text)
    f.close()
    f = open(out_path + 'info.txt', 'w')
    f.write(res)
    f.close()

