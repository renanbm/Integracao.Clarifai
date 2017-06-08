from abc import ABC, abstractmethod

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CLImage

from helpers import Image_Helper


class ClarifaiBase(ABC, object):
    @abstractmethod
    def __init__(self):
        self.instance = ClarifaiApp("t_PWeUfWygWotDHWGPW6llqt2-nxMMTDNdNK1n39", "bDSBvO-qsHqRUcmNwGGCcxgJMr6eursYE4TgnZtb")


class ClarifaiPredictByUrl(ClarifaiBase):
    def __init__(self):
        super(ClarifaiPredictByUrl, self).__init__()
        self.model = self.instance.models.get('general-v1.3')

    def predict_by_url(self, url, language):
        return self.model.predict_by_url(url=url, lang=language)


class ClarifaiDemographics(ClarifaiBase):
    def __init__(self):
        super(ClarifaiDemographics, self).__init__()
        self.model = self.instance.models.get('demographics')

    def predict_demographics_by_url(self, url):
        image = CLImage(url=url)
        return self.model.predict([image])

    def predict_demographics_by_path(self, path):
        imageBase64 = Image_Helper.get_path_as_pure_base64(path)
        image = CLImage(base64=imageBase64)
        return self.model.predict([image])
