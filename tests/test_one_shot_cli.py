import json
from assistant import main
def test_single_query_json_does_not_read_stdin(monkeypatch,capsys):
    monkeypatch.setattr('builtins.input',lambda _:(_ for _ in ()).throw(AssertionError('stdin')))
    assert main(['cash flow','--json'])==0
    assert 'Cash Inflows' in json.loads(capsys.readouterr().out)['answer']
