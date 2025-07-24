
#!/usr/bin/env python

import argparse, shlex
import os, sys
import shutil
from datetime import date
import importlib
import importlib.util
from collections import namedtuple
import time
import webbrowser

def parse_args():
    today = date.today()
    default_year = today.year if today.month >= 11 else today.year - 1
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, default=default_year)
    parser.add_argument("day", type=int)

    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--open", action="store_true", help="Opens URL to day of challenge")
    action.add_argument("--stub", action="store_true", help="Create scaffolding for challenge")
    action.add_argument("--all", action="store_true", help="Run all samples. If successful, run input.txt")
    action.add_argument("--sample", action="store_true", help="Run all samples")
    action.add_argument("--input", action="store_true", help="Run input.txt")

    argv = (
        # VSCode's ${command:pickArgs} is passed as one string, split it up
        # credit to https://stackoverflow.com/a/78950896
        shlex.split(" ".join(sys.argv[1:]))
        if "USED_VSCODE_COMMAND_PICKARGS" in os.environ
        else sys.argv[1:]
    )

    return parser.parse_args(argv)

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def ensure_file(filepath):
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass # create empty

def stub_files(directory):
    ensure_dir(directory)

    files_to_stub = ["sample.txt", "input.txt"]

    for file in files_to_stub:
        filepath = os.path.join(directory, file)
        ensure_file(filepath)
        if file == "sample.txt":
            with open(filepath, "w") as f:
                f.write("ANSWER:\n")
    soln_filepath = get_soln_path(directory)
    if not os.path.exists(soln_filepath):
        shutil.copyfile("./python/solution_template.py", soln_filepath)


def get_sample_path(directory):
    return os.path.join(directory, "sample.txt")

def get_sampleI_path(directory, idx):
    return os.path.join(directory, f"sample{idx}.txt")

def get_input_path(directory):
    return os.path.join(directory, "input.txt")

def get_soln_path(directory):
    return os.path.join(directory, "solution.py")

def assert_files(directory, try_sample, try_input):
    assert os.path.exists(directory), f"Call with --stub before trying to test ({directory=} did not exist)"
    assert os.path.exists(get_soln_path(directory)), f"{get_soln_path(directory)} does not exist"
    if try_sample:
        base_exists = os.path.exists(get_sample_path(directory))
        num_exists = os.path.exists(get_sampleI_path(directory, 0))
        assert base_exists or num_exists, f"No sample files exist. {get_sample_path(directory)} and {get_sampleI_path(directory, 0)} do not exist"
    if try_input:
        assert os.path.exists(get_input_path(directory)), f"{get_input_path(directory)} does not exist"

def load_file_to_lines(filename):
    with open(filename, "r") as file:
        return [line[:-1] if line[-1] == "\n" else line for line in file]

def run_solution(soln, lines, expected_answer=None):
    answers = soln.run(lines)
    if expected_answer:
        if type(expected_answer) == tuple:
            pass

def extract_answers(lines):
    expected_answer = []
    for i in lines:
        if i.startswith("ANSWER:"):
            answer = i.split(":")[1]
            if answer.isdigit():
                answer = int(answer)
            expected_answer.append(answer)

    lines = lines[len(expected_answer):]

    return tuple(expected_answer), lines

def sec_to_str(sec):
    mins = sec // 60
    sec = sec % 60
    if mins > 0:
        return f"{mins} min and {int(sec)} sec"
    millisec = sec * 1000
    sec = millisec // 1000
    millisec = millisec % 1000
    if millisec < 1:
        return "<1 ms"
    result = ""
    if sec > 0:
        result = f"{int(sec)} sec and "
    return result + f"{int(millisec)} ms"

def test_solution(soln_module, input_path):
    lines = load_file_to_lines(input_path)
    expected_answers, lines = extract_answers(lines)
    print()
    start_time = time.time()
    actual_answers = soln_module.run(lines)
    time_lapsed = time.time() - start_time

    max_answers = max(len(expected_answers), len(actual_answers))

    num_dashes = 52
    print("-" * num_dashes)
    print(f"For {input_path}")
    print(f"Time Lapsed: {sec_to_str(time_lapsed)}")


    for i in range(max_answers):
        no_actual = i >= len(actual_answers) or actual_answers[i] is None
        no_expected = i >= len(expected_answers) or expected_answers[i] is None
        if no_actual and no_expected:
            pass
        elif no_actual:
            print(f"PART {i+1} (MISSING) EXPECTED = {expected_answers[i]}")
        elif no_expected:
            print(f"PART {i+1} (ready to submit?) {actual_answers[i]}")
        elif actual_answers[i] == expected_answers[i]:
            print(f"PART {i+1} (PASS ! ) = {actual_answers[i]}")
        else:
            print(f"PART {i+1} FAIL!")
            if type(actual_answers[i]) != type(expected_answers[i]):
                print(f"EXPECTED       = ({type(expected_answers[i])}) {expected_answers[i]}")
                print(f"ACTUAL (FAIL!) = ({type(actual_answers[i])}) {actual_answers[i]}")
            else:
                print(f"EXPECTED       = {expected_answers[i]}")
                print(f"ACTUAL (FAIL!) = {actual_answers[i]}")
            sys.exit(1)
    print("-" * num_dashes)

def import_solution(directory):
    soln_spec = importlib.util.spec_from_file_location("solution", get_soln_path(directory))
    soln_module = importlib.util.module_from_spec(soln_spec)
    soln_spec.loader.exec_module(soln_module)
    return soln_module

def launch_aoc_website(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"
    print(f"Opening {url=!r} in default browser")
    webbrowser.open(url, new=0, autoraise=True)

def main():
    args = parse_args()

    directory = os.path.join(os.getcwd(), str(args.year), f"day{args.day}")

    if args.stub:
        stub_files(directory)
        return

    if args.open:
        launch_aoc_website(args.year, args.day)
        return

    try_sample = args.all or args.sample
    try_input = args.all or args.input

    assert_files(directory, try_sample, try_input)
    soln_module = import_solution(directory)

    if try_sample:
        idx = 0
        while os.path.exists(get_sampleI_path(directory, idx)):
            test_solution(soln_module, get_sampleI_path(directory, idx))
            idx += 1

        if os.path.exists(get_sample_path(directory)):
            test_solution(soln_module, get_sample_path(directory))

    if try_input:
        test_solution(soln_module, get_input_path(directory))


if __name__ == '__main__':
    main()
