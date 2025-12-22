import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# Тесты для capitalize()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("тест", "Тест"),
])
def test_capitalize_positive(input_str, expected):
    """Позитивные тесты: обычные строки"""
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", "   "),
    ("123abc", "123abc"),
    (" skypro", " skypro"),
])
def test_capitalize_negative(input_str, expected):
    """Негативные тесты: граничные случаи"""
    assert string_utils.capitalize(input_str) == expected


# Тесты для trim()
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("  hello world  ", "hello world  "),
    ("\tskypro", "\tskypro"),
    ("", ""),
])
def test_trim_positive(input_str, expected):
    """Позитивные тесты для удаления пробелов в начале"""
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_no_spaces():
    """Строка без пробелов в начале не должна меняться"""
    assert string_utils.trim("skypro") == "skypro"


@pytest.mark.negative
def test_trim_only_spaces():
    """Строка только из пробелов"""
    assert string_utils.trim("     ") == ""


# Тесты для contains()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "Pro", True),
    ("Hello World", " ", True),
    ("", "", True),
])
def test_contains_positive(string, symbol, expected):
    """Позитивные тесты: символ присутствует"""
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("Hello", "hello", False),
    ("   ", "a", False),
])
def test_contains_negative(string, symbol, expected):
    """Негативные тесты: символ отсутствует"""
    assert string_utils.contains(string, symbol) == expected


# Тесты для delete_symbol()
@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
    ("aaa", "a", ""),
    ("ababab", "ab", ""),
])
def test_delete_symbol_positive(string, symbol, expected):
    """Позитивные тесты: удаление существующих символов"""
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("Hello", "", "Hello"),
    ("   ", " ", ""),
])
def test_delete_symbol_negative(string, symbol, expected):
    """Негативные тесты: удаление несуществующих символов"""
    assert string_utils.delete_symbol(string, symbol) == expected


# Дополнительные тесты
def test_capitalize_with_numbers():
    """Строка с числами должна работать"""
    result = string_utils.capitalize("123 test")
    assert result == "123 test"


def test_contains_case_sensitive():
    """Метод contains чувствителен к регистру"""
    assert not string_utils.contains("SkyPro", "s")
    assert string_utils.contains("SkyPro", "S")


def test_trim_tab_and_newline():
    """Проверяем удаление табуляций и переносов строк"""
    result = string_utils.trim("\t\n  test")
    assert result == "test", f"Ожидалось 'test', получено '{result}'"


def test_trim_multiple_whitespace_chars():
    """Разные пробельные символы: обычный пробел,
    табуляция, неразрывный пробел"""
    result = string_utils.trim("  \t \u00A0test")
    assert result == "test", f"Ожидалось 'test', получено '{result}'"


def test_delete_symbol_all_occurrences_bug():
    """Баг: удаление всех вхождений символа"""
    result = string_utils.delete_symbol("abracadabra", "a")
    assert result == "brcdbr", f"Ожидалось 'brcdbr', получено '{result}'"


def test_delete_symbol_overlapping():
    """Удаление перекрывающихся подстрок"""
    result = string_utils.delete_symbol("aaa", "aa")
    assert result == "a", f"Ожидалось 'a', получено '{result}'"


def test_capitalize_special_chars():
    """Спецсимволы в начале строки"""
    result = string_utils.capitalize("@test")
    assert result == "@test", f"Ожидалось '@test', получено '{result}'"


def test_capitalize_already_capitalized():
    """Строка уже с заглавной буквой"""
    result = string_utils.capitalize("Test")
    assert result == "Test", f"Ожидалось 'Test', получено '{result}'"


def test_trim_with_mixed_spaces():
    """Смешанные пробелы: пробел + таб + пробел"""
    result = string_utils.trim(" \t test \t ")
    expected = "test \t "
    assert result == expected, f"Ожидалось '{expected}', получено '{result}'"


def test_contains_unicode_symbols():
    """Юникод-символы (русские буквы, эмодзи)"""
    assert string_utils.contains("Привет 🐍", "🐍")
    assert string_utils.contains("Привет мир", "мир")


def test_delete_symbol_unicode():
    """Удаление юникод-символов"""
    result = string_utils.delete_symbol("Hello🐍World🐍", "🐍")
    assert result == "HelloWorld", "Ожидалось 'HelloWorld'"


def test_string_none_handling():
    """Как метод обрабатывает None (должна быть ошибка)"""
    try:
        string_utils.capitalize(None)
        pytest.fail("Метод должен вызывать ошибку при передаче None")
    except AttributeError:
        pass
    except TypeError:
        pass


def test_trim_return_type():
    """Проверяем, что возвращается строка (не другой тип)"""
    result = string_utils.trim("  test")
    assert isinstance(result, str), "Метод должен возвращать str"


if __name__ == "__main__":
    pytest.main(["-v", __file__])
