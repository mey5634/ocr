import tesserocr
import urllib
import urlparse
import cStringIO
from PIL import Image

def _is_url(url_candidate):
    return urlparse.urlparse(url_candidate).scheme != ""

def parse(url):
    '''Take url or path to file and return OCR'd text. Flag failure 
    with non-200 status code.
    '''
    if _is_url(url):
        try:
            buffer = cStringIO.StringIO(urllib.urlopen(url).read())
            img = Image.open(buffer) 
            text = tesserocr.image_to_text(img).strip()
            return { 'status': 200 if text else 415,
                    'caption': text or 'Text not found.',
                    'url': url}
        except:
            return {'status': 500,
                    'caption': "Couldn't retrieve the image at %s" %url,
                    'ulr': url}
    else: # is path to file
        with tesserocr.PyTessBaseAPI() as api:
            api.SetImageFile(url)
            text = api.GetUTF8Text().strip()
            return { 'status': 200 if text else 415,
                     'caption': text or 'Text not found.',
                     'url': url}
