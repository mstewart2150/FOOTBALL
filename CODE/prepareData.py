import nfl_data_py as nfl
import numpy as np

year = [2023]
df_depth = nfl.import_depth_charts(year)
df_pbp = nfl.import_pbp_data(year, downcast=True, cache=False, alt_path=None)


df_qb_throw = df_pbp[df_pbp['time_to_throw'] != np.nan]