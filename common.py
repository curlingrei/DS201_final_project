from datetime import datetime
def is_valid_yyyy_mm_dd(date_str):
    try:
      datetime.strptime(date_str, "%Y-%m-%d")
      return True
    except ValueError:
      return False