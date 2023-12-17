class Translations:
    en_dictionary = {
        "start": (
            "Provide a text entered using wrong keyboard layout and I will"
            " transform it to the expected version."
        ),
        "help": (
            "Provide a text entered using wrong keyboard layout and I will"
            " transform it to the expected version. If you encountered any"
            " issues please create a new issue here:"
            " https://github.com/bukSHA1024/text-correction-bot"
        ),
        "something_went_wrong": (
            "Something went wrong. Please fill an issue here:"
            " https://github.com/bukSHA1024/text-correction-bot"
        ),
        "nothing_to_correct": "This message doesn't have any text to correct.",
        "not_supported_layout": (
            "Cannot convert message written on a mixed keyboard layout. Please"
            " provide message that was written using a single keyboard layout."
        ),
    }

    languages = {
        "en": en_dictionary,
    }

    translation_not_found = (
        "Translation of this message was not found. Please create an issue"
        " here: https://github.com/bukSHA1024/text-correction-bot"
    )

    def get_translation(phrase_key, language="en"):
        if language in Translations.languages.keys():
            if phrase_key in Translations.languages[language].keys():
                return str(Translations.languages[language][phrase_key])
        return str(Translations.translation_not_found)
