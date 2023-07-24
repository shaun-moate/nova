from nova.tokenizer import Tokenizer
from nova.dataclasses import FileLocation, Word, RawToken

# lex_tokens_from_file():
def test_lex_tokens_from_file_arithmetic_plus():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    assert tokenizer.raw_tokens == [
                      RawToken(FileLocation('tests/arithmetic-plus.nv', 2, 1), False, '34'),
                      RawToken(FileLocation('tests/arithmetic-plus.nv', 2, 4), False, '35'),
                      RawToken(FileLocation('tests/arithmetic-plus.nv', 2, 7), False, '+'),
                      RawToken(FileLocation('tests/arithmetic-plus.nv', 2, 9), False, 'dump'),
                     ]

def test_lex_tokens_from_file_arithmetic_minus():
    tokenizer = Tokenizer('tests/arithmetic-minus.nv')
    assert tokenizer.raw_tokens == [
                      RawToken(FileLocation('tests/arithmetic-minus.nv', 2, 1), False, '500'),
                      RawToken(FileLocation('tests/arithmetic-minus.nv', 2, 5), False, '80'),
                      RawToken(FileLocation('tests/arithmetic-minus.nv', 2, 8), False, '-'),
                      RawToken(FileLocation('tests/arithmetic-minus.nv', 2, 10), False, 'dump')
                     ]

def test_lex_tokens_from_file_arithmetic_multiply():
    tokenizer = Tokenizer('tests/arithmetic-multiply.nv')
    assert tokenizer.raw_tokens == [
                      RawToken(FileLocation('tests/arithmetic-multiply.nv', 2, 1), False, '3'),
                      RawToken(FileLocation('tests/arithmetic-multiply.nv', 2, 3), False, '23'),
                      RawToken(FileLocation('tests/arithmetic-multiply.nv', 2, 6), False, '*'),
                      RawToken(FileLocation('tests/arithmetic-multiply.nv', 2, 8), False, 'dump')
                     ]

# lex_line_to_words():
def test_lex_line_to_words_as_expected():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    line = '69 96 + dump'
    tokens = list(tokenizer.lex_line_to_words(line))
    assert tokens == [
            Word(0, 2, "69", False),
            Word(3, 5, "96", False),
            Word(6, 7, "+", False),
            Word(8, 12, "dump", False),
            ]

def test_lex_line_to_tokens_with_string():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    line = '"Hello, World!" write'
    tokens = list(tokenizer.lex_line_to_words(line))
    assert tokens == [
            Word(0, 15, "Hello, World!", True),
            Word(16, 21, "write", False),
            ]

# get_next_word
def test_get_next_word_as_expected():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    line = '69 96 + dump'
    word = tokenizer.get_next_word(line, start=0) 
    assert word == Word(start = 0, end = 2, value = '69', string = False)

def test_get_next_symbol_string_case():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    line = '     "this is a string, hello world!"'
    symbol = tokenizer.get_next_word(line, start=0) 
    assert symbol == Word(start = 5, end = 37, value = 'this is a string, hello world!', string = True)

def test_get_next_symbol_as_list():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    word_list = []
    start = 0
    line = '69 96 + dump'
    while start < len(line):
        word = tokenizer.get_next_word(line, start)
        word_list.append(word)
        start = word.end
    assert word_list == [Word(start = 0, end = 2, value = '69', string = False), 
                          Word(start = 3, end = 5, value = '96', string = False), 
                          Word(start = 6, end = 7, value = '+', string = False), 
                          Word(start = 8, end = 12, value = 'dump', string = False)]

def test_get_next_word_as_list_with_string():
    tokenizer = Tokenizer('tests/arithmetic-plus.nv')
    word_list = []
    start = 0
    line = '69 96 + "hello, world!" dump'
    while start < len(line):
        word = tokenizer.get_next_word(line, start)
        word_list.append(word)
        start = word.end
    assert word_list == [Word(start = 0, end = 2, value = '69', string = False), 
                          Word(start = 3, end = 5, value = '96', string = False), 
                          Word(start = 6, end = 7, value = '+', string = False), 
                          Word(start = 8, end = 23, value = 'hello, world!', string = True),
                          Word(start = 24, end = 28, value = 'dump', string = False)]

