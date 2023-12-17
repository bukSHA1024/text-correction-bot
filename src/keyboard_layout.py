EnglishLayout = """`1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
RussianLayout = """ё1234567890-=йцукенгшщзхъфывапролджэ\ячсмитьбю.Ё!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""

EnglishOnlyChars = "".join(set(EnglishLayout) - set(RussianLayout))
RussianOnlyChars = "".join(set(RussianLayout) - set(EnglishLayout))

EnglishLayoutKey = "en"
RussianLayoutKey = "ru"
MixedLayoutKey = "mixed"


class NotSupportedLayoutException(Exception):
    pass


def detect_current_and_desired_layout(text):
    foundEnglishOnlyChars = False
    foundRussianOnlyChars = False
    for char in text:
        if char in EnglishOnlyChars:
            foundEnglishOnlyChars = True
        if char in RussianOnlyChars:
            print(char, RussianOnlyChars)
            foundRussianOnlyChars = True
    print(foundEnglishOnlyChars, foundRussianOnlyChars)
    if foundEnglishOnlyChars and not foundRussianOnlyChars:
        return (EnglishLayoutKey, RussianLayoutKey)
    elif foundRussianOnlyChars and not foundEnglishOnlyChars:
        return (RussianLayoutKey, EnglishLayoutKey)
    else:
        return (MixedLayoutKey, MixedLayoutKey)


def change_char_layout(char, current_layout, desired_layout):
    if (
        current_layout == EnglishLayoutKey
        and desired_layout == RussianLayoutKey
    ):
        charIndex = EnglishLayout.find(char)
        if charIndex == -1:
            return char
        return RussianLayout[charIndex]
    elif (
        current_layout == RussianLayoutKey
        and desired_layout == EnglishLayoutKey
    ):
        charIndex = RussianLayout.find(char)
        if charIndex == -1:
            return char
        return EnglishLayout[charIndex]


def correct_layout(text):
    result_text = ""
    current_layout, desired_layout = detect_current_and_desired_layout(text)
    print(current_layout, desired_layout, EnglishOnlyChars, RussianOnlyChars)
    if current_layout == MixedLayoutKey or desired_layout == MixedLayoutKey:
        raise NotSupportedLayoutException(
            "Mixed keyboard layout is not supported."
        )
    for char in text:
        result_text += change_char_layout(char, current_layout, desired_layout)
    return result_text
