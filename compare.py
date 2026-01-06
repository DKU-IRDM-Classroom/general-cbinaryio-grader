import sys

from pathlib import Path


def read_data(file_path: Path) -> bytes:

    try:
        data = file_path.open('rb').read()
    except Exception:
        sys.exit(2)

    return data


def main():

    if len(sys.argv) != 3:
        sys.exit(3)

    ans_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    data_ans = read_data(ans_path)
    data_out = read_data(out_path)

    if len(data_ans) != len(data_out):
        sys.exit(2)

    if data_ans != data_out:
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
