from io import StringIO

from stock_analyzer import run


def test_sample_data():
    input_file_content = """52924702,aaa,13,1136
52924702,aac,20,477
52925641,aab,31,907
52927350,aab,29,724
52927783,aac,21,638
52930489,aaa,18,1222
52931654,aaa,9,1077
52933453,aab,9,756"""
    input_file = StringIO(input_file_content)
    output_file = StringIO()
    run(input_file, output_file)

    expected_output = """aaa,5787,40,1161,1222
aab,6103,69,810,907
aac,3081,41,559,638
"""
    assert expected_output == output_file.getvalue()
