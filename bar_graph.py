# -*- coding: utf-8 -*-
"""bar graph.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZPYiPTiY0CKK_qfOcBJj-JAPKe0ozkaz
"""

import pandas as pd

df_EnergySource = pd.read_csv ('electric utility .csv')

df_EnergySource.loc[0:5,:]

df_EnergySourc.plot.bar(x='Electric utilities', y='Year 2020')

