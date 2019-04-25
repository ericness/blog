import pandas as pd
import uuid


def generate_hierarchy():
    """Returns four UUIDs separated by double colons."""
    return "::".join([str(uuid.uuid4()) for _ in range(4)])


def generate_hierarchy_records():
    """Returns DataFrame of hierarchy records"""
    return pd.DataFrame(
        data={"hierarchy": [generate_hierarchy() for _ in range(100)]}
    )
