import streamlit as st
import pandas as pd

# Placeholder data
farm_data = {
    'Farm Name': ['Farm A', 'Farm B', 'Farm C'],
    'Location': ['Location A', 'Location B', 'Location C'],
    'Crop': ['Wheat', 'Corn', 'Soybean'],
    'Livestock': ['Cattle', 'Pigs', 'Chickens'],
    'Area (acres)': [100, 200, 150],
    'Livestock Count': [50, 200, 150],
    'Feeding Schedule': ['Twice a day', 'Three times a day', 'Once a day'],
    'Health Status': ['Good', 'Excellent', 'Fair']
}

# Create a session state for the DataFrame
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(farm_data)

def main():
    st.title('Farm Management App')

    # Sidebar with options
    st.sidebar.title('Menu')
    page = st.sidebar.radio('Select a page', ['Home', 'Crop Management', 'Livestock Tracking', 'Tasks'])

    df = st.session_state.df

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
        st.write(f"**Livestock Count:** {livestock_info['Livestock Count']}")
        st.write(f"**Feeding Schedule:** {livestock_info['Feeding Schedule']}")
        st.write(f"**Health Status:** {livestock_info['Health Status']}")

        # Input widget to change health status
        new_health_status = st.selectbox('Change Health Status', ['Good', 'Fair', 'Poor', 'Excellent'], index=['Good', 'Fair', 'Poor', 'Excellent'].index(livestock_info['Health Status']))
        if st.button('Update Health Status'):
            # Update the DataFrame with the new health status
            df.loc[df['Livestock'] == selected_livestock, 'Health Status'] = new_health_status
            st.session_state.df = df  # Update session state

            st.write(f"Health status of {selected_livestock} updated to {new_health_status}")

            # Display the updated information
            livestock_info = df[df['Livestock'] == selected_livestock].iloc[0]
            st.write(f"**Health Status:** {livestock_info['Health Status']}")

    elif page == 'Tasks':
        st.subheader('Task Management')
        st.write('Manage your farm tasks here.')

        task = st.text_area('Enter a new task')
        if st.button('Add Task'):
            st.write(f'New task added: {task}')
    
if __name__ == '__main__':
    main()
