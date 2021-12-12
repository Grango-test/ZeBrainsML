import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("setu4993/LaBSE")

model = AutoModel.from_pretrained("setu4993/LaBSE")
model = model.eval()


def similarity(emb1, emb2):
    nemb1 = F.normalize(emb1, p=2)
    nemb2 = F.normalize(emb2, p=2)
    return torch.cosine_similarity(nemb1, nemb2).item()


def find_similarity(text1, text2):
    input1 = tokenizer([text1], return_tensors="pt", padding=True)
    input2 = tokenizer([text2], return_tensors="pt", padding=True)
    with torch.no_grad():
        output1 = model(**input1)
        output1 = output1.pooler_output

        output2 = model(**input2)
        output2 = output2.pooler_output

    return similarity(output1, output2)



