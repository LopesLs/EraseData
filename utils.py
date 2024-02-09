from datetime import datetime, timedelta
import os

def remove_yesterday_file(file_path: str, create_time: datetime) -> bool:
    """
    Remove files that have more than 24 hours created from the current data
    """

    current_date = datetime.now()
    difference = current_date - create_time

    if difference > timedelta(hours=24):
        os.remove(file_path)
        return True

    return "Time left: " + str((timedelta(days=1) - difference))

def get_modified_time(file_path):
    """
    Return the creation time of a file
    """

    create_time = os.path.getmtime(file_path)

    return datetime.fromtimestamp(create_time)
