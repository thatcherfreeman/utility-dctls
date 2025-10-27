import os
import argparse
import re

EXTENSIONS = (".dctl", ".h")

def lint_dctl(file):
    print(f"Linting {file}")

    # Identify any doubles in the file and put f at the end of them
    def convert_to_float(match: re.Match[str]):
        fl = match.group(0)
        if fl.endswith("f"):
            return fl
        return fl + "f"

    pattern = re.compile(
        r"(?<![A-Za-z0-9_])[-+]?(?:(?:\d+\.\d*|\.\d+)(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![fF\w])"
    )

    skip_prefixes = ("DEFINE_UI_PARAMS(", "DEFINE_UI_TOOLTIP(")

    new_lines = []
    with open(file, "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        for line in all_lines:
            stripped = line.strip()

            # Skip if line is a comment or starts with DEFINE macros
            if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*") or stripped.startswith(skip_prefixes):
                new_lines.append(line)
                continue

            # Skip if line has quotation marks in it (strings).
            if '"' in stripped or "'" in stripped:
                new_lines.append(line)
                continue

            matches = re.findall(pattern, line)
            new_line, num_changes = re.subn(pattern, convert_to_float, line)
            new_lines.append(new_line)
            if num_changes:
                print("", line.strip(), " >>> ", matches, "\n", new_line.strip())

    with open(file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=str, help="Directory of DCTL or .h files to lint.")
    args = parser.parse_args()

    target_dir = args.directory

    if os.path.isdir(target_dir):
        for file in os.listdir(target_dir):
            if any([file.endswith(ext) for ext in EXTENSIONS]):
                assert lint_dctl(os.path.join(target_dir, file)), f"Failed to lint file {file}"

    elif os.path.isfile(target_dir):
        file = target_dir
        if any([file.endswith(ext) for ext in EXTENSIONS]):
            assert lint_dctl(file), f"Failed to lint file {file}"

    else:
        assert False, f"Invalid directory {target_dir}"

    print(f"Completed cleanup of {target_dir}")

if __name__ == "__main__":
    main()