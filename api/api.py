import pytz
from typing import Dict, List
from datetime import datetime

from fastapi import FastAPI


api = FastAPI()


@api.get("/api/time")
def time() -> Dict[str, str]:
    return {"time": datetime.now().strftime("%H:%M:%S")}


@api.get("/api/date")
def date(tz: str = 'Brazil/East') -> Dict[str, str]:
    return {"date": str(datetime.now(pytz.timezone(tz)))}


@api.get("/api/get_timezones")
def get_timezones() -> Dict[str, List[str]]:
    return {"timezones": pytz.all_timezones}
