import cli
import db_conection
import db_setup

connection = db_conection.set_connection(db_setup.DATABASE)


def main():
    db_setup.main()
    cli.ims_flow(connection)


if __name__ == "__main__":
    main()
