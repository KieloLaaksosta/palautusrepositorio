# Repository notes

- This is a collection of separate weekly Python exercises, not one app or a uv workspace. Each exercise with a `pyproject.toml` has its own environment and `uv.lock`; run commands from that exercise directory.
- The projects require Python 3.14 or newer. There is no repository-wide build, lint, or test command; use the project-specific commands below.
- `viikko1/riippuvuuksien-injektointi`: focused unit tests: `uv run pytest src/tests/laskin_test.py`.
- `viikko1/nhl-statistics`: focused tests: `uv run pytest src/tests/statistics_service_test.py`. These tests fetch NHL player data from the Helsinki course server; network access is required.
- `viikko 2/nhl-reader`: focused tests: `uv run python -m unittest tests.test_player_stats` (tests live in `tests/`, unlike the app code in `src/`).
- `viikko3/hello-robot`: run tests with `uv run robot src/tests`.
- `viikko3/login`: start the app from this directory with `uv run python src/index.py` (listens on port 5001), then in another terminal run `uv run robot src/tests`. The browser tests expect the app at `localhost:5001` and use Robot Framework Browser with Chromium; initialize its browser setup with `uv run rfbrowser init` if needed. Run a single suite by replacing `src/tests` with e.g. `src/tests/login.robot`.
