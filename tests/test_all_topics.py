import json
from assistant import matching_topics, main, respond

def test_specific_overlaps_and_distinct_mentions():
    assert matching_topics("profit margin and ROI and profit margin and profit")==["profit margin","roi","profit"]
    assert respond("profit margin and ROI").startswith("Profit Margin")

def test_multitopic_cli(capsys):
    assert main(["profit margin and ROI","--all-matches","--json"])==0
    record=json.loads(capsys.readouterr().out)
    assert [m["topic"] for m in record["matches"]]==["profit margin","roi"]
