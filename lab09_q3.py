import unittest


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def is_valid_ip(ip):
    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        if int(part) < 0 or int(part) > 255:
            return False

    return True


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


class TestCelsius(unittest.TestCase):

    def test_freezing(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_boiling(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)


class TestValidIP(unittest.TestCase):

    def test_valid(self):
        self.assertTrue(is_valid_ip("192.168.1.1"))

    def test_invalid_octet(self):
        self.assertFalse(is_valid_ip("256.1.1.1"))

    def test_too_few_parts(self):
        self.assertFalse(is_valid_ip("1.2.3"))

    def test_empty(self):
        self.assertFalse(is_valid_ip(""))


class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(7), "7")


if __name__ == "__main__":
    unittest.main()