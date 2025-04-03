import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model and encoded values
with open(r"final_model.pkl", 'rb') as model_file:
    model = pickle.load(model_file)
# Load the encoded values
with open(r"mapping_data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

st.set_page_config(page_title="Singapore Flat Resale Price Predictor", page_icon="🏡", layout="wide")
st.sidebar.header("Explore Options")
page = st.sidebar.radio("Select a Page", options=["Home", "Price Prediction"])

if page == "Home":
    st.title("Singapore Flat Resale Price Predictor 🏡")
    st.write("Welcome to the **Singapore Flat Resale Price Predictor**, a user-friendly tool designed to help buyers and sellers estimate the resale value of flats in Singapore. Whether you're planning to buy your dream home or sell your current flat, this app provides accurate price predictions based on historical resale data and advanced machine learning techniques.")

    st.header("About the Project")
    st.write("The resale flat market in Singapore is competitive, and pricing can be influenced by various factors such as location, flat type, floor area, and lease duration. This application leverages historical resale transaction data to predict flat prices, giving users valuable insights to make informed decisions.")

    st.subheader("Key Features:")
    st.markdown("- **Accurate Predictions**: Powered by a machine learning model trained on years of resale transaction data.")
    st.markdown("- **User-Friendly Interface**: Enter details such as town, flat type, storey range, floor area, and lease commence date to get an instant price estimate.")
    st.markdown("- **Comprehensive Insights**: Built using data from the Singapore Housing and Development Board (HDB) from 1990 to the present.")

    st.header("How It Works")
    st.write("1. **Input Details**: Provide information about the flat, including its location, type, floor area, and more.")
    st.write("2. **Predict Resale Price**: The app uses a machine learning model to analyze the input data and predict the flat's resale price.")
    st.write("3. **Get Results**: View the predicted price to your appropriate decision-making.")

    st.header("Why Use This Tool?")
    st.markdown("- **Save Time**: Quickly estimate resale prices without manual research.")
    st.markdown("- **Data-Driven Decisions**: Rely on insights generated from real historical data.")
    st.markdown("- **Empowering Users**: Simplify the complex process of understanding flat pricing.")

    st.header("Behind the Scenes")
    st.write("This application was built using:")
    st.markdown("- **Machine Learning Models**: Carefully trained and evaluated using metrics like MAE, RMSE, and R² score.")
    st.markdown("- **Streamlit**: For an interactive and intuitive user interface.")
    st.markdown("- **Deployment**: Hosted on the Render platform for easy accessibility.")

    st.header("Get Started")
    st.write("Simply fill in the required details about your flat to begin exploring the resale price predictions. Our tool is here to assist you in navigating the Singapore flat resale market with confidence.")

    st.markdown("---")
    st.write("**Start Exploring Now!**")

elif page == "Price Prediction":
    st.title("Resale Price Prediction 🏠")
    st.write("Please enter the inputs vertically, first in the first column and then in the second column.")
    col1, col2 = st.columns(2)
    with col1:
        selected_town = st.selectbox("Select a Town", options=["Select"] + list(loaded_data["town_street_map"].keys()))
        selected_street = st.selectbox("Select a Street", options=["Select"] + list(loaded_data["town_street_map"].get(selected_town, [])))
        block = st.number_input("Enter Block Number (sample 1 to 250 but you can give nay number)", min_value=0, max_value=985, step=1)
        flat_type = st.selectbox("Select Flat Type", options=["Select"] + list(loaded_data["flat_type_model_map"].keys()))
        flat_model = st.selectbox("Select Flat Model", options=["Select"] + list(loaded_data["flat_type_model_map"].get(flat_type, [])))
    with col2:
        storey_range = st.selectbox("Select Storey Range", options=["Select"] + list(loaded_data["flat_model_storey_range_map"].get(flat_model, [])))
        floor_area_sqm = st.number_input("Floor Area (in sqm)", min_value=1.0, step=0.1)
        lease_commence_year = st.selectbox("Select Lease Commence Year", list(range(1966, 2021)))
        resale_year = st.selectbox("Select Resale Year", list(range(1990, 2025)))
        resale_month = st.selectbox("Select Resale Month", list(range(1, 13)))

    # Encode categorical values based on loaded mappings
    encoded_town = loaded_data["town_encoded"].get(selected_town) if selected_town != "Select" else None
    encoded_street = loaded_data["street_name"].get(selected_street) if selected_street else None
    encoded_flat_type = loaded_data["flat_type"].get(flat_type) if flat_type != "Select" else None
    encoded_flat_model = loaded_data["flat_model"].get(flat_model) if flat_model else None
    encoded_storey_range = loaded_data["storey_range"].get(storey_range) if storey_range else None
    encoded_block = loaded_data["block_group_enc"].get(str(block))  

    # Calculate lease difference
    lease_year_difference = resale_year - lease_commence_year

    # Collecting user inputs into a dictionary
    user_input = {'floor_area_sqm': floor_area_sqm,'lease_commence_year': lease_commence_year,'year': resale_year,'month': resale_month,
        'lease_years_difference': lease_year_difference,'storey_range': encoded_storey_range,'flat_type': encoded_flat_type,
        'flat_model': encoded_flat_model,'town_encoded': encoded_town,'street_name_encoded': encoded_street,'block_group_enc': encoded_block}

    # Convert input to DataFrame
    user_input_df = pd.DataFrame([user_input])
    col1, col2, col3 = st.columns(3)
    with col2:
        # Predict Button and Display Result
        if st.button("Predict Resale Price"):
            if None in user_input.values():
                st.error("Please fill in all the required fields before predicting.")
            else:
                # Prepare the input array for prediction
                user_input_array = user_input_df.to_numpy()
                predicted_price = model.predict(user_input_array)
            st.success(f"The predicted resale price for the input you have provided is : **{predicted_price[0]:,.2f}**")
