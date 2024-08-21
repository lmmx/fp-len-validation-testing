from pytest import importorskip


def test_example_new_long():
    importorskip("examples.new_long")


def test_example_new_readonly():
    importorskip("examples.new_readonly")


def test_example_existing_long():
    importorskip("examples.existing_long")
