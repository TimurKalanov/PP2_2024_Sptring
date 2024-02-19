from datetime import datetime

def drop_microseconds(dt):
    return dt.replace(microsecond=0)
    
current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)
