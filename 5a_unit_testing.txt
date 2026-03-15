import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_anger(self):
        result = emotion_detector("I am very angry today")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_emotion_disgust(self):
        result = emotion_detector("I feel disgusted by this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_emotion_fear(self):
        result = emotion_detector("I am scared about the situation")
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_emotion_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_emotion_sadness(self):
        result = emotion_detector("I am very sad today")
        self.assertEqual(result['dominant_emotion'], 'sadness')


if __name__ == "__main__":
    unittest.main()