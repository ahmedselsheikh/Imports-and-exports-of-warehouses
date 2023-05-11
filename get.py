import pandas as pd
import streamlit as st

df = pd.read_excel('مخازن سباكة وكهرباء.xlsx', sheet_name='المنصرف',
                   skiprows=4)
st.set_page_config(layout='wide')

column_names = df.columns[1:17]

# Select columns to filter
filter_columns = st.multiselect('Select column to filter:',
                                options=column_names)

filtered_df = df.copy()
for col in filter_columns:
    data_to_filter = df[col].unique().tolist()
    selected_data_to_filter = st.multiselect(f'select {col} data to filter', options=data_to_filter)
    filtered_df = filtered_df[filtered_df[col].isin(selected_data_to_filter)]

st.write(filtered_df)

sum_by_material_name = filtered_df.groupby('اسم الخامة')['الكمية'].sum()


# Add the 'الوحدة' column to the grouped DataFrame
# sum_by_material_name = sum_by_material_name.reset_index()
# print(sum_by_material_name)
# unit_column = filtered_df.groupby('اسم الخامة')['الوحدة'].first()
# sum_by_material_name['الوحدة'] = unit_column.values

# Add the 'الوحدة' column to the grouped DataFrame
sum_by_material_name = sum_by_material_name.reset_index()
unit_column = filtered_df.groupby('اسم الخامة')['الوحدة'].first()
sum_by_material_name.insert(1, 'الوحدة', unit_column.values)


st.dataframe(sum_by_material_name, width=500)





