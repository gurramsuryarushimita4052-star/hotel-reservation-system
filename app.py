
import streamlit as st

from database import (
    create_tables,
    insert_rooms,
    add_customer
)

# Initialize database
create_tables()
insert_rooms()

# Page configuration
st.set_page_config(
    page_title="Hotel Reservation System",
    page_icon="🏨",
    layout="centered"
)

# Main heading
st.title("🏨 Hotel Reservation System")

st.write("Welcome to our Hotel Reservation System!")

st.divider()

# Customer registration
st.header("Customer Registration")

with st.form("customer_form"):

    name = st.text_input("Customer Name")

    phone = st.text_input("Phone Number")

    email = st.text_input("Email Address")

    submit = st.form_submit_button("Register Customer")

    if submit:

        if name.strip() and phone.strip():

            add_customer(name, phone, email)

            st.success("Customer registered successfully!")

        else:
            st.error("Please enter your name and phone number.")