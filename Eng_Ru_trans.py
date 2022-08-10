from textblob import TextBlob

from py3langid.langid import classify

def tr_string(t):
    try:
        text = TextBlob(t)
        l = classify(t)
        return text.translate(from_lang=l[0], to="ru")
    except:
        return "Перевод невозможен"