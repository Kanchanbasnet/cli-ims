import cli
import db_setup


def main():
    db_setup.main()
    cli.main()


if __name__ == "__main__":
    main()
