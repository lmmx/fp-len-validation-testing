from pytest import importorskip


def test_example_existing():
    importorskip("examples.existing")


def test_example_new():
    importorskip("examples.new")
