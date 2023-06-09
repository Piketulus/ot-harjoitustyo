from entities.statistic import Statistic
from database_connection import get_database_connection


def get_stat_by_row(row):
    """
     Get Statistic object from row. This is used to create Statistic object from database row. 
     The row should be a dictionary with keys name time difficulty date

     Args:
         row: Dictionary with keys name time difficulty date

     Returns: 
         Statistic object or None if not found in the row
    """
    return Statistic(row["name"], row["time"], row["difficulty"], row["date"]) if row else None


class StatisticRepository:
    """
    Class responsible for handling the statistics in the database.
    """

    def __init__(self, connection):
        """
         Initialize the class.

         Args:
                 connection: The connection to the database
        """

        self._connection = connection

    def find_all(self):
        """
        Find all stats in the database.

        Returns: 
            list of Statistic objects in the database
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from stats")
        rows = cursor.fetchall()
        return list(map(get_stat_by_row, rows))

    def find_all_by_filter(self, name, maxtime, difficulty):
        """
        Find all stats matching a filter. This is useful for filtering by names and difficulty.

        Args:
            name: The name to search for.
            maxtime: The maximum time in seconds that the statistics time value can be
            difficulty: The value of the difficulty of the statistic

        Returns: 
            A list of Statistic objects that match the filter. 
            If there are no matches an empty list is returned
        """

        name = "%" + name + "%"

        cursor = self._connection.cursor()

        if difficulty == "All":
            cursor.execute(
                "select * from stats where name like ? and time <= ?",
                (name, maxtime)
            )
        else:
            cursor.execute(
                "select * from stats where name like ? and time <= ? and difficulty = ?",
                (name, maxtime, difficulty)
            )
        rows = cursor.fetchall()
        return list(map(get_stat_by_row, rows))

    def create(self, statistic):
        """
        Create a new statistic in the database.

        Args:
            statistic: The Statistic object used to create the entry
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "insert into stats (name, time, difficulty, date) values (?, ?, ?, ?)",
            (statistic.name, statistic.time, statistic.difficulty, statistic.date)
        )
        self._connection.commit()

    def delete_all(self):
        """
        Delete all stats from the database.
        """

        cursor = self._connection.cursor()
        cursor.execute("delete from stats")
        self._connection.commit()


statistic_repository = StatisticRepository(get_database_connection())
