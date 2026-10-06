def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    difficulty_ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return difficulty_ranges.get(difficulty, (1, 100))


class GuessResult(str):
    """String-like outcome that also supports tuple unpacking for app use."""

    def __new__(cls, outcome: str, message: str):
        obj = str.__new__(cls, outcome)
        obj.message = message
        return obj

    def __iter__(self):
        yield str(self)
        yield self.message


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    cleaned = str(raw).strip()
    if cleaned == "":
        return False, None, "Enter a guess."

    try:
        if "." in cleaned:
            value = int(float(cleaned))
        else:
            value = int(cleaned)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome while also supporting tuple unpacking.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return GuessResult("Win", "🎉 Correct!")

    if guess > secret:
        return GuessResult("Too High", "📈 Go HIGHER!")

    return GuessResult("Too Low", "📉 Go LOWER!")


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
