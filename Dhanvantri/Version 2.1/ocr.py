from paddleocr import PaddleOCR

# Initialize the OCR model
ocr = PaddleOCR()

# Perform OCR on an image
result = ocr.ocr('Version 2.1/received_photo.jpg')

# print(result)

# Access the OCR resul
for line in result[0]:
    print(f'Text: {line[1]}')
