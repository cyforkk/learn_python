from greeter_app.core import greet


def test_greet() -> None:
    assert "Python" in greet("Python")
    assert greet("Ada").startswith("Hello")
