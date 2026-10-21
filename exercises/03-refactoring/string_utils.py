def _clean_text(s):
    if s is None:
        return ""

    text = s.strip()
    return text if text else ""


def shout(s):
    text = _clean_text(s)
    return "" if not text else text.upper() + "!"


def whisper(s):
    text = _clean_text(s)
    return "" if not text else text.lower() + "..."
