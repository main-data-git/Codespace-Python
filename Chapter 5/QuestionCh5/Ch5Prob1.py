hindi_dictoanry = {
    "hello": "नमस्ते",
    "goodbye": "अलविदा",
    "please": "कृपया",
    "thank you": "धन्यवाद",
    "yes": "हाँ",
    "no": "नहीं"
}



key_word = input("Enter an English word: ").lower()

print(hindi_dictoanry.get(key_word, "Word not found in dictionary."))