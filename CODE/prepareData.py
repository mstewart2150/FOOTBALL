import nfl_data_py as nfl
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
#pd.reset_option('display.max_columns')


year = [2023]
df_depth = nfl.import_depth_charts(year)
df_pbp = nfl.import_pbp_data(year, downcast=True, cache=False, alt_path=None)


df_qb_throw = df_pbp[df_pbp['time_to_throw'] != np.nan]
df_qb_throw_summary = df_qb_throw.groupby(['season_type', 'pass_length', 'passer_player_name'])['time_to_throw'].min().reset_index().sort_values(['time_to_throw', 'passer_player_name'])