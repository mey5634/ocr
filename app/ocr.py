from tesserocr import PyTessBaseAPI

def read_text_from_image(image):
  with PyTessBaseAPI() as api:
      api.SetImageFile(image)
      text = api.GetUTF8Text().strip()
      text = text or ''
      message = {
          'status': 200 if text else 415,
          'caption': text or 'Text not found.'
      }
      #confidence = api.AllWordConfidences()
      #data = {"caption":text,"confidence":confidence}
      return message
