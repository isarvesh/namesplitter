from namesplitter.utils import name_helper

def test_two_names():
    assert name_helper.split_name("John Smith") == ["John", "Smith"]

def test_middle_names():
    assert name_helper.split_name("John Patrick Smith") == ["John Patrick", "Smith"]
    assert name_helper.split_name("John Patrick Thomson Smith") == ["John Patrick Thomson", "Smith"]

def test_surname_prefixes():
    assert name_helper.split_name("John van der Berg") == ["John", "van der Berg"]
    assert name_helper.split_name("John Patrick van der Berg") == ["John Patrick", "van der Berg"]

def test_split_name_onename():
    assert name_helper.split_name("Smith") == ["", "Smith"]

def test_split_name_nonames():
    assert name_helper.split_name("") == ["", ""]