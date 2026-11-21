import pytest
from assistant import respond
def test_compatibility_characters_and_separators_match_existing_topics():
    assert respond('ＲＯＩ')==respond('roi')
    assert respond('cash_flow')==respond('cash flow')
    assert respond('profit/margin')==respond('profit margin')
def test_nontext_query_has_explicit_validation_error():
    with pytest.raises(ValueError,match='text'):respond(None)
def test_topic_matching_keeps_word_boundaries():
    assert 'not trained' in respond('profitable')
