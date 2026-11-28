import assistant

def test_repeated_topic_batch_bound_and_reused_matcher(monkeypatch):
    original=assistant.matching_topics;calls=[]
    def match(query):
        calls.append(query)
        return original(query)
    monkeypatch.setattr(assistant,'matching_topics',match)
    record=assistant.query_record(('roi '*4096).strip(),all_matches=True,suggestions=True)
    assert [item['topic'] for item in record['matches']]==['roi']
    assert len(calls)==1 and 'suggestions' not in record
