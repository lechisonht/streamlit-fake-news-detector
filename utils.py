import pandas as pd
import re
import base64
import requests
import numpy as np



url = 'https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/master/vietnamese-stopwords.txt'
req = requests.get(url)
vn_stop_words = req.text

vn_stop_words = vn_stop_words.splitlines()

def remove_stopword(text):
    text = text.lower()
    for i in range(len(vn_stop_words)):
        stop_word = vn_stop_words[i]
        stop_word = stop_word.strip()
        stop_word = " " + stop_word + " "
        text = text.replace(stop_word, ' ')
    return text

def stemming(text):
    text = remove_stopword(text)
    text = re.sub(r"[^a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯĂẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỀỂẾưăạảấầẩẫậắằẳẵặẹẻẽềềểếỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ0-9^,!.\/'+-=]", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub(r"\'", " ", text)
    text = re.sub(r"@", " ", text)
    text = text.strip('_')
    text = text.strip('*')
    text = re.sub(' +', ' ',text)
    #text = unidecode.unidecode(text)
    return text

def text_preprocessing(text):
    return stemming(text)
