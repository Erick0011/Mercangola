from datetime import datetime
import pytz

def get_local_time(timezone_str="Africa/Luanda"):
    """Retorna a data e hora no fuso horário especificado."""
    tz = pytz.timezone(timezone_str)
    return datetime.now(pytz.utc).astimezone(tz)
