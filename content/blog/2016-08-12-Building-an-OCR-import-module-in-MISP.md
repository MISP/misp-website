---
title: Building an OCR import module in MISP
banner: /img/blog/misp-small.png
date: 2016-08-12
layout: post
---

## Building an Optical Character Recognition module in MISP

When collecting information from different places, analysts need sometime to perform OCR on documents (like report, faxes, images)
to import and correlate the information in their MISP instance. As MISP 2.4.50 introduced a new modular
framework for export and import modules, we decided to build a simple OCR service accessible to MISP user on a local instance.
This shows how easy you can extend MISP with the [new modules framework](https://github.com/MISP/misp-modules/).

The complete code of the OCR MISP module is the following:
 
```python
import json
import base64

from PIL import Image

from pytesseract import image_to_string
from io import BytesIO
misperrors = {'error': 'Error'}
userConfig = { };

inputSource = ['file']

moduleinfo = {'version': '0.1', 'author': 'Alexandre Dulaunoy',
              'description': 'Optical Character Recognition (OCR) module for MISP',
              'module-type': ['import']}

moduleconfig = []


def handler(q=False):
    if q is False:
        return False
    r = {'results': []}
    request = json.loads(q)
    image = base64.b64decode(request["data"])
    image_file = BytesIO(image)
    image_file.seek(0)
    ocrized = image_to_string(Image.open(image_file))
    freetext = {}
    freetext['values'] = ocrized
    freetext['types'] = ['freetext']
    r['results'].append(freetext)
    return r


def introspection():
    modulesetup = {}
    try:
        userConfig
        modulesetup['userConfig'] = userConfig
    except NameError:
        pass
    try:
        inputSource
        modulesetup['inputSource'] = inputSource
    except NameError:
        pass
    return modulesetup


def version():
    moduleinfo['config'] = moduleconfig
    return moduleinfo

if __name__ == '__main__':
    x = open('test.json', 'r')
    handler(q=x.read())
```

The import module framework is based on the [same model as the expansion services](https://www.circl.lu/assets/files/misp-training/first2016/1-MISP-modules.pdf). So the important part is to define the inputSource that will be supported by your module. In our case, the file type is used as the user will upload image files from the MISP interface. Then the module will take the input encoded Base64 and then can process it (in our case perform the OCR with tesseract). When the data are scanned, the full input is passed back to MISP as freetext. Freetext allows misp to search for potential indicators in a raw text block.

The module is automatically integrated in MISP via the [misp-modules framework](https://github.com/MISP/misp-modules).

An analyst will have access to the following MISP user-interfaces while using the OCR module. The module just work like an expansion module and the user will see all the potential indicators scanned from the document. The OCR module is included as an example in the misp-modules framework and can be directly enabled in the MISP configuration. In order to use the module, the [Tesseract OCR](http://miphol.com/muse/2013/05/install-tesseract-ocr-on-ubunt.html) have to be installed locally on your MISP instance.

![MISP user interface listing the modules and showing the ocr module](/img/blog/ocr1.png){:class="img-responsive"}

![MISP ocr module - scan a file](/img/blog/ocr2.png){:class="img-responsive"}

![MISP ocr module - import scanned results](/img/blog/ocr3.png){:class="img-responsive"}

