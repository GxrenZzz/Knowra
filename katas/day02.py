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



#E2(Regex Version)
import re
def words_regex_method(text:str)->list[str]:
   # 1.Convert text to lowercase.
   # 2.Keep Unicode letters and digits.
   # 3.Preserve apostrophes only between two alphanumeric characters.
   # 4.Treat punctuation, whitespace, and underscores as separators.
   # 5.Ignore empty tokens.

   text = text.lower()
   regex_tokens = re.findall(r"[^\W_]+(?:'[^\W_]+)*",text)
   return regex_tokens

# E2 Test Cases 
def test_words_regex_method():
   assert words_regex_method("Hello! World") == ["hello", "world"]
   assert words_regex_method("don't stop") == ["don't", "stop"]
   assert words_regex_method("'hello'") == ["hello"]
   assert words_regex_method("rock'n'roll") == ["rock'n'roll"]
   assert words_regex_method("AI2026") == ["ai2026"]
   assert words_regex_method("Café 中文") == ["café", "中文"]
   assert words_regex_method("") == []
   assert words_regex_method("hello_world") == ["hello", "world"]
   assert words_regex_method("hello'") == ["hello"]
   assert words_regex_method("''hello''") == ["hello"]
   assert words_regex_method("a_b") == ["a", "b"]
   assert words_regex_method("can't've") == ["can't've"]

#E2 Test cases for both string and Regex

def test_regex_and_string():
    assert words_strings_method("Don't panic -- it's 42!") == ["don't", "panic", "it's", "42"]
    assert words_regex_method("Don't panic -- it's 42!") == ["don't", "panic", "it's", "42"]
    assert words_strings_method("Hello, WORLD!") == ["hello", "world"]
    assert words_regex_method("Hello, WORLD!") == ["hello", "world"]
    assert words_strings_method("") == []
    assert words_regex_method("") == []
    assert words_strings_method("   !!! -- ") == []
    assert words_regex_method("   !!! -- ") == []
    assert words_strings_method("one  two\nthree\tfour") == ["one", "two", "three", "four"]
    assert words_regex_method("one  two\nthree\tfour") == ["one", "two", "three", "four"]
    assert words_strings_method("Ünïcode CAFÉ") == ["ünïcode", "café"]
    assert words_regex_method("Ünïcode CAFÉ") == ["ünïcode", "café"]

# E3 Implementaion
# 1. Check whether n <= 0. If so, return [] immediately.
# 2. Tokenize the text using your E2 implementation.
# 3. Normalize the stopwords so they match your lowercase tokens. Treat None as an empty set.
# 4. Create an empty dictionary for word counts.
# 5. Loop through the tokens. Skip stopwords; otherwise increment the word's count.
# 6. Sort the dictionary entries by descending count, then alphabetical word order.
# 7. Return only the first n entries as a list of (word, count) tuples.

def top_words_dict(text:str , n:int , stopwards : set[str] | None = None) -> list[tuple[str,int]]:
   if n <=0:
      return [] 
   if stopwards is None:
      stopwards = set() 

   stopwards = {word.lower() for word in stopwards}
   
   count: dict[str,int] = {}
   words = words_regex_method(text)
   for word in words:

      if word in stopwards:
         continue # passes that word cuz of the context meaning 

      count[word] = count.get(word,0) + 1

   return sorted(count.items(),key=lambda item: (-item[1], item[0]),)[:n]

# E3 1st Version Test Case 
def test_top_words_dict():
    assert top_words_dict("pear apple pear banana apple", 2) == [("apple", 2),("pear", 2),]
    assert top_words_dict("Apple apple BANANA", 3) == [("apple", 2),("banana", 1),]
    assert top_words_dict("the cat and the dog",5,stopwards={"the", "and"},) == [("cat", 1),("dog", 1),]
    assert top_words_dict("apple banana", 0) == []
    assert top_words_dict("apple banana", -1) == []
    assert top_words_dict("", 3) == []
    assert top_words_dict("pear pear apple", 10) == [("pear", 2),("apple", 1),]


# E3 Second Version 
from collections import Counter
def top_words_counter(text:str , n:int , stopwords : set[str] | None = None) -> list[tuple[str,int]] :
   # condition if n <= 0
   if n <= 0:
      return []

   # tokenization of text
   words = words_regex_method(text)

   # stopward to lowercase
   if stopwords is None:
      stopwords = set()

   stopwords = {word.lower() for word in stopwords}

   # Filtering Stopwards
   filter_words = []
   for word in words:
      if word not in stopwords:
         filter_words.append(word)

   count = Counter(filter_words)

   return sorted(count.items(),key= lambda item : (-item[1],item[0]),)[:n]

def test_top_words_counter():
   assert top_words_counter("pear apple pear banana apple", 2) == [("apple", 2),("pear", 2),]
   assert top_words_counter("Apple apple BANANA", 3) == [("apple", 2),("banana", 1),]
   assert top_words_counter("the cat and the dog",5,stopwords={"the", "and"}) == [("cat", 1),("dog", 1),]
   assert top_words_counter("The cat the dog",5,stopwords={"THE"}) == [("cat", 1),("dog", 1),]
   assert top_words_counter("apple banana", 0) == []
   assert top_words_counter("apple banana", -2) == []
   assert top_words_counter("", 3) == []
   assert top_words_counter("pear pear apple", 10) == [("pear", 2),("apple", 1),]

import pytest

@pytest.mark.parametrize(
    "text, n, stopwords, expected",
    [
        (
            "pear apple pear banana apple",
            2,
            None,
            [("apple", 2), ("pear", 2)],
        ),
        (
            "Apple apple BANANA",
            3,
            None,
            [("apple", 2), ("banana", 1)],
        ),
        (
            "the cat and the dog",
            5,
            {"the", "and"},
            [("cat", 1), ("dog", 1)],
        ),
        (
            "The cat the dog",
            5,
            {"THE"},
            [("cat", 1), ("dog", 1)],
        ),
        (
            "apple banana",
            0,
            None,
            [],
        ),
        (
            "apple banana",
            -2,
            None,
            [],
        ),
        (
            "",
            3,
            None,
            [],
        ),
        (
            "pear pear apple",
            10,
            None,
            [("pear", 2), ("apple", 1)],
        ),
    ],
)
def test_top_words_implementations(text, n, stopwords, expected):
    assert top_words_dict(text, n, stopwords) == expected
    assert top_words_counter(text, n, stopwords) == expected

# E4 Chunking words 

def chunk_words(words: list[str],size: int,overlap: int,) -> list[list[str]]:

    # 1. Validate size
    if size <= 0:
        raise ValueError("Size must be greater than 0")

    # 2. Validate overlap
    if overlap < 0:
        raise ValueError("Overlap cannot be negative")

    # 3. Validate overlap against size
    if overlap >= size:
        raise ValueError("Overlap must be smaller than size")

    # 4. Calculate stride
    step = size - overlap

    # 5. Handle empty input
    if not words:
        return []

    # 6. Generate chunks
    chunks = []

    for i in range(0, len(words), step):
        chunk = words[i:i + size]
        chunks.append(chunk)

    return chunks

# E4 Test Caases 

import pytest


# ==========================================
# E4: CHUNK WORDS — VALID INPUT TEST CASES
# ==========================================

VALID_CHUNK_CASES = [
    (
        "basic_overlap",
        list("abcdefghij"),
        4,
        1,
        [
            list("abcd"),
            list("defg"),
            list("ghij"),
            list("j"),
        ],
    ),
    (
        "no_overlap",
        list("abcdef"),
        3,
        0,
        [
            list("abc"),
            list("def"),
        ],
    ),
    (
        "maximum_valid_overlap",
        list("abcde"),
        3,
        2,
        [
            list("abc"),
            list("bcd"),
            list("cde"),
            list("de"),
            list("e"),
        ],
    ),
    (
        "partial_final_chunk",
        list("abcdefg"),
        3,
        0,
        [
            list("abc"),
            list("def"),
            list("g"),
        ],
    ),
    (
        "input_smaller_than_size",
        ["hello", "world"],
        5,
        1,
        [
            ["hello", "world"],
        ],
    ),
    (
        "empty_input",
        [],
        3,
        1,
        [],
    ),
    (
        "single_element_chunks",
        list("abc"),
        1,
        0,
        [
            ["a"],
            ["b"],
            ["c"],
        ],
    ),
    (
        "exact_multiple_of_step",
        list("abcdef"),
        4,
        2,
        [
            list("abcd"),
            list("cdef"),
            list("ef"),
        ],
    ),
    (
        "single_word",
        ["hello"],
        3,
        0,
        [
            ["hello"],
        ],
    ),
]


@pytest.mark.parametrize(
    "name, words, size, overlap, expected",
    VALID_CHUNK_CASES,
    ids=[case[0] for case in VALID_CHUNK_CASES],
)
def test_chunk_words_valid(name, words, size, overlap, expected):
    assert chunk_words(words, size, overlap) == expected


# ==========================================
# E4: CHUNK WORDS — INVALID INPUT TEST CASES
# ==========================================

INVALID_CHUNK_CASES = [
    ("zero_size", ["a", "b"], 0, 0),
    ("negative_size", ["a", "b"], -1, 0),
    ("negative_overlap", ["a", "b"], 3, -1),
    ("overlap_equal_to_size", ["a", "b"], 3, 3),
    ("overlap_greater_than_size", ["a", "b"], 3, 4),
]


@pytest.mark.parametrize(
    "name, words, size, overlap",
    INVALID_CHUNK_CASES,
    ids=[case[0] for case in INVALID_CHUNK_CASES],
)
def test_chunk_words_invalid(name, words, size, overlap):
    with pytest.raises(ValueError):
        chunk_words(words, size, overlap)

