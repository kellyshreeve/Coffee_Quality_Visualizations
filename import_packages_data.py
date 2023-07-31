## IMPORT PACKAGES AND DATA
# Import Packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Import Data
coffee = pd.read_excel('/Users/kellyshreeve/Desktop/Data-Sets/df_arabica_clean.xlsx', header=0, index_col=0)
