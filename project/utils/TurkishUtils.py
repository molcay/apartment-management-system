
class TurkishUtils:
    to_upper_letter_map = {
        'ğ': 'Ğ',
        'ü': 'Ü',
        'ş': 'Ş',
        'i': 'İ',
        'ı': 'I',
        'ö': 'Ö',
        'ç': 'Ç'
    }

    to_lower_letter_map = {
        'Ğ': 'ğ',
        'Ü': 'ü',
        'Ş': 'ş',
        'İ': 'i',
        'I': 'ı',
        'Ö': 'ö',
        'Ç': 'ç'
    }

    @staticmethod
    def currency_to_human_readable(price: float, round_with: int = 2, with_icon: bool = False) -> str:
        unit = '₺' if with_icon else 'TL'
        price_as_str = '{1:.{0}f}'.format(round_with, price).replace('.', ',')
        if len(price_as_str) > 6:
            price_as_str = price_as_str[:-6] + '.' + price_as_str[-6:]
        return "{0} {1}".format(price_as_str, unit)

    @staticmethod
    def lower(text: str) -> str:
        result = ''
        for c in text:
            result += TurkishUtils.to_lower_letter_map.get(c, c.lower())

        return result

    @staticmethod
    def upper(text: str) -> str:
        result = ''
        for c in text:
            result += TurkishUtils.to_upper_letter_map.get(c, c.upper())

        return result
