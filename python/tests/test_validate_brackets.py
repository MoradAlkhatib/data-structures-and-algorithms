from challenges.multi_bracket_validation.multi_bracket_validation import validate_brackets


def test_validate_brackets():
    
    string="{}"
    assert validate_brackets(string)==True

def test_validate_brackets1():
    
    string="{}(){}"
    assert validate_brackets(string)==True

def test_validate_brackets2():
    
    string="()[[Extra Characters]]"
    assert validate_brackets(string)==True

def test_validate_brackets3():
    
    string="(){}[[]]"
    assert validate_brackets(string)==True

def test_validate_brackets4():
    
    string="{}{Code}[Fellows](())"
    assert validate_brackets(string)==True

def test_validate_brackets5():
    
    string="[({}]"
    assert validate_brackets(string)==False

def test_validate_brackets6():
    
    string="(]("
    assert validate_brackets(string)==False


def test_validate_brackets7():
    
    string="{(})"
    assert validate_brackets(string)==False








