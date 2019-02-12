# Spell Checker with recursive Levenshtein distance

## Requirements 
The code is pure Python 3.
I'm using type annotations, so it should be any version higher or equal 3.5
## Overview
`main.py` is interactive console to try out functionality
`spellchecker.py` is main module file, where you can find `Spellchecker` class.
`/test` dir contains Unit tests in `test.py` and `.txt` files with test dictionaries.
#### Methods
```Spellchecker.load_words([str])``` - takes a list of words ([str]) and loads it into Trie.

```Spellchecker.check_word(str)``` - takes a word and return True if this word already in Trie and False otherwise.

```Spellchecker.check_list([str])``` - takes a list of words ([str]) and return a new list of unknown words that are not in Trie or empty list

```Spellchecker.suggest_correction_by_word(str, Levenshtein_distance=1)``` - takes a word and return list of suggestions within given distance (OPTIONAL, default=1)

```Spellchecker.suggest_correction_by_list([str], Levenshtein_distance=1)``` - takes a list of words ([str]) and return dictionary, where key is all words from given list with suggestions and values is list of suggestions within given distance (OPTIONAL, default=1)
## Usage
Download
```bash
git clone https://github.com/Just-kiy/spell-checker.git
cd spell-checker
```
Interactive console
```bash
python main.py

Write any word: 
>qwe
No suggestions for this word

Write any word:
>one
The word is correct

Write any word: 
>swar
Did you mean: 
swap
swat
swarm
```

## Background
This is my test task to [E-cetera](https://e-cetera.ru/).

The most popular approach is Peter Norvig's [How to Write a Spelling Corrector](http://norvig.com/spell-correct.html),
but I had to implement a fast-working algorithm, so it wasn't my option.

Instead of creating all possible variants of given word, I'm using Trie to store all known words and
recursively going down, calculating Damerau-Levenshtein distance on each step. If current step is already more than distance,
the algo stops investigating this path. 