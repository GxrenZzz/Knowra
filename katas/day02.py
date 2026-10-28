# E1 Implementation 
def normalize(text:str) -> str:
  # 1.Convert text to lowercase.
  # 2.Remove leading and trailing whitespace.
  # 3.Collapse internal sequences of whitespace into a single space.

  clean_text = " ".join(text.lower().split())
  
  return clean_text

# E1 - Test Cases
def test_normalize():
    assert normalize("  Hello\n\tWORLD  ") == "hello world"
    assert normalize("Python") == "python"
    assert normalize("") == ""
    assert normalize("   \n\t  ") == ""
    assert normalize("a    b\n\nc") == "a b c"


# E2 Implementation
  # 1.Convert all tokens to lowercase.
  # 2.Keep letters, digits, and apostrophes inside tokens.
  # 3.Treat punctuation such as !, ,, and -- as separators.
  # 4.Ignore empty tokens.
  # 5.Decide how Unicode letters should behave and test your decision.

def words_strings_method(text:str)-> list[str]:
    text = text.lower() 
    token_string = ""
    tokens = []
    for i,char in enumerate(text):
       if char.isalnum():
          token_string = token_string + char
       elif char =="'" and (i>0 and i+1<len(text)): # handling neiughbour indexes and range bound
          if text[i-1].isalnum() and text[i+1].isalnum():
             token_string = token_string + char
          else:
             if token_string:
                tokens.append(token_string)
                token_string = "" 
       else:
          # if we hit a space/Punctuations and a world built up , save the token
          if token_string and char != "'":
             tokens.append(token_string)
             token_string = "" #resets the token 
    # catch the very last word if the text didn't end with a punctuations
    if token_string:
       tokens.append(token_string)
    return tokens

# E2 Test Cases 
def test_words_strings_method():
    assert words_strings_method("Hello! World") == ["hello", "world"]
    assert words_strings_method("don't stop") == ["don't", "stop"]
    assert words_strings_method("hello' world") == ["hello", "world"]
    assert words_strings_method("'hello'") == ["hello"]
    assert words_strings_method("rock'n'roll") == ["rock'n'roll"]
    assert words_strings_method("AI2026") == ["ai2026"]
    assert words_strings_method("Café 中文") == ["café", "中文"]
    assert words_strings_method("") == []
    assert words_strings_method("   ") == []
    assert words_strings_method("Don't panic -- it's 42!") == ["don't", "panic", "it's", "42"]
    assert words_strings_method("123 45abc abc45") == ["123", "45abc", "abc45"]
    assert words_strings_method("hello!!!world") == ["hello", "world"]


