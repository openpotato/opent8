import argparse
import json
import sys

from pathlib import Path
from jsonschema import FormatChecker
from jsonschema.validators import validator_for


def annotate(file: Path, message: str):
    message = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::error file={file}::{message}")


def validate(json_file: Path, schema_file: Path) -> bool:
    with schema_file.open(encoding="utf-8") as f:
        schema = json.load(f)

    with json_file.open(encoding="utf-8") as f:
        data = json.load(f)

    validator_class = validator_for(schema)
    validator_class.check_schema(schema)

    validator = validator_class(schema, format_checker=FormatChecker())

    errors = sorted(
        validator.iter_errors(data),
        key=lambda error: tuple(str(p) for p in error.absolute_path),
    )

    for error in errors:
        location = "/" + "/".join(str(p) for p in error.absolute_path)
        annotate(json_file, f"{location}: {error.message}")

    if errors:
        print(f"FAILED: {json_file} ({len(errors)} errors)")
        return False

    print(f"VALID: {json_file}")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file", type=Path)
    parser.add_argument("schema_file", type=Path)
    args = parser.parse_args()

    try:
        return 0 if validate(args.json_file, args.schema_file) else 1
    except Exception as error:
        annotate(args.json_file, str(error))
        return 2


if __name__ == "__main__":
    sys.exit(main())
