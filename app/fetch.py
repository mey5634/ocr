import requests
import urlparse
import shutil
import os
CURDIR = os.path.dirname(os.path.realpath(__file__))
ROOTDIR = os.path.abspath(os.path.join(CURDIR, '..'))
TMPDIR = os.path.join(ROOTDIR, 'tmp')

def _is_url(url_candidate):
    return urlparse.urlparse(url_candidate).scheme != ""

def get_data(url_or_filepath):
  '''Takes a URL or path to file, returns path to file that contains JPEG.
  No checks on if the file exists at path.
  '''
  if _is_url(url_or_filepath):
    resp = requests.get(url_or_filepath, stream=True)
    if resp.status_code == 200:
      outfile = os.path.join(TMPDIR, str(hash(url_or_filepath))+'.jpg')
      with open(outfile, 'wb') as f:
          resp.raw.decode_content = True
          shutil.copyfileobj(resp.raw, f)   
      return outfile
    else: return None
  else:
    return url_or_filepath