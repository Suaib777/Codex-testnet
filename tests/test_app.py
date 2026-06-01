from codex_testnet.app import greet, normalize_name


def test_normalize_name_defaults_to_friend():
    assert normalize_name("") == "friend"


def test_normalize_name_trims_whitespace():
    assert normalize_name("  Codex ") == "Codex"


def test_greet_defaults_to_friend():
    assert greet("") == "Hello, friend!"


def test_greet_trims_name():
    assert greet("  Codex ") == "Hello, Codex!"
