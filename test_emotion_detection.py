from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        self.assertEqual(
            emotion_detector("I am glad this happened").get("dominant_emotion"),
            "joy"
        )
        self.assertEqual(
            emotion_detector("I am really mad about this").get("dominant_emotion"),
            "anger"
        )
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this").get("dominant_emotion"),
            "disgust"
        )
        self.assertEqual(
            emotion_detector("I am so sad about this").get("dominant_emotion"),
            "sadness"
        )
        self.assertEqual(
            emotion_detector("I am really afraid that this will happen").get("dominant_emotion"),
            "fear"
        )

if __name__ == '__main__':
    unittest.main()
