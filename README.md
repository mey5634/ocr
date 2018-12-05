### What

A webservice accepting a path to an image of text and returning OCR'd text:

- using `tesserocr` for OCR
- [Flask](http://flask.pocoo.org/) endpoint

### Prerequisites

1. Install [pyenv](https://github.com/pyenv/pyenv-installer) to set up
   an isolated Python interpreter and workspace
2. Install Python2.7 with `pyenv`: `pyenv install 2.7.15`
3. Set up a workspace:

```shell
pyenv virtualenv 2.7.15 ocr
```

4. `cd` into the repo, run `echo "ocr" > .python-version` to
   activate/deactivate the virtualenv on switching in/out of the directory
5. Install [tesserocr](https://pypi.org/project/tesserocr/) prereqs. On
    MacOS the most expedient way is to `brew install tesseract`.
6. pull in dependencies with `pip install -r requirements.txt`

### Quickstart

Start the dev server with `python app/app.py`.

Test it by sending a path to JPEG (filepath or URL):
```shell
curl -X POST http://127.0.0.1:5001/ \
     -H "Content-type: application/json" \
     -d '{"image":"/Users/myegorov/projects/ocr/test/images/2.jpg"}'

# => {"caption":"Abstract\n\nGood information design depends on clarifying the
# meaningful\nstructure in an image. We describe a computational approach
# to\nstylizing and abstracting photographs that explicitly responds to\nthis
# design goal. Our system transforms images into a line-drawing\nstyle using bold
# edges and large regions of constant color. To do\nthis, it represents images as
# a hierarchical structure of parts and\nboundaries computed using
# state-of-the-art computer vision. Our\nsystem identifies the meaningful
# elements of this structure using a\nmodel of human perception and a record of a
# user's eye movements\nin looking at the photo; the system renders a new image
# using trans-\nformations that preserve and highlight these visual elements.
# Our\n\u2018icin Hiss teececiiie a bee alernntive Snichne chumcedliatic
# re.","img_path":"/Users/myegorov/projects/ocr/test/images/2.jpg","status":200}
```

```shell
curl -X POST \
  http://127.0.0.1:5001/ \
  -H 'Content-Type: application/json' \
  -d '{"image":"https://pbs.twimg.com/media/DthcI5dV4AAR1GO?format=jpg&name=orig"}'

# =>{"caption":"Text not found.","img_path":"/Users/myegorov/projects/ocr/tmp/4880886555319275386.jpg","status":415}
```

Caveat: things are currently brittle -- no validation checks run.
