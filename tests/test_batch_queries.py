import json
import pytest
from assistant import main

def test_batch_order_and_blank_lines(tmp_path,capsys):
    src=tmp_path/"q.txt";src.write_text("\ufeffprofit\n\nroi\n",encoding="utf-8")
    assert main(["--queries-file",str(src)])==0
    assert [json.loads(line)["query"] for line in capsys.readouterr().out.splitlines()]==["profit","roi"]

def test_oversized_file_emits_no_partial_answers(tmp_path,capsys):
    src=tmp_path/"q.txt";src.write_text("profit\n"+"x"*1048576)
    with pytest.raises(SystemExit):main(["--queries-file",str(src)])
    assert capsys.readouterr().out==""
