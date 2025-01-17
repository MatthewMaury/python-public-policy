# Corresponds to the Requirements for homework 6. Requires cloc and nbconvert. Usage:
#
#   python3 ./extras/scripts/hw_6_check.py <assignment>.ipynb

import json
import pandas as pd
import re
import shlex
import subprocess
import sys

MIN_LINES = 40


def handle_process_err(cmd, err):
    if type(cmd) == list:
        cmd = shlex.join(cmd)

    output = err.stderr.decode("utf-8")
    print(
        f"{bcolors.FAIL}ERROR{bcolors.ENDC} while running\n\n\t{cmd}\n\n{output}",
        file=sys.stderr,
    )
    sys.exit(err.returncode)


def get_cmd_output(cmd, input=None, shell=False):
    try:
        process = subprocess.run(
            cmd, capture_output=True, check=True, input=input, shell=shell
        )
    except subprocess.CalledProcessError as err:
        handle_process_err(cmd, err)

    return process.stdout


def get_script(notebook_path):
    return get_cmd_output(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "script",
            "--log-level",
            "WARN",
            "--stdout",
            notebook_path,
        ]
    )


def lines_of_code(code):
    output = get_cmd_output(
        "cloc --stdin-name=script.py --json -", input=code, shell=True
    )
    data = json.loads(output)
    return data["SUM"]["code"]


def code_contains(pattern, code):
    matches = re.search(re.compile(pattern, re.VERBOSE), code)
    return bool(matches)


def has_link(cell):
    pattern = r"https?://"
    if cell["cell_type"] == "code":
        # check for URL in comment
        pattern = r"^\s*#.*" + pattern

    return any(code_contains(pattern, line) for line in cell["source"])


def includes_link(notebook):
    return any(has_link(cell) for cell in notebook["cells"])


def uses_transform(script):
    return code_contains(
        r"""\b(
               concat|
               groupby|
               join|
               melt|
               merge|
               pivot(_table)?|
               resample|
               (un)?stack
            )\(""",
        script,
    )


def has_plotting(script):
    return code_contains(
        r"""\b(
               # visualization packages
               altair|
               bokeh|
               folium|
               geoplotlib|
               geoviews|
               ipyleaflet|
               keplergl|
               matplotlib|
               plotly|
               plotnine|
               pygal|
               seaborn
            )\b
        |
        \.plot[\(\.] # plot submodule/method""",
        script,
    )


# https://stackoverflow.com/a/287944/358804
class bcolors:
    OKGREEN = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def pass_fail(result):
    """Apply ANSI color escape codes"""
    color = bcolors.OKGREEN if result else bcolors.FAIL
    return f"{color}{result}{bcolors.ENDC}"


def exit(results):
    exit_code = 0 if results.all() else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    notebook_path = sys.argv[1]

    script_bytes = get_script(notebook_path)
    script = str(script_bytes)
    notebook = json.load(open(notebook_path))
    num_lines = lines_of_code(script_bytes)

    # use pandas for outputting a table
    results = pd.Series(
        {
            f"Enough lines of code ({num_lines})": num_lines >= MIN_LINES,
            "Includes link": includes_link(notebook),
            "Uses transform": uses_transform(script),
            "Has plotting": has_plotting(script),
        }
    )

    outputs = results.apply(lambda val: pass_fail(val))
    print(outputs.to_string())
    exit(results)
