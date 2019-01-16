import pytest

from version_checker import Version, VersionCheckerError

from random import randint


def generate_parse_good(n):
    data = []

    for _ in range(n):
        version_string = '.'.join([
            str(randint(0, 999)),
            str(randint(0, 999)),
            str(randint(0, 999))])

        data.append((version_string, f'Version {version_string}'))

    return data


@pytest.mark.parametrize('version_string,expected', generate_parse_good(999))
def test_parse_success(version_string, expected):
    assert str(Version(version_string)) == expected


bad_data = [
    '01.0.0', '0', '9.02.1', '0.1', '10.10.01'        
]

@pytest.mark.parametrize('version_string', bad_data)
def test_parse_failure(version_string):
    with pytest.raises(VersionCheckerError):
        Version(version_string)

comparison_data = [
    ('0.0.0', '0.0.0', 0), 
    ('0.0.0', '0.0.1', -1), 
    ('0.1.0', '0.0.0', 1) 
]
@pytest.mark.parametrize('first,second,expected', comparison_data)
def test_comparison(first, second, expected):
    assert Version(first).__cmp__(Version(second)) == expected


def generate_eq_data(n):
    data = []

    for _ in range(n):
        major = str(randint(0, 999))
        minor = str(randint(0, 999))
        patch = str(randint(0, 999))

        version_string = '.'.join([major, minor, patch])

        data.append((version_string, version_string))

    return data

@pytest.mark.parametrize('first,second', generate_eq_data(999))
def test_eq(first, second):
    assert Version(first) == Version(second)


def generate_not_eq_data(n):
    """Assume we'll never get equal version strings for given n"""
    data = []

    for _ in range(n):
        fmajor = randint(0, 999)
        fminor = randint(0, 999)
        fpatch = randint(0, 999)

        smajor = randint(0, 999)
        sminor = randint(0, 999)
        spatch = randint(0, 999)

        while fmajor == smajor:
            smajor = randint(0, 999)

        while fminor == sminor:
            sminor = randint(0, 999)

        while fpatch == spatch:
            spatch = randint(0, 999)

        first = '.'.join(map(str, [fmajor, fminor, fpatch]))
        second = '.'.join(map(str, [smajor, sminor, spatch]))

        data.append((first, second))

    return data

@pytest.mark.parametrize('first,second', generate_not_eq_data(999))
def test_not_eq(first, second):
    assert Version(first) != Version(second)
