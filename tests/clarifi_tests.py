import unittest
import Integracao
import helpers.Image_Helper as ImageHelper


class ClarifaiTests(unittest.TestCase):
    def test_predict_demographics_by_image(self):
        imagebase64 = ImageHelper.get_path_as_pure_base64(r"C:\\Users\mr0028\Desktop\17894326.jpg")
        result = predict_demographics_by_image(imagebase64)
        self.assertTrue(result == True)
        
    def test_predict_by_url(self):
        result = predict_by_url(r'https://samples.clarifai.com/metro-north.jpg', 'pt')
        self.assertTrue(result == True)

    def test_predict_demographics_by_url(self):
        result = predict_demographics_by_url(r"https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAmRAAAAJDMyMTM0NGE3LWJkZmMtNDNjZi04Y2U1LWQxYjdkYjFmZjJmYQ.jpg")
        self.assertTrue(result == True)

    def test_predict_demographics_by_path(self):
        result = predict_demographics_by_path(r"C:\\Users\mr0028\Desktop\17894326.jpg")
        self.assertTrue(result == True)


def predict_demographics_by_image(imageBase64):
    instancia = Integracao.ClarifaiDemographics()
    result = instancia.predict_demographics_by_image(imageBase64)
    return checkJson(result)


def predict_by_url(url, language):
    instancia = Integracao.ClarifaiPredictByUrl()
    result = instancia.predict_by_url(url, language)
    return checkJson(result)


def predict_demographics_by_url(url):
    instancia = Integracao.ClarifaiDemographics()
    result = instancia.predict_demographics_by_url(url)
    return checkJson(result)


def predict_demographics_by_path(path):
    instancia = Integracao.ClarifaiDemographics()
    result = instancia.predict_demographics_by_path(path)
    return checkJson(result)


def checkJson(jsonContents):
    test = True if "description" in jsonContents["status"] and jsonContents["status"]["description"] == "Ok" else False
    return test


def main():
    unittest.main()

if __name__ == '__main__':
    main()
