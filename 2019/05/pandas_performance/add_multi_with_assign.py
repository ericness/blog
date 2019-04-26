import typing

import data_generator

TEST_DATA_SIZE = 10000


def get_hierarchy_level(
    hierarchy: str, hierarchy_level: int
) -> typing.Union[str, None]:
    """
    Split the hierarchy into levels and return the selected level.

    :param hierarchy:
        Raw hierarchy string.
    :param hierarchy_level:
        Level of the hierarchy to return. Index is zero-based.
    :return:
        Specified hierarchy level.
    """
    levels = hierarchy.split("::") if hierarchy else []

    return levels[hierarchy_level] if len(levels) > hierarchy_level else None


records = data_generator.generate_hierarchy_records(TEST_DATA_SIZE)

transformed_records = (
    records.assign(
        hierarchyLevelOne=lambda df: df["hierarchy"].apply(
            get_hierarchy_level, hierarchy_level=0
        )
    )
    .assign(
        hierarchyLevelTwo=lambda df: df["hierarchy"].apply(
            get_hierarchy_level, hierarchy_level=1
        )
    )
    .assign(
        hierarchyLevelThree=lambda df: df["hierarchy"].apply(
            get_hierarchy_level, hierarchy_level=2
        )
    )
    .assign(
        hierarchyLevelFour=lambda df: df["hierarchy"].apply(
            get_hierarchy_level, hierarchy_level=3
        )
    )
)

print(transformed_records.head(5).to_string())
