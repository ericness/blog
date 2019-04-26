import copy
import pandas as pd

import data_generator

TEST_DATA_SIZE = 10000


def append_hierarchy_levels(record: pd.Series) -> pd.Series:
    """
    Split the hierarchy into levels and append then to `record`.

    :param record:
        Series containing hierarchy fields.
    :return:
        Series with hierarchy levels appended.
    """
    updated_ticket = copy.deepcopy(record)
    levels = record["hierarchy"].split("::") if record["hierarchy"] else []
    indexes = [
        "hierarchyLevelOne",
        "hierarchyLevelTwo",
        "hierarchyLevelThree",
        "hierarchyLevelFour",
    ]

    for index in indexes:
        updated_ticket[index] = levels.pop(0) if len(levels) > 0 else None
    return updated_ticket


records = data_generator.generate_hierarchy_records(TEST_DATA_SIZE)

transformed_records = records.apply(
    append_hierarchy_levels, axis="columns"
)

print(transformed_records.head(5).to_string())
