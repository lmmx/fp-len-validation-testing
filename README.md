# Filepath length validation testing

Development on [issue 8308][issue] on the Pydantic repo

> File path length validation (`NewPath`) #8308

[issue]: https://github.com/pydantic/pydantic/issues/8308

## Usage

- This repo is a `uv` workspace, the PR fork of Pydantic is a workspace member in `packages` (a git subrepo, code not co-included). Install the workspace and all dependencies with `uv pip install .`
- Run the examples as standalone scripts or run the tests (`pytest tests`)
