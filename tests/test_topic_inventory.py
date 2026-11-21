import json
from assistant import main,available_topics,respond
def test_topic_inventory_is_sorted_complete_and_queryable(capsys):
    assert main(['--topics','--json'])==0
    topics=json.loads(capsys.readouterr().out)
    assert topics==available_topics()==sorted(set(topics))
    assert 'cash flow' in topics and all('not trained' not in respond(t) for t in topics)
