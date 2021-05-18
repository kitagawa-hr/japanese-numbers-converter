import pytest

from jnc import NotSupportedError, ParseError, ValidationError, to_number


@pytest.mark.parametrize(
    "input_case, expected",
    [
        ("〇", 0),
        ("三〇", 30),
        ("六八", 68),
        ("一六〇〇", 1600),
        ("二〇一七", 2017),
        ("二十", 20),
        ("五十九", 59),
        ("三百二", 302),
        ("四千五百", 4500),
        ("十", 10),
        ("十五", 15),
        ("百", 100),
        ("百十", 110),
        ("百八", 108),
        ("千六", 1006),
        ("千十", 1010),
        ("千百十", 1110),
        ("百万", 1000000),
        ("一万五千八百", 15800),
        ("二億五千万", 250000000),
        ("十兆百億七百万", 10010007000000),
        ("百兆三", 100000000000003),
        ("二千万", 20000000),
        ("一千万", 10000000),
        ("千五百", 1500),
        ("一千五百", 1500),
        ("千五百万", 15000000),
        ("一千五百万", 15000000),
        ("参弐壱", 321),
        ("弐拾参", 23),
        ("拾弐万参千弐百拾壱", 123211),
        ("九千七兆千九百九十二億五千四百七十四万九百九十一", 9007199254740991),
        ("九〇〇七兆一九九二億五四七四万九九一", 9007199254740991),
    ],
)
def test_valid_cases(input_case, expected):
    assert to_number(input_case) == expected


@pytest.mark.parametrize(
    "input_case",
    [
        # throws Error when input contains unsupported characters
        ("第百十六回"),
        # throws Error when input string is too long
        ("一二三四五六七八九〇一二三四五六七八九〇一二三四五六七八九〇一二三"),
    ],
)
def test_raises_not_supported_error(input_case):
    with pytest.raises(NotSupportedError):
        to_number(input_case)


@pytest.mark.parametrize(
    "input_case",
    [
        # throws Error when input string is empty
        (""),
        # "一百" and "一十" are invalid in common writing. 100 is just "百", and 10 is just "十"
        ("一十"),
        ("一百"),
        ("一百一十"),
        ("四百一十五"),
        # if "千" directly precedes the name of powers of myriad, "一" is normally attached before "千"
        ("千万"),
        ("一億千万"),
        ("億千万"),
        # Each place (十,百,千,拾) should not have more than one digit
        ("六七百"),
        ("二〇〇十七"),
        ("三四千五六七百"),
        # 万,億,兆 cannot be adjacent to each other or be the first character of the sequence
        ("万"),
        ("億"),
        ("兆"),
        ("兆億万"),
    ],
)
def test_raises_validation_error(input_case):
    with pytest.raises(ValidationError):
        to_number(input_case)


@pytest.mark.parametrize(
    "input_case",
    [
        # throws Error when name of powers of 10 appears more than once in subsequence
        ("十百千"),
        ("三十七百九千"),
        ("四万三億二兆"),
        # Each place (十,百,千,拾) should not start with zero
        ("〇十"),
        ("〇千〇百〇十"),
        # Positional notation or place of "一" should not start with zero
        ("〇〇"),
        ("〇十〇"),
        ("〇一二三"),
        ("十〇"),
        ("千〇"),
        ("千〇〇"),
        ("〇万"),
        # throws Error when name of powers of 10 appears more than once in subsequence
        ("十十"),
        ("二十五十"),
        ("三十二十"),
        ("八百五百"),
    ],
)
def test_raises_parse_error(input_case):
    with pytest.raises(ParseError):
        to_number(input_case)
