# demo-test-repo

Tiny throwaway repo for demoing the [Autonomous Dev Agent](../dev-agent).
Contains one deliberately broken module and a failing test suite.

## Setup

1. Push this repo to your own GitHub account, e.g. `yourusername/demo-test-repo`.
2. Confirm the bug is really there:
   ```bash
   pip install pytest
   pytest -v
   ```
   You should see 2 failing tests (`test_add`, `test_average`).
3. Open a new **Issue** on the repo (GitHub → Issues → New issue) with:

   **Title:**
   ```
   Bug: add() and average() return wrong results
   ```

   **Body:**
   ```
   The add() function in src/math_utils.py returns the wrong value —
   it looks like it's subtracting instead of adding.

   The average() function also seems off by one; it doesn't match the
   test expectations in tests/test_math_utils.py.

   Both are causing test_math_utils.py to fail. Please fix.
   ```
4. Note the issue number (shown in the URL, e.g. `.../issues/1`).
5. In your `dev-agent` project, set `REPO_FULL_NAME=yourusername/demo-test-repo`
   in `.env`, then run:
   ```bash
   python -m dev_agent.cli --issue 1 --verbose
   ```

The agent should locate `src/math_utils.py`, propose a fix, run the test
suite in a sandbox, and — once both tests pass — open a PR back to this repo.
