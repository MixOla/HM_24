import re
from typing import List, Any

def filter_query(param: str, data: List[str]) -> List[str]:
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: List[str]) -> List[str]:
    col_number: int = int(param)
    return list(map(lambda x: x.split(" ")[col_number], data))


def unique_query(data: str, *args: Any, **kwargs: Any) -> List[str]:
    return list(set(data))


def sort_query(param: str, data: List[str]) -> List[str]:
    reverse: bool = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: List[str]) -> List[str]:
    limit: int = int(param)
    return list(data)[:limit]


def regex_query(param: str, data: List[str]) -> List[str]:
    pattern: re.Pattern = re.compile(param)
    return list(filter(lambda x: re.search(pattern, x), data))