import re
import subprocess
from pathlib import Path


def test_lazy():
    # Determine the path to the main.py script
    main_file = Path(__file__).parent.parent / "main.py"

    test_1 = [
        "python3",
        main_file,
        "-v",
        "-a",
        "-rep",
        "name1",
        "-as",
        "name2",
        "-t",
        "2w",
        "-s",
    ]

    test_2 = [
        "python3",
        main_file,
        "-v",
        "-r",
        "-rep",
        "name1",
        "-as",
        "none",
        "-t",
        "2w",
        "-s",
    ]

    test_3 = ["python3", main_file, "-v", "-s"]

    try:
        result = subprocess.run(test_1, text=True, capture_output=True, check=True)
        output = result.stdout
        expected_output = "assignee = name2 AND reporter = name1 AND updated >= -2w ORDER BY updated DESC"
        assert (
            expected_output in output
        ), f"Expected:\n{expected_output}\n\nActual:{output}"

        result = subprocess.run(test_2, text=True, capture_output=True, check=True)
        output = result.stdout
        expected_output = "resolution != Unresolved AND reporter = name1 AND updated >= -2w ORDER BY updated DESC"
        assert (
            expected_output in output
        ), f"Expected:\n{expected_output}\n\nActual:{output}"

        result = subprocess.run(test_3, text=True, capture_output=True, check=True)
        output = result.stdout
        expected_output = (
            r"assignee = \S+ AND resolution = Unresolved ORDER BY updated DESC"
        )
        assert re.search(expected_output, output)
    except subprocess.CalledProcessError as e:
        # If the command fails, make the test fail with an error message
        assert False, f"Command failed with error: {e.stderr}"
