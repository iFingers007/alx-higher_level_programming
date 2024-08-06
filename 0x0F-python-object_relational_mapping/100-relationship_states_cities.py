#!/usr/bin/python3
"""Module for Creating states"""


def main():
    if len(sys.argv) != 4:
        print("Usage: 100-relationship_states_cities.py <mysql_username> <mysql_password> <database_name>")  # noqa
        return

    # Retrieve MySQL credentials and database name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create a SQLAlchemy engine to connect to the MySQL database
    engine = create_engine(
        f'mysql+mysqlconnector://{mysql_username}:{mysql_password}@localhost:3306/{database_name}',  # noqa
        pool_pre_ping=True
    )

    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a State with an associated City
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)

    # Add the state and city to the session and commit
    session.add(new_state)
    session.commit()

    # Print a confirmation message
    print(f"State '{new_state.name}' with City '{new_city.name}' added to the database.")  # noqa

    # Close the session
    session.close()


if __name__ == '__main__':
    main()
