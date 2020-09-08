
from googletrans import Translator, LANGUAGES

sample_text = input("Enter Text")
for language in LANGUAGES:
    t = Translator().translate(sample_text, dest=language)
    print(LANGUAGES[language] , t.text )


