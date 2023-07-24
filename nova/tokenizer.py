from typing import Generator
from nova.helpers import find_next
from nova.dataclasses import Word, FileLocation, RawToken

class Tokenizer():
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.raw_tokens = []
        self.lex_tokens_from_file()

    def lex_tokens_from_file(self):
        with open(self.file_path, "r") as file:
            tokens = [
                      RawToken(
                            location = FileLocation(
                                            row = line_number+1,
                                            col = word.start+1,
                                            file_path = self.file_path,
                                        ),
                            string_literal = word.string,
                            value = word.value,
                        )
                    for (line_number, line) in enumerate(file.readlines())
                    for word in self.lex_line_to_words(line.split("//")[0])]
            self.raw_tokens = tokens

    def lex_line_to_words(self, line: str) -> Generator[Word, None, None]:
        start = 0
        while start < len(line)-1:
            word = self.get_next_word(line, start)
            start = word.end+1
            yield(word)

    def get_next_word(self, line: str, start: int) -> Word:
        word_start = find_next(line, start, lambda x : not x.isspace()) 
        if line[word_start] == "\"":
            word_end = find_next(line, word_start+1, lambda x : x == "\"")
            return Word(
                    start = word_start, 
                    end = word_end+1, 
                    string = True,
                    value = line[word_start+1:word_end], 
                    )
        else:
            word_end = find_next(line, word_start, lambda x : x.isspace())
            return Word(
                    start = word_start, 
                    end = word_end, 
                    string = False,
                    value = line[word_start:word_end], 
                    )

