import streamlit as st
import pandas as pd
import datetime
a=st.text_input("enter farm name")
b=st.text_input("enter farm name")
c=st.text_input("enter farm name")
d=st.text_input("enter location name")
e=st.text_input("enter location name")
f=st.text_input("enter location name")
g=st.text_input("enter crop name")
h=st.text_input("enter crop name")
i=st.text_input("enter crop name")
j=st.text_input("enter livestock name")
k=st.text_input("enter livestock name")
l=st.text_input("enter livestock name")
m=st.text_input("enter area name")
n=st.text_input("enter area name")
o=st.text_input("enter area name")
# Placeholder data 
farm_data = {
    'Farm Name': [a,b,c],
    'Location': [d, e, f],
    'Crop': [g,h,i],
    'Livestock': [j, k, l],
    'Area (acres)': [m, n, o]
}

df = pd.DataFrame(farm_data)

def main():
    st.title('Farm Management App')

    # Sidebar with options
    st.sidebar.title('Menu')
    page = st.sidebar.radio('Select a page', ['Home', 'Crop Management', 'Livestock Tracking', 'Tasks'])

    if page == 'Home':
        st.subheader('Farm Overview')
        st.write(df)  # Display farm data

    elif page == 'Crop Management':
        st.subheader('Crop Management')
        st.write('Select a crop to manage:')

        selected_crop = st.selectbox('Select Crop', df['Crop'].unique())
        crop_info = df[df['Crop'] == selected_crop].iloc[0]

        st.write(f"**Crop Name:** {crop_info['Crop']}")
        st.write(f"**Farm Name:** {crop_info['Farm Name']}")
        st.write(f"**Location:** {crop_info['Location']}")
        st.write(f"**Area (acres):** {crop_info['Area (acres)']}")

    elif page == 'Livestock Tracking':
        st.subheader('Livestock Tracking')
        st.write('Select a livestock to track:')

        selected_livestock = st.selectbox('Select Livestock', df['Livestock'].unique())
        livestock_info = df[df['Livestock'] == selected_livestock].iloc[0]

        st.write(f"**Livestock Type:** {livestock_info['Livestock']}")
        st.write(f"**Farm Name:** {livestock_info['Farm Name']}")
        st.write(f"**Location:** {livestock_info['Location']}")
        st.write(f"**Area (acres):** {livestock_info['Area (acres)']}")

    elif page == 'Tasks':
        st.subheader('Task Management')
        st.write('Manage your farm tasks here.')

        task = st.text_area('Enter a new task')
        if st.button('Add Task'):
            st.write(f'New task added: {task}')
    
if __name__ == '__main__':
    main()



