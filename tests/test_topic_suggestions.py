from assistant import query_record

def test_suggestions_never_silently_answer_fuzzy_query():
    record=query_record("proft margin",suggestions=True)
    assert "profit margin" in record["suggestions"] and len(record["suggestions"])<=3
    assert "not trained" in record["answer"]
    assert "suggestions" not in query_record("profit margin",suggestions=True)
    assert "suggestions" not in query_record("proft margin")
