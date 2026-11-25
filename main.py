import os

LINE = (
    "We are all here because nobody wanted to be the person who said "
    "this could have been an email, so we are saying it in person, "
    "for an hour, at ten salaries an hour."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
