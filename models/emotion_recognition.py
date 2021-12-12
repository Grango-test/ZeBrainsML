import torch
from torch.nn.functional import softmax
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

emotion_tokenizer = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")
emotion_model = AutoModelForSequenceClassification.from_pretrained("cointegrated/rubert-tiny2-cedr-emotion-detection")
labels = ['нет эмоций', 'радость', 'грусть', 'удивление', 'страх', 'злость']


def get_prediction(text):
    inputs = emotion_tokenizer(text, return_tensors="pt")
    output = softmax(emotion_model(**inputs).logits, dim=1)
    res = {i[0]: i[1].item() for i in zip(labels, *output)}
    return res
