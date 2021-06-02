import streamlit as st
import pandas as pd
import yaml
import numpy as np

## Hack to extend the width of the main pane.
def _max_width_():
    max_width_str = f"max-width: 1000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    th {{
        text-align: left;
        font-size: 110%;
       

     }}

    tr:hover {{
        background-color: #ffff99;
        }}

    </style>
    """,
        unsafe_allow_html=True,
    )

DATASET_FOLDER = './dataset/'
params = st.experimental_get_query_params()
datasets = params['dataset']
dataset = 'default'
if len(datasets) > 0:
    dataset = datasets[0]

yaml_path = DATASET_FOLDER+dataset+'.yaml'
try: 
    with open (yaml_path, 'r') as f:
        metadata = yaml.safe_load(f)
except Exception as e:
    print('Error reading the metadata yaml file')

ext = metadata['extension']
if ext[0] == 'csv':
    data = pd.read_csv(DATASET_FOLDER+dataset+'.'+ext[0])

_max_width_()
st.sidebar.image("logo.png", width=300)
st.title("Dataset Viewer")
st.write("Dataset : ", dataset)

col_names = list(data.columns)
filtered_cols = st.multiselect("Choose Columns", col_names, default = col_names)
data = data[filtered_cols]

st.dataframe(data)
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
# print(data)


# import plotly
# import plotly.figure_factory as ff
# hist_data = np.transpose(np.array(data))
# fig = ff.create_distplot(hist_data,col_names)
# st.plotly_chart(fig, use_container_width=True)

# map_data = data.rename(columns = {"high": "lat", "low":"lon"})
# st.map(map_data)

