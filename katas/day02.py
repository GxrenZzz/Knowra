# E1 
def normalize(text:str) -> str:
  # 1.Convert text to lowercase.
  # 2.Remove leading and trailing whitespace.
  # 3.Collapse internal sequences of whitespace into a single space.

  clean_text = " ".join(text.lower().split())
  
  return clean_text


def test_normalize():
    assert normalize("  Hello\n\tWORLD  ") == "hello world"
    assert normalize("Python") == "python"
    assert normalize("") == ""
    assert normalize("   \n\t  ") == ""
    assert normalize("a    b\n\nc") == "a b c"