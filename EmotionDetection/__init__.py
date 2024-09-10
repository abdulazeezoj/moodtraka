import requests
import json


def emotion_detector(text_to_analyze: str):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": { 
            "text": text_to_analyze
        }
    }

    # send request
    res = requests.post(url, headers=headers, data=json. dumps(payload) )

    # read data
    data = json. loads (res.text)

    # parse data
    emotion_preds = data. get("emotionPredictions")

    if not emotion_preds:
        return

    emotion = emotion_preds[0].get("emotion")

    if not emotion:
        return

    main_emotion = sorted(emotion.items(), key=lambda x: x[1])[-1][0]

    return {
        **emotion,
        "dominant_emotion": main_emotion
    }
