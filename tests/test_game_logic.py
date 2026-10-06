from pathlib import Path  # Issue two
from streamlit.testing.v1 import AppTest

APP_FILE = str(Path(__file__).resolve().parents[1] / "app.py")  # Issue two

def submit_guess(guess):  # Issue two
    app = AppTest.from_file(APP_FILE).run(timeout=30)  # Issue two
    app.session_state["secret"] = 50  # Issue two
    app.text_input[0].set_value(str(guess))  # Issue two
    app.button[0].click().run(timeout=30)  # Issue two
    return app  # Issue two

def test_winning_guess():  # Issue two
    app = submit_guess(50)  # Issue two
    assert app.session_state["status"] == "won"  # Issue two

def test_guess_too_high():  # Issue two
    app = submit_guess(60)  # Issue two
    assert app.warning[0].value == "Go LOWER!"  # Issue two

def test_guess_too_low():  # Issue two
    app = submit_guess(40)  # Issue two
    assert app.warning[0].value == "Go HIGHER!"  # Issue two


def test_attempt_count_starts_at_zero_and_only_valid_guesses_count():  # Issue three
    app = AppTest.from_file(APP_FILE).run(timeout=30)  # Issue two; Issue three

    assert app.session_state["attempts"] == 0  # Issue three
    assert "Attempts left: 8" in app.info[0].value  # Issue three

    app.text_input[0].set_value("not a number")  # Issue three
    app.button[0].click().run(timeout=30)  # Issue three
    assert app.session_state["attempts"] == 0  # Issue three

    app.text_input[0].set_value("1")  # Issue three
    app.button[0].click().run(timeout=30)  # Issue three
    assert app.session_state["attempts"] == 1  # Issue three

def test_new_game_restarts_after_loss():  # Issue one
    app = AppTest.from_file(APP_FILE).run(timeout=30)  # Issue one; Issue two
    app.session_state["status"] = "lost"  # Issue one
    app.session_state["attempts"] = 8  # Issue one
    app.session_state["score"] = 25  # Issue one
    app.session_state["history"] = [1, 2, 3]  # Issue one
    app.button[1].click().run(timeout=30)  # Issue one
    assert app.session_state["status"] == "playing"  # Issue one
    assert app.session_state["attempts"] == 0  # Issue one
    assert app.session_state["score"] == 0  # Issue one
    assert app.session_state["history"] == []  # Issue one
