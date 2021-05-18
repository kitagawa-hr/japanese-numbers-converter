# japanese-number-converter

Converts [Japanese Numerals](https://en.wikipedia.org/wiki/Japanese_numerals) into `arabic number`.

## Installation

```sh
pip install japanese-number-converter
```

## Usage

```py
import jnc

assert jnc.ja_to_arabic("九千七兆千九百九十二億五千四百七十四万九百九十一") == 9007199254740991
```

For detail, see [test cases](./test_jnc.py).

## Supported formats

### numbers 0 to 9

- `〇`, `一`, `二`, `三`, `四`, `五`, `六`, `七`, `八`, `九`

### names of powers of 10

- `十`, `百`, `千`, `万`, `億`, `兆`

### [formal numerals (daiji) used in legal documents](https://en.wikipedia.org/wiki/Japanese_numerals#Formal_numbers)

- `壱`, `弐`, `参`, `拾`

## Reference

I used [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) as a reference.
