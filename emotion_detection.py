import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        try:
            #print(result)
            text_value = result['emotionPredictions'][0]['emotionMentions'][0]['span']['text']
            return text_value
        except (KeyError, IndexError):
            return "Could not extract text value."
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
