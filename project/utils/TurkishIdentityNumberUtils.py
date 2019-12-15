class TurkishIdentityNumberUtils:
    @staticmethod
    def validate(value: str) -> bool:
        if not (len(value) == 11 and value.isdigit() and value[0] != '0' and value[-1] in '02468'):
            return False
        digits = [int(c) for c in value]
        tenth_digit = ((sum(digits[:9:2]) * 7) - (sum(digits[1:9:2]))) % 10
        is_tenth_digit_valid = tenth_digit == digits[9]
        if not is_tenth_digit_valid:
            return False
        eleventh_digit = sum(digits[:-1]) % 10
        is_eleventh_digit_valid = eleventh_digit == digits[-1]
        if not is_eleventh_digit_valid:
            return False
        return True
