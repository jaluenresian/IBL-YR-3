from seasons import convert_to_english_words

def test_convert_to_english_words():
    assert convert_to_english_words(0) == "0 minutes"
    assert convert_to_english_words(1) == "1 minute"
    assert convert_to_english_words(60) == "1 hour"
    assert convert_to_english_words(120) == "2 hours"
    assert convert_to_english_words(1440) == "1 day"
    assert convert_to_english_words(288