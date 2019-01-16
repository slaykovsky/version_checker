import functools
import re

class VersionCheckerError(ValueError):
    def __init__(self, string):
        super().__init__(string)
        self.strerror = string

class Version:
    """Implements Semantic Versioning 2.0.0 with NO extensions"""
    matcher = re.compile(r'^(\d+)\.(\d+)\.(\d+)$')

    def __init__(self, version_string):
        major, minor, patch = self.parse(version_string)

        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return f'Version {self.major}.{self.minor}.{self.patch}'

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter((self.major, self.minor, self.patch))

    def __cmp__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplementedError

        def cmp(x, y):
            if x == y:
                return 0
            elif x > y:
                return 1
            elif x < y:
                return -1
            else:
                raise NotImplementedError

        comparators = zip([cmp, cmp, cmp], self, other)

        for f, s_member, o_member in comparators:
            result = f(s_member, o_member)
            if result != 0:
                return result
        return 0

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def parse(self, version_string):
        if not version_string:
            raise VersionCheckerError('Empty version string')

        match = self.matcher.match(version_string)
        if not match:
            raise VersionCheckerError(f'Invalid version string: {version_string}')

        major, minor, patch = match.groups()
        if not minor:
            minor = 0

        if not patch:
            patch = 0

        check_failures = []
        for checker in [self._check_major(major), self._check_minor(minor), self._check_patch(patch)]:
            if checker is None:
                continue
            check_failures.append(checker.strerror)

        if check_failures:
            raise VersionCheckerError(f'Invalid version string:{";".join(check_failures)}')

        major = int(major)
        minor = int(minor)
        patch = int(patch)

        return major, minor, patch

    def _check_zero(self, number, version):
        if (number
            and number.isdigit()
            and number != '0'
            and number[0] == '0'
        ):
            return VersionCheckerError(f'{version} version {number} has leading zero')

    def _check_major(self, number):
        return self._check_zero(number, 'major')

    def _check_minor(self, number):
        return self._check_zero(number, 'minor')

    def _check_patch(self, number):
        return self._check_zero(number, 'patch')


def compare_versions(first, second):
    first = Version(first)
    second = Version(second)

    if first == second: return f'{first} is equal to {second}'
    if first < second: return f'{first} is less than {second}'
    if first > second: return f'{first} is greater than {second}'
