from pytest import importorskip


def test_example_new_long_file_name():
    importorskip("examples.new_long_file_name")


def test_example_new_long_dir_and_file_names():
    importorskip("examples.new_long_dir_and_file_names")


def test_example_existing_long():
    importorskip("examples.existing_long")
