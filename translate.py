from deep_translator import GoogleTranslator

text = "Hello, how are you?"
translated = GoogleTranslator(source='auto', target='es').translate(text)

print("Original:", text)
print("Traducido:", translated)
