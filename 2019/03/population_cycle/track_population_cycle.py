from datetime import datetime
import pandas as pd

import displayer
import interpolator
import standardizer
import generator

START_DATE = datetime(2018, 1, 1)
START_DATE_OFFSET = 90
END_DATE_OFFSET = 90
END_DATE_MIN_OFFSET = 60
VALUE_SCALE = 1.5
NOISE_SCALE = 0.3
NOISE_SEGMENTS = 12

INTERPOLATION_POINTS = 100
POPULATION_COUNT = 20
QUANTILES = [0.25, 0.5, 0.75]

if __name__ == "__main__":

    customer_activity = {}
    for customer_id in range(POPULATION_COUNT):

        customer_activity[customer_id] = generator.generate_time_series(
            start_date=START_DATE,
            start_date_offset=START_DATE_OFFSET,
            end_date_offset=END_DATE_OFFSET,
            end_date_min_offset=END_DATE_MIN_OFFSET,
            value_scale=VALUE_SCALE,
            noise_scale=NOISE_SCALE,
            noise_segments=NOISE_SEGMENTS,
        )

    displayer.graph_timelines(customer_activity)

    customer_activity_std = {
        customer_id: standardizer.standardize_timeline(activity)
        for customer_id, activity in customer_activity.items()
    }

    displayer.graph_timelines(customer_activity_std)

    customer_activity_int = {
        customer_id: interpolator.interpolate_time_series(
            activity, n_points=INTERPOLATION_POINTS
        )
        for customer_id, activity in customer_activity_std.items()
    }

    displayer.graph_timelines(customer_activity_int)

    customer_activity_df = pd.DataFrame(customer_activity_int).T

    interpolated_quantiles = customer_activity_df.quantile(q=QUANTILES, axis=0)

    displayer.graph_quantiles(interpolated_quantiles)
