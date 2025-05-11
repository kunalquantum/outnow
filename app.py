import streamlit as st
from datetime import date
import pandas as pd
import os
import json

# File paths for JSON storage
ADMIN_DATA_PATH = "admin_data.json"
WORKER_DATA_PATH = "worker_data.json"
USERS_DATA_PATH = "users.json"  # New file for storing user credentials
PAYMENTS_DATA_PATH = "payments_data.json"  # New file for storing payment settlements

# Functions for loading and saving data from JSON files
def load_admin_data():
    if os.path.exists(ADMIN_DATA_PATH):
        with open(ADMIN_DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_admin_data(data):
    with open(ADMIN_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def load_worker_data():
    if os.path.exists(WORKER_DATA_PATH):
        with open(WORKER_DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_worker_data(data):
    with open(WORKER_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def load_payments_data():
    if os.path.exists(PAYMENTS_DATA_PATH):
        with open(PAYMENTS_DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_payments_data(data):
    with open(PAYMENTS_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def load_users():
    if os.path.exists(USERS_DATA_PATH):
        with open(USERS_DATA_PATH, "r") as f:
            return json.load(f)
    # Default users if file doesn't exist
    default_users = [
        {"username": "admin", "password": "admin123", "role": "admin"},
        {"username": "worker", "password": "worker123", "role": "worker"}
    ]
    save_users(default_users)
    return default_users

def save_users(users):
    with open(USERS_DATA_PATH, "w") as f:
        json.dump(users, f, indent=4)

# Set page configuration
st.set_page_config(
    page_title="Bread Distribution System",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🍞"
)

# Load custom CSS
def load_css():
    with open("style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Try to load CSS if file exists
if os.path.exists("style.css"):
    load_css()

# Initialize session state variables
if 'admin_data' not in st.session_state:
    st.session_state.admin_data = load_admin_data() or default_admin_data
    if not load_admin_data():
        save_admin_data(default_admin_data)
    
if 'worker_data' not in st.session_state:
    st.session_state.worker_data = load_worker_data() or []
    
if 'date_filter' not in st.session_state:
    st.session_state.date_filter = str(date.today())

# Initialize user authentication variables
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
    
if 'username' not in st.session_state:
    st.session_state.username = ""
    
if 'user_role' not in st.session_state:
    st.session_state.user_role = ""

# Initialize data with pre-populated admin data if none exists
default_admin_data = [
    {"SR.NO": 1, "SKU NAME": "LARGE 350", "AW RATE": 31.75, "DIFF1": 2.05, "DEL.B.RATE": 33.80, "DIFF2": 1.45, "RETAILOR RATE": 35.25, "JALI": 35, "JALI QUA": 24, "TOTAL QUA": 840},
    {"SR.NO": 2, "SKU NAME": "ECO 800", "AW RATE": 62.50, "DIFF1": 3.30, "DEL.B.RATE": 65.80, "DIFF2": 2.70, "RETAILOR RATE": 68.50, "JALI": 4, "JALI QUA": 15, "TOTAL QUA": 60},
    {"SR.NO": 3, "SKU NAME": "HALF 150", "AW RATE": 15.60, "DIFF1": 1.20, "DEL.B.RATE": 16.80, "DIFF2": 0.70, "RETAILOR RATE": 17.50, "JALI": 15, "JALI QUA": 48, "TOTAL QUA": 720},
    {"SR.NO": 4, "SKU NAME": "POP 500", "AW RATE": 39.20, "DIFF1": 2.30, "DEL.B.RATE": 41.50, "DIFF2": 1.50, "RETAILOR RATE": 43.00, "JALI": 1, "JALI QUA": 20, "TOTAL QUA": 20},
    {"SR.NO": 5, "SKU NAME": "BR 400", "AW RATE": 38.70, "DIFF1": 2.25, "DEL.B.RATE": 40.95, "DIFF2": 1.55, "RETAILOR RATE": 42.50, "JALI": 2, "JALI QUA": 24, "TOTAL QUA": 48},
    {"SR.NO": 6, "SKU NAME": "FRT 200", "AW RATE": 19.30, "DIFF1": 1.25, "DEL.B.RATE": 20.55, "DIFF2": 0.95, "RETAILOR RATE": 21.50, "JALI": 2, "JALI QUA": 35, "TOTAL QUA": 70},
    {"SR.NO": 7, "SKU NAME": "H.ATTA 200", "AW RATE": 18.20, "DIFF1": 2.30, "DEL.B.RATE": 20.50, "DIFF2": 1.50, "RETAILOR RATE": 22.00, "JALI": 1, "JALI QUA": 48, "TOTAL QUA": 48},
    {"SR.NO": 8, "SKU NAME": "MD 200", "AW RATE": 16.50, "DIFF1": 0.70, "DEL.B.RATE": 17.20, "DIFF2": 0.80, "RETAILOR RATE": 18.00, "JALI": 0, "JALI QUA": 42, "TOTAL QUA": 0},
    {"SR.NO": 9, "SKU NAME": "MG 400", "AW RATE": 46.50, "DIFF1": 3.90, "DEL.B.RATE": 50.40, "DIFF2": 2.60, "RETAILOR RATE": 53.00, "JALI": 2, "JALI QUA": 24, "TOTAL QUA": 48},
    {"SR.NO": 10, "SKU NAME": "WW 450", "AW RATE": 41.75, "DIFF1": 2.80, "DEL.B.RATE": 44.55, "DIFF2": 1.95, "RETAILOR RATE": 46.50, "JALI": 24, "JALI QUA": 24, "TOTAL QUA": 576},
    {"SR.NO": 11, "SKU NAME": "WW 250", "AW RATE": 23.60, "DIFF1": 1.30, "DEL.B.RATE": 24.90, "DIFF2": 1.10, "RETAILOR RATE": 26.00, "JALI": 0, "JALI QUA": 42, "TOTAL QUA": 0},
    {"SR.NO": 12, "SKU NAME": "H.SLICE 450", "AW RATE": 39.20, "DIFF1": 2.30, "DEL.B.RATE": 41.50, "DIFF2": 1.50, "RETAILOR RATE": 43.00, "JALI": 2, "JALI QUA": 15, "TOTAL QUA": 30},
    {"SR.NO": 13, "SKU NAME": "600 GM", "AW RATE": 50.00, "DIFF1": 3.60, "DEL.B.RATE": 53.60, "DIFF2": 3.40, "RETAILOR RATE": 57.00, "JALI": 16, "JALI QUA": 15, "TOTAL QUA": 240},
    {"SR.NO": 14, "SKU NAME": "BR200", "AW RATE": 21.20, "DIFF1": 2.00, "DEL.B.RATE": 23.20, "DIFF2": 1.30, "RETAILOR RATE": 24.50, "JALI": 7, "JALI QUA": 48, "TOTAL QUA": 336},
    {"SR.NO": 15, "SKU NAME": "MG200", "AW RATE": 23.00, "DIFF1": 1.70, "DEL.B.RATE": 24.70, "DIFF2": 1.30, "RETAILOR RATE": 26.00, "JALI": 1, "JALI QUA": 24, "TOTAL QUA": 24},
    {"SR.NO": 16, "SKU NAME": "WW350", "AW RATE": 30.50, "DIFF1": 2.00, "DEL.B.RATE": 32.50, "DIFF2": 1.50, "RETAILOR RATE": 34.00, "JALI": 0, "JALI QUA": 15, "TOTAL QUA": 0},
    {"SR.NO": 17, "SKU NAME": "AT400", "AW RATE": 0.00, "DIFF1": 0.00, "DEL.B.RATE": 0.00, "DIFF2": 0.00, "RETAILOR RATE": 0.00, "JALI": 0, "JALI QUA": 24, "TOTAL QUA": 0},
    {"SR.NO": 18, "SKU NAME": "BUN70", "AW RATE": 7.50, "DIFF1": 0.60, "DEL.B.RATE": 8.10, "DIFF2": 0.40, "RETAILOR RATE": 8.50, "JALI": 10, "JALI QUA": 24, "TOTAL QUA": 240},
    {"SR.NO": 19, "SKU NAME": "AK", "AW RATE": 30.00, "DIFF1": 3.00, "DEL.B.RATE": 33.00, "DIFF2": 1.00, "RETAILOR RATE": 34.00, "JALI": 0, "JALI QUA": 9, "TOTAL QUA": 0},
    {"SR.NO": 20, "SKU NAME": "MK", "AW RATE": 30.00, "DIFF1": 3.00, "DEL.B.RATE": 33.00, "DIFF2": 1.00, "RETAILOR RATE": 34.00, "JALI": 0, "JALI QUA": 9, "TOTAL QUA": 0},
    {"SR.NO": 21, "SKU NAME": "BUR200", "AW RATE": 30.00, "DIFF1": 3.00, "DEL.B.RATE": 33.00, "DIFF2": 1.00, "RETAILOR RATE": 34.00, "JALI": 0, "JALI QUA": 6, "TOTAL QUA": 0},
    {"SR.NO": 22, "SKU NAME": "BUR100", "AW RATE": 19.50, "DIFF1": 1.35, "DEL.B.RATE": 20.85, "DIFF2": 0.65, "RETAILOR RATE": 21.50, "JALI": 0, "JALI QUA": 20, "TOTAL QUA": 0},
    {"SR.NO": 23, "SKU NAME": "PAV250", "AW RATE": 19.50, "DIFF1": 1.35, "DEL.B.RATE": 20.85, "DIFF2": 0.65, "RETAILOR RATE": 21.50, "JALI": 1, "JALI QUA": 16, "TOTAL QUA": 16},
    {"SR.NO": 24, "SKU NAME": "GAR300", "AW RATE": 34.50, "DIFF1": 2.30, "DEL.B.RATE": 36.80, "DIFF2": 1.70, "RETAILOR RATE": 38.50, "JALI": 1, "JALI QUA": 12, "TOTAL QUA": 12},
    {"SR.NO": 25, "SKU NAME": "B.PAV250", "AW RATE": 23.50, "DIFF1": 1.50, "DEL.B.RATE": 25.00, "DIFF2": 1.00, "RETAILOR RATE": 26.00, "JALI": 1, "JALI QUA": 6, "TOTAL QUA": 6},
    {"SR.NO": 26, "SKU NAME": "VA50", "AW RATE": 7.70, "DIFF1": 0.40, "DEL.B.RATE": 8.10, "DIFF2": 0.40, "RETAILOR RATE": 8.50, "JALI": 6, "JALI QUA": 42, "TOTAL QUA": 252},
    {"SR.NO": 27, "SKU NAME": "CHOC50", "AW RATE": 7.70, "DIFF1": 0.40, "DEL.B.RATE": 8.10, "DIFF2": 0.40, "RETAILOR RATE": 8.50, "JALI": 1, "JALI QUA": 42, "TOTAL QUA": 42},
    {"SR.NO": 28, "SKU NAME": "MP150", "AW RATE": 25.43, "DIFF1": 2.92, "DEL.B.RATE": 28.35, "DIFF2": 1.65, "RETAILOR RATE": 30.00, "JALI": 2, "JALI QUA": 12, "TOTAL QUA": 24},
    {"SR.NO": 29, "SKU NAME": "M.BUN", "AW RATE": 14.00, "DIFF1": 1.00, "DEL.B.RATE": 15.00, "DIFF2": 2.00, "RETAILOR RATE": 17.00, "JALI": 40, "JALI QUA": 1, "TOTAL QUA": 40},
    {"SR.NO": 30, "SKU NAME": "M.BUN", "AW RATE": 14.00, "DIFF1": 1.00, "DEL.B.RATE": 15.00, "DIFF2": 2.00, "RETAILOR RATE": 17.00, "JALI": 0, "JALI QUA": 1, "TOTAL QUA": 0},
    {"SR.NO": 31, "SKU NAME": "SLICE", "AW RATE": 7.00, "DIFF1": 0.80, "DEL.B.RATE": 7.80, "DIFF2": 1.20, "RETAILOR RATE": 9.00, "JALI": 70, "JALI QUA": 1, "TOTAL QUA": 70}
]

# Authentication Function
def authenticate(username, password):
    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.user_role = user["role"]
            return True
    return False

# Logout Function
def logout():
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.user_role = ""

# Display Login Form
if not st.session_state.authenticated:
    # Initialize registration mode state if not exist
    if 'show_registration' not in st.session_state:
        st.session_state.show_registration = False
    
    # Function to toggle between login and registration
    def toggle_registration():
        st.session_state.show_registration = not st.session_state.show_registration
    
    # Remove default Streamlit menu and styling
    hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)
    
    # Simple centered layout
    _, center_col, _ = st.columns([1, 10, 1])
    
    with center_col:
        # Logo - using a custom bread icon that matches the one in the screenshot
        st.markdown("""
        <div style="display: flex; justify-content: center">
            <img src="https://img.icons8.com/fluency/96/bread.png" width="50" alt="bread icon" style="margin-bottom: 0;">
        </div>
        """, unsafe_allow_html=True)
        
        # Welcome title
        st.markdown("<h1>Welcome to the Bread Distribution System</h1>", unsafe_allow_html=True)
        
        # Welcome message
        st.markdown("<p style='text-align: center; margin-bottom: 30px;'>Please login to access the system. Different features are available based on your role.</p>", unsafe_allow_html=True)
        
        # Login or Registration Form
        if not st.session_state.show_registration:
            # Login subtitle
            st.markdown("<h2 style='text-align: left; font-size: 1.2rem; margin-bottom: 15px;'>Login</h2>", unsafe_allow_html=True)
            
            # Username field
            username = st.text_input("Username", key="login_username")
            
            # Password field with eye icon for visibility
            password = st.text_input("Password", type="password", key="login_password")
            
            # Login button
            login_button = st.button("Login", use_container_width=True)
            
            if login_button:
                if authenticate(username, password):
                    st.success(f"Welcome {username}!")
                    st.experimental_rerun()
                else:
                    st.error("Invalid username or password")
            
            # Registration link
            st.markdown("<div style='text-align: center; margin-top: 20px;'>Don't have an account?</div>", unsafe_allow_html=True)
            st.button("Register New Account", key="to_register", on_click=toggle_registration, use_container_width=True)
            
            # Default credentials (collapsed by default)
            with st.expander("Default Credentials & Information", expanded=False):
                st.info("Admin: username = admin, password = admin123")
                st.info("Worker: username = worker, password = worker123")
        
        else:
            # Registration subtitle
            st.markdown("<h2 style='text-align: left; font-size: 1.2rem; margin-bottom: 15px;'>Register New Account</h2>", unsafe_allow_html=True)
            
            # Registration form fields
            new_username = st.text_input("Username", key="reg_username")
            new_password = st.text_input("Password", type="password", key="reg_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
            
            # Default role is worker for new registrations
            new_role = "worker"
            
            # Register button
            register_button = st.button("Register", use_container_width=True)
            
            if register_button:
                # Validate inputs
                if not new_username or not new_password:
                    st.error("Username and password are required")
                elif new_password != confirm_password:
                    st.error("Passwords do not match")
                else:
                    # Check if username exists
                    users = load_users()
                    if any(user["username"] == new_username for user in users):
                        st.error(f"Username '{new_username}' is already taken")
                    else:
                        # Add new user
                        users.append({
                            "username": new_username,
                            "password": new_password,
                            "role": new_role
                        })
                        save_users(users)
                        st.success(f"Account created successfully! You can now log in.")
                        # Switch back to login screen
                        st.session_state.show_registration = False
                        st.experimental_rerun()
            
            # Back to login link
            st.markdown("<div style='text-align: center; margin-top: 20px;'>Already have an account?</div>", unsafe_allow_html=True)
            st.button("Back to Login", key="to_login", on_click=toggle_registration, use_container_width=True)

else:
    # Sidebar with navigation and logout button
    st.sidebar.title(f"Welcome, {st.session_state.username}")
    st.sidebar.caption(f"Role: {st.session_state.user_role.capitalize()}")
    
    # Display navigation based on user role
    pages = []
    if st.session_state.user_role == "admin":
        pages = ["Admin Table", "Worker Table", "Analytics", "User Management"]
    elif st.session_state.user_role == "worker":
        pages = ["Worker Table", "Settle Payments"]
    
    page = st.sidebar.radio("Navigate", pages)
    
    # Logout button
    if st.sidebar.button("Logout", use_container_width=True):
        logout()
        st.experimental_rerun()
    
    # Utility functions for data formatting
    def format_currency(value):
        return f"₹{value:.1f}"

    def format_percentage(value):
        if isinstance(value, str):
            return value
        return f"{value:.2f}%"

    # Function to calculate derived fields
    def calculate_derived_fields(row):
        # Calculate DEL.B.RATE = AW RATE + DIFF1
        row['DEL.B.RATE'] = row['AW RATE'] + row['DIFF1']
        
        # Calculate RETAILOR RATE = DEL.B.RATE + DIFF2
        row['RETAILOR RATE'] = row['DEL.B.RATE'] + row['DIFF2']
        
        # Calculate TOTAL QUA = JALI * JALI QUA
        row['TOTAL QUA'] = row['JALI'] * row['JALI QUA']
        
        return row

    # Apply styling to highlight negative values in red
    def highlight_negative(df):
        # Apply styling to the dataframe
        return df.style.applymap(
            lambda x: 'color: red; font-weight: bold' if isinstance(x, (int, float)) and x < 0 else '',
            subset=['SALE', 'AMOUNT']
        )

    # Content based on the selected page
    if page == "Admin Table":
        st.title("Bread Rate Management")
        
        # Add a button to toggle between table view and form view for mobile
        view_mode = st.radio("View Mode", ["Table View", "Add/Edit Mode"], horizontal=True)
        
        if view_mode == "Table View":
            # Display the admin table directly using basic dataframe
            st.dataframe(
                pd.DataFrame(st.session_state.admin_data),
                use_container_width=True
            )
            
            # Add a button to download the data as CSV
            if st.session_state.admin_data:
                csv = pd.DataFrame(st.session_state.admin_data).to_csv(index=False)
                st.download_button(
                    label="Download as CSV",
                    data=csv,
                    file_name="admin_data.csv",
                    mime="text/csv",
                    use_container_width=True
                )
        else:
            # Add improved form for editing/adding items
            st.subheader("Add or Update Product")
            
            # Add mode selection
            mode = st.radio("Select Mode", ["Add New Product", "Update Existing Product"], horizontal=False)
            
            # Get the next SR.NO
            next_id = len(st.session_state.admin_data) + 1 if st.session_state.admin_data else 1
            
            # Initialize form values
            sku_name = ""
            aw_rate = 0.0
            diff1 = 0.0
            diff2 = 0.0
            jali = 0
            jali_qua = 0
            
            # If updating existing product, show dropdown to select product
            existing_product = None
            if mode == "Update Existing Product":
                # Create dropdown with existing SKU names
                sku_options = [product["SKU NAME"] for product in st.session_state.admin_data]
                selected_sku = st.selectbox("Select Product to Update", sku_options)
                
                # Find the selected product in admin_data
                for product in st.session_state.admin_data:
                    if product["SKU NAME"] == selected_sku:
                        existing_product = product
                        break
                        
                # Pre-fill form with existing values
                if existing_product:
                    sku_name = existing_product["SKU NAME"]
                    aw_rate = existing_product["AW RATE"]
                    diff1 = existing_product["DIFF1"]
                    diff2 = existing_product["DIFF2"]
                    jali = existing_product["JALI"]
                    jali_qua = existing_product["JALI QUA"]
            
            # Form for input fields - use a single column for mobile
            with st.form("admin_form"):
                if mode == "Add New Product":
                    sku_name = st.text_input("SKU NAME", sku_name)
                else:
                    st.text_input("SKU NAME", sku_name, disabled=True)
                    
                aw_rate = st.number_input("AW RATE (₹)", min_value=0.0, step=0.1, format="%.1f", value=aw_rate)
                diff1 = st.number_input("DIFF 1", min_value=0.0, step=0.1, format="%.1f", value=diff1)
                diff2 = st.number_input("DIFF 2", min_value=0.0, step=0.1, format="%.1f", value=diff2)
                jali = st.number_input("JALI (Tray Count)", min_value=0, step=1, value=jali)
                jali_qua = st.number_input("JALI QUA (Units per Tray)", min_value=0, step=1, value=jali_qua)
                
                # Calculate derived values
                del_b_rate = aw_rate + diff1
                retailor_rate = del_b_rate + diff2
                total_qua = jali * jali_qua
                
                # Display calculated fields
                st.write(f"DEL.B.RATE: {format_currency(del_b_rate)}")
                st.write(f"RETAILOR RATE: {format_currency(retailor_rate)}")
                st.write(f"TOTAL QUA: {total_qua}")
                
                # Conditional submit button label based on mode
                submit_label = "Update Product" if mode == "Update Existing Product" else "Add New Product"
                submitted = st.form_submit_button(submit_label, use_container_width=True)
                
                if submitted:
                    if mode == "Add New Product" and not sku_name:
                        st.error("Please enter a SKU NAME")
                    elif mode == "Add New Product":
                        # Add new product
                        new_product = {
                            "SR.NO": next_id,
                            "SKU NAME": sku_name,
                            "AW RATE": aw_rate,
                            "DIFF1": diff1,
                            "DEL.B.RATE": del_b_rate,
                            "DIFF2": diff2,
                            "RETAILOR RATE": retailor_rate,
                            "JALI": jali,
                            "JALI QUA": jali_qua,
                            "TOTAL QUA": total_qua
                        }
                        st.session_state.admin_data.append(new_product)
                        st.success(f"Product '{sku_name}' added successfully!")
                    elif existing_product:
                        # Update existing product
                        for i, product in enumerate(st.session_state.admin_data):
                            if product["SKU NAME"] == sku_name:
                                updated_product = {
                                    "SR.NO": product["SR.NO"],
                                    "SKU NAME": sku_name,
                                    "AW RATE": aw_rate,
                                    "DIFF1": diff1,
                                    "DEL.B.RATE": del_b_rate,
                                    "DIFF2": diff2,
                                    "RETAILOR RATE": retailor_rate,
                                    "JALI": jali,
                                    "JALI QUA": jali_qua,
                                    "TOTAL QUA": total_qua
                                }
                                st.session_state.admin_data[i] = updated_product
                                st.success(f"Product '{sku_name}' updated successfully!")
                                break
                    
                    # Save to database
                    save_admin_data(st.session_state.admin_data)
                    st.experimental_rerun()

    elif page == "Worker Table":
        st.title("Daily Sales Tracking")
        
        # Help text to explain what the fields mean - as an expander to save space on mobile
        with st.expander("Field Explanations"):
            st.markdown("""
            - **SKU NAME**: Product name
            - **SKU**: Initial quantity received
            - **MR**: Market Returns - products returned from market
            - **SALE**: Automatically calculated as (SKU - MR)
            - **AMOUNT**: Revenue from sales (calculated as SALE × RETAILOR RATE)
            - **RCENTA**: Return percentage (calculated as MR/SKU × 100)
            - **ORDER**: Quantity to order for next day
            """)
        
        # Date selection
        selected_date = st.date_input("Select Date", date.today())
        st.session_state.date_filter = str(selected_date)
        
        # Get retail rates from admin data for calculations
        retail_rates = {product["SKU NAME"]: product["RETAILOR RATE"] for product in st.session_state.admin_data}
        
        # Get all SKU names from admin data
        sku_names = [product["SKU NAME"] for product in st.session_state.admin_data]
        
        # Get existing data for this date
        existing_data = [item for item in st.session_state.worker_data 
                        if item.get("DATE") == st.session_state.date_filter]
        
        # Create a dictionary of existing entries with SKU NAME as key
        existing_entries = {item["SKU NAME"]: item for item in existing_data if "SKU NAME" in item}
        
        # Create a list of all worker entries for this date
        worker_entries = []
        
        # Initialize data for all SKUs from admin table
        for sku_name in sku_names:
            if sku_name in existing_entries:
                # Use existing entry for this SKU
                entry = existing_entries[sku_name]
                worker_entries.append(entry)
            else:
                # Create a new entry with zeros
                worker_entries.append({
                    "DATE": st.session_state.date_filter,
                    "SKU NAME": sku_name,
                    "SKU": 0,
                    "MR": 0,
                    "FR": 0,
                    "SALE": 0,
                    "AMOUNT": 0,
                    "RCENTA": 0,
                    "ORDER": 0
                })
        
        # Create DataFrame
        df = pd.DataFrame(worker_entries)
        
        # Create editable table for worker data - with better mobile appearance
        st.subheader("Daily Sales Data")
        st.info("Enter quantities for SKU (initial quantity) and MR (market returns). SALE will be auto-calculated as (SKU - MR).")
        
        # Option to filter by product name for easier mobile navigation
        search_term = st.text_input("Search Product", placeholder="Type to filter products...")
        if search_term:
            df = df[df["SKU NAME"].str.contains(search_term, case=False)]
        
        # Configure columns for the editable table - simplified for mobile
        column_config = {
            "SKU NAME": st.column_config.TextColumn("SKU NAME", disabled=True),
            "SKU": st.column_config.NumberColumn("SKU", min_value=0, step=1, format="%d"),
            "MR": st.column_config.NumberColumn("MR", min_value=0, step=1, format="%d"),
            "FR": st.column_config.NumberColumn("FR", min_value=0, step=1, format="%d", disabled=True),
            "SALE": st.column_config.NumberColumn("SALE", step=1, format="%d", disabled=True),
            "AMOUNT": st.column_config.NumberColumn("AMT (₹)", format="₹%.1f", disabled=True),
            "RCENTA": st.column_config.NumberColumn("RTN %", format="%.1f%%", disabled=True),
            "ORDER": st.column_config.NumberColumn("ORDER", min_value=0, step=1, format="%d"),
        }
        
        # Create the data editor - with options friendly for mobile
        edited_df = st.data_editor(
            df,
            column_config=column_config,
            use_container_width=True,
            hide_index=True,
            num_rows="fixed",
            column_order=["SKU NAME", "SKU", "MR", "SALE", "AMOUNT", "RCENTA", "ORDER"],
            key="worker_editor"
        )
        
        # Button to calculate and save the data
        if st.button("Calculate & Save", use_container_width=True):
            # Create a copy to process and save
            processed_df = edited_df.copy()
            
            # Calculate the derived fields
            for idx, row in processed_df.iterrows():
                # Calculate SALE automatically as SKU - MR
                processed_df.at[idx, "SALE"] = max(0, row["SKU"] - row["MR"])
                
                # Get rate for this SKU
                sku_rate = retail_rates.get(row["SKU NAME"], 0)
                
                # Calculate AMOUNT based on auto-calculated SALE
                processed_df.at[idx, "AMOUNT"] = processed_df.at[idx, "SALE"] * sku_rate
                
                # Calculate RCENTA (return percentage)
                if row["SKU"] > 0:
                    processed_df.at[idx, "RCENTA"] = (row["MR"] / row["SKU"]) * 100
                else:
                    processed_df.at[idx, "RCENTA"] = 0
                    
                # Set FR to 0 as it's no longer used
                processed_df.at[idx, "FR"] = 0
            
            # Update session state and save to database
            # First, remove existing entries for this date
            updated_worker_data = [item for item in st.session_state.worker_data 
                                 if item.get("DATE") != st.session_state.date_filter]
            
            # Add the updated entries
            updated_worker_data.extend(processed_df.to_dict('records'))
            
            # Save to session state and database
            st.session_state.worker_data = updated_worker_data
            save_worker_data(updated_worker_data)
            
            st.success("Data calculated and saved successfully!")
            st.experimental_rerun()
        
        # Display totals in a collapsible section to save space on mobile
        if not df.empty:
            with st.expander("Daily Totals Summary", expanded=True):
                # Calculate totals
                total_sku = df["SKU"].sum()
                total_mr = df["MR"].sum()
                
                # Calculate total sale based on SKU - MR for each row
                total_sale = 0
                total_amount = 0
                
                for idx, row in df.iterrows():
                    sku_name = row["SKU NAME"]
                    sku_value = row["SKU"]
                    mr_value = row["MR"]
                    
                    # Calculate sale for this row
                    sale_value = max(0, sku_value - mr_value)
                    total_sale += sale_value
                    
                    # Calculate amount for this row
                    total_amount += sale_value * retail_rates.get(sku_name, 0)
                
                # Calculate overall return percentage
                overall_rcenta = (total_mr / total_sku * 100) if total_sku > 0 else 0
                
                # Display totals in columns or vertical stack based on screen size
                st.subheader("Daily Totals")
                
                # Use two rows of metrics for better mobile layout
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Total SKU", f"{total_sku}")
                    st.metric("Total Sales", f"{total_sale}")
                with col2:
                    st.metric("Total Returns", f"{total_mr}")
                    st.metric("Return %", format_percentage(overall_rcenta))
                
                # Final metric centered
                st.metric("Total Amount", format_currency(total_amount))
        
        # Add a button to download the data as CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Daily Data as CSV",
            data=csv,
            file_name=f"worker_data_{st.session_state.date_filter}.csv",
            mime="text/csv",
            use_container_width=True
        )

    elif page == "Settle Payments" and st.session_state.user_role == "worker":
        st.title("Settle Payments")
        
        # Date selection for settlement
        selected_date = st.date_input("Select Date for Settlement", date.today())
        selected_date_str = str(selected_date)
        
        # Get all worker data for the selected date
        worker_data = [item for item in st.session_state.worker_data 
                      if item.get("DATE") == selected_date_str]
        
        # Calculate total sales amount for the day
        total_amount = 0
        if worker_data:
            # Convert to DataFrame
            df = pd.DataFrame(worker_data)
            
            # Sum up the AMOUNT column if it exists
            if "AMOUNT" in df.columns:
                total_amount = df["AMOUNT"].sum()
        
        # Format the total amount for display
        formatted_total = format_currency(total_amount)
        
        # Display the total sales amount
        st.subheader("Daily Sales Summary")
        st.metric("Total Sales Amount", formatted_total)
        
        # Check if there's an existing settlement for this date
        payments_data = load_payments_data()
        existing_settlement = None
        for payment in payments_data:
            if (payment.get("date") == selected_date_str and 
                payment.get("worker") == st.session_state.username):
                existing_settlement = payment
                break
        
        # Initialize session state for smart form if not already present
        if 'payment_values' not in st.session_state:
            st.session_state.payment_values = {
                'cash_amount': existing_settlement["cash_amount"] if existing_settlement else 0.0,
                'online_amount': existing_settlement["online_amount"] if existing_settlement else 0.0,
                'adjustment_amount': existing_settlement["adjustment_amount"] if existing_settlement else 0.0,
                'adjustment_note': existing_settlement["adjustment_note"] if existing_settlement else "",
                'editing_mode': False
            }
        
        # When an existing settlement is found and we're not in editing mode, load it
        if existing_settlement and not st.session_state.payment_values['editing_mode']:
            st.session_state.payment_values['cash_amount'] = existing_settlement["cash_amount"]
            st.session_state.payment_values['online_amount'] = existing_settlement["online_amount"]
            st.session_state.payment_values['adjustment_amount'] = existing_settlement["adjustment_amount"]
            st.session_state.payment_values['adjustment_note'] = existing_settlement["adjustment_note"]
        
        def enable_editing():
            st.session_state.payment_values['editing_mode'] = True
            
        def reset_form():
            st.session_state.payment_values['cash_amount'] = 0.0
            st.session_state.payment_values['online_amount'] = 0.0
            st.session_state.payment_values['adjustment_amount'] = 0.0
            st.session_state.payment_values['adjustment_note'] = ""
            st.session_state.payment_values['editing_mode'] = True
        
        # Settlement information status
        if existing_settlement and not st.session_state.payment_values['editing_mode']:
            st.success("A settlement record already exists for this date.")
            
            # Display existing settlement details
            total_settled = existing_settlement["cash_amount"] + existing_settlement["online_amount"] + existing_settlement["adjustment_amount"]
            remaining = existing_settlement["remaining_balance"]
            
            # Status indicators
            settlement_status = "✅ Fully Settled" if abs(remaining) < 0.01 else "⚠️ Partially Settled"
            
            # Show existing settlement in a clean format
            with st.container():
                st.subheader("Current Settlement Details")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Cash Payment", format_currency(existing_settlement["cash_amount"]))
                    st.metric("Online Payment", format_currency(existing_settlement["online_amount"]))
                    
                with col2:
                    st.metric("Adjustment", format_currency(existing_settlement["adjustment_amount"]))
                    st.metric("Status", settlement_status)
                
                if existing_settlement["adjustment_note"]:
                    st.info(f"Adjustment Note: {existing_settlement['adjustment_note']}")
            
            # Edit and Reset buttons
            col1, col2 = st.columns(2)
            with col1:
                st.button("Edit Settlement", on_click=enable_editing, use_container_width=True)
            with col2:
                st.button("Create New Settlement", on_click=reset_form, use_container_width=True)
        
        # Only show the form if we're in editing mode or no settlement exists
        if st.session_state.payment_values['editing_mode'] or not existing_settlement:
            # Outside the form, create inputs for values that will auto-calculate
            # These don't directly control the form inputs but prepare the values for them
            st.subheader("Payment Details")
            st.info(f"Total amount to be settled: {formatted_total}")
            
            # Create columns for the inputs outside the form
            out_col1, out_col2 = st.columns(2)
            
            # Cash input
            with out_col1:
                cash_value = st.number_input(
                    "Cash Payment (₹) - Enter value",
                    min_value=0.0,
                    value=st.session_state.payment_values['cash_amount'],
                    step=1.0,
                    format="%.1f",
                    key="cash_outside"
                )
                
                # Auto-calculate online based on cash
                if cash_value != st.session_state.payment_values['cash_amount']:
                    st.session_state.payment_values['cash_amount'] = cash_value
                    # Update online to fill remainder
                    remainder = total_amount - (cash_value + st.session_state.payment_values['adjustment_amount'])
                    if remainder >= 0:
                        st.session_state.payment_values['online_amount'] = remainder
                    else:
                        st.session_state.payment_values['online_amount'] = 0.0
            
            # Online input    
            with out_col1:
                online_value = st.number_input(
                    "Online Payment (₹) - Enter value",
                    min_value=0.0,
                    value=st.session_state.payment_values['online_amount'],
                    step=1.0,
                    format="%.1f",
                    key="online_outside"
                )
                
                # Auto-calculate cash based on online
                if online_value != st.session_state.payment_values['online_amount']:
                    st.session_state.payment_values['online_amount'] = online_value
                    # Update cash to fill remainder
                    remainder = total_amount - (online_value + st.session_state.payment_values['adjustment_amount'])
                    if remainder >= 0:
                        st.session_state.payment_values['cash_amount'] = remainder
                    else:
                        st.session_state.payment_values['cash_amount'] = 0.0
            
            # Adjustment input
            with out_col2:
                adjustment_value = st.number_input(
                    "Adjustment (₹) - Enter value",
                    value=st.session_state.payment_values['adjustment_amount'],
                    step=1.0,
                    format="%.1f",
                    key="adjustment_outside"
                )
                
                # Update adjustment and recalculate
                if adjustment_value != st.session_state.payment_values['adjustment_amount']:
                    st.session_state.payment_values['adjustment_amount'] = adjustment_value
                    # Update online to fill remainder
                    remainder = total_amount - (st.session_state.payment_values['cash_amount'] + adjustment_value)
                    if remainder >= 0:
                        st.session_state.payment_values['online_amount'] = remainder
                    else:
                        # We've over-adjusted, reset online
                        st.session_state.payment_values['online_amount'] = 0.0
            
            # Adjustment note
            with out_col2:
                adjustment_note = st.text_area(
                    "Adjustment Note",
                    value=st.session_state.payment_values['adjustment_note'],
                    placeholder="Explain any adjustments here...",
                    key="adjustment_note_outside"
                )
                st.session_state.payment_values['adjustment_note'] = adjustment_note
            
            # Auto-balance button outside the form
            if abs(total_amount - (st.session_state.payment_values['cash_amount'] + 
                                  st.session_state.payment_values['online_amount'] + 
                                  st.session_state.payment_values['adjustment_amount'])) > 0.01:
                if st.button("Auto-Balance", use_container_width=True):
                    # Distribute remaining amount
                    remaining = total_amount - (st.session_state.payment_values['cash_amount'] + 
                                               st.session_state.payment_values['adjustment_amount'])
                    if remaining >= 0:
                        st.session_state.payment_values['online_amount'] = remaining
                    else:
                        # We've over-allocated, adjust cash down
                        over_amount = abs(remaining)
                        if st.session_state.payment_values['cash_amount'] >= over_amount:
                            st.session_state.payment_values['cash_amount'] -= over_amount
                        else:
                            st.session_state.payment_values['cash_amount'] = 0.0
                    
                    # Force a rerun to update the UI
                    st.experimental_rerun()
            
            # Calculate total settled and remaining balance
            total_settled = st.session_state.payment_values['cash_amount'] + \
                           st.session_state.payment_values['online_amount'] + \
                           st.session_state.payment_values['adjustment_amount']
            remaining = total_amount - total_settled
            
            # Show summary of current values
            st.subheader("Settlement Summary")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Total Sales", formatted_total)
                st.metric("Total Settled", format_currency(total_settled))
            
            with col2:
                status = "✅ Fully Settled" if abs(remaining) < 0.01 else "⚠️ Partially Settled"
                st.metric("Remaining Balance", format_currency(remaining))
                st.markdown(f"**Status**: {status}")
            
            # Now create a simple form just for the submit button
            with st.form("settlement_form"):
                # Hidden form fields that just copy values from session state
                # These aren't shown to the user but are needed for the form submission
                cash_amount = st.number_input(
                    "Cash Payment (hidden)",
                    value=st.session_state.payment_values['cash_amount'],
                    key="cash_form",
                    label_visibility="collapsed"
                )
                
                online_amount = st.number_input(
                    "Online Payment (hidden)",
                    value=st.session_state.payment_values['online_amount'],
                    key="online_form",
                    label_visibility="collapsed"
                )
                
                adjustment_amount = st.number_input(
                    "Adjustment (hidden)",
                    value=st.session_state.payment_values['adjustment_amount'],
                    key="adjustment_form",
                    label_visibility="collapsed"
                )
                
                # Submit button
                submitted = st.form_submit_button("Save Settlement", use_container_width=True)
                
                if submitted:
                    # Validate the settlement
                    if total_settled < 0:
                        st.error("Total settled amount cannot be negative.")
                    else:
                        # Create or update settlement record
                        settlement = {
                            "date": selected_date_str,
                            "worker": st.session_state.username,
                            "total_amount": total_amount,
                            "cash_amount": st.session_state.payment_values['cash_amount'],
                            "online_amount": st.session_state.payment_values['online_amount'],
                            "adjustment_amount": st.session_state.payment_values['adjustment_amount'],
                            "adjustment_note": st.session_state.payment_values['adjustment_note'],
                            "remaining_balance": remaining,
                            "timestamp": str(pd.Timestamp.now())
                        }
                        
                        # Remove existing settlement for this date if it exists
                        if existing_settlement:
                            payments_data = [p for p in payments_data if not (
                                p.get("date") == selected_date_str and 
                                p.get("worker") == st.session_state.username
                            )]
                        
                        # Add the new settlement
                        payments_data.append(settlement)
                        save_payments_data(payments_data)
                        
                        # Reset editing mode
                        st.session_state.payment_values['editing_mode'] = False
                        
                        st.success("Settlement saved successfully!")
                        st.experimental_rerun()
        
        # Display settlement history
        st.subheader("Settlement History")
        
        # Filter payments for current worker
        worker_payments = [p for p in payments_data if p.get("worker") == st.session_state.username]
        
        if worker_payments:
            # Convert to DataFrame
            payments_df = pd.DataFrame(worker_payments)
            
            # Sort by date (most recent first)
            payments_df["date"] = pd.to_datetime(payments_df["date"])
            payments_df = payments_df.sort_values("date", ascending=False)
            
            # Format for display
            display_df = payments_df.copy()
            display_df["total_amount"] = display_df["total_amount"].apply(format_currency)
            display_df["cash_amount"] = display_df["cash_amount"].apply(format_currency)
            display_df["online_amount"] = display_df["online_amount"].apply(format_currency)
            display_df["adjustment_amount"] = display_df["adjustment_amount"].apply(format_currency)
            display_df["remaining_balance"] = display_df["remaining_balance"].apply(format_currency)
            display_df["date"] = display_df["date"].dt.strftime("%Y-%m-%d")
            
            # Select columns to display
            display_df = display_df[["date", "total_amount", "cash_amount", 
                                   "online_amount", "adjustment_amount", 
                                   "remaining_balance"]]
            
            # Rename columns for clarity
            display_df.columns = ["Date", "Total Sales", "Cash", "Online", 
                                "Adjustment", "Remaining"]
            
            # Display the table
            st.dataframe(display_df, use_container_width=True)
        else:
            st.info("No settlement history found.")

    elif page == "Analytics":
        st.title("Performance Analytics")
        
        # Date range selection - stacked vertically for mobile
        start_date = st.date_input("Start Date", date.today().replace(day=1))
        end_date = st.date_input("End Date", date.today())
        
        # Convert dates to strings for comparison
        start_date_str = str(start_date)
        end_date_str = str(end_date)
        
        # Filter worker data by date range
        filtered_data = [item for item in st.session_state.worker_data 
                         if start_date_str <= item.get("DATE", "") <= end_date_str]
        
        if filtered_data:
            # Create a DataFrame
            df = pd.DataFrame(filtered_data)
            
            # Summary metrics - stacked for mobile
            st.subheader("Summary Metrics")
            
            total_sales = df["SALE"].sum() if "SALE" in df.columns else 0
            total_amount = df["AMOUNT"].sum() if "AMOUNT" in df.columns else 0
            
            # Calculate average return percentage
            total_sku = df["SKU"].sum() if "SKU" in df.columns else 0
            total_returns = df["MR"].sum() + df["FR"].sum() if "MR" in df.columns and "FR" in df.columns else 0
            
            avg_return_percentage = (total_returns / total_sku * 100) if total_sku > 0 else 0
            
            # Display metrics with mobile-friendly layout
            st.metric("Total Sales", f"{total_sales} units")
            st.metric("Total Revenue", format_currency(total_amount))
            st.metric("Avg Return Rate", format_percentage(avg_return_percentage))
            
            # Product-wise performance
            st.subheader("Product Performance")
            
            # Add a search/filter option for mobile
            product_search = st.text_input("Search Product", placeholder="Type to filter products...")
            
            # Group by SKU NAME
            sku_performance = df.groupby("SKU NAME").agg({
                "SKU": "sum",
                "MR": "sum",
                "FR": "sum",
                "SALE": "sum",
                "AMOUNT": "sum"
            }).reset_index()
            
            # Apply filter if search term exists
            if product_search:
                sku_performance = sku_performance[sku_performance["SKU NAME"].str.contains(product_search, case=False)]
            
            # Calculate return percentages
            sku_performance["Return %"] = (
                (sku_performance["MR"] + sku_performance["FR"]) / 
                sku_performance["SKU"] * 100
            ).apply(format_percentage)
            
            # Format currency columns
            sku_performance["AMOUNT"] = sku_performance["AMOUNT"].apply(format_currency)
            
            st.dataframe(sku_performance, use_container_width=True)
            
            # Visualizations in tabs for mobile
            st.subheader("Sales Visualization")
            viz_tabs = st.tabs(["Sales Trend", "Revenue Trend"])
            
            # Group by date for time-series
            if "DATE" in df.columns:
                daily_sales = df.groupby("DATE").agg({
                    "SALE": "sum",
                    "AMOUNT": "sum"
                }).reset_index()
                
                # Convert to proper date format
                daily_sales["DATE"] = pd.to_datetime(daily_sales["DATE"])
                daily_sales = daily_sales.sort_values("DATE")
                
                # Line chart for sales over time
                with viz_tabs[0]:
                    st.subheader("Sales Over Time")
                    st.line_chart(daily_sales.set_index("DATE")["SALE"])
                
                # Line chart for revenue over time
                with viz_tabs[1]:
                    st.subheader("Revenue Over Time")
                    st.line_chart(daily_sales.set_index("DATE")["AMOUNT"])
        else:
            st.info("No data available for the selected date range.")

    elif page == "User Management" and st.session_state.user_role == "admin":
        st.title("User Management")
        
        # Load users
        users = load_users()
        
        # Option to filter users for better mobile navigation
        user_search = st.text_input("Search Users", placeholder="Type to filter users...")
        
        # Filter users if search term exists
        displayed_users = users
        if user_search:
            displayed_users = [user for user in users if user_search.lower() in user["username"].lower()]
        
        # Display current users
        st.subheader("Current Users")
        
        # Create a DataFrame from users list
        users_df = pd.DataFrame(displayed_users)
        
        # Configure columns for display
        column_config = {
            "username": st.column_config.TextColumn("Username"),
            "password": st.column_config.TextColumn("Password", disabled=True),
            "role": st.column_config.SelectboxColumn("Role", options=["admin", "worker"])
        }
        
        # Show users in a table
        st.dataframe(users_df, column_config=column_config, use_container_width=True)
        
        # Forms for adding and managing users - use tabs for space efficiency on mobile
        st.subheader("User Actions")
        
        # Create tabs for add, edit, delete
        tab1, tab2, tab3 = st.tabs(["Add", "Edit", "Delete"])
        
        with tab1:
            # Form to add new user
            with st.form("add_user_form"):
                new_username = st.text_input("Username")
                new_password = st.text_input("Password", type="password")
                new_role = st.selectbox("Role", ["admin", "worker"])
                
                add_submitted = st.form_submit_button("Add User", use_container_width=True)
                
                if add_submitted:
                    if not new_username or not new_password:
                        st.error("Username and password are required.")
                    elif any(user["username"] == new_username for user in users):
                        st.error(f"Username '{new_username}' already exists.")
                    else:
                        # Add new user
                        users.append({
                            "username": new_username,
                            "password": new_password,
                            "role": new_role
                        })
                        save_users(users)
                        st.success(f"User '{new_username}' added successfully!")
                        st.experimental_rerun()
        
        with tab2:
            # Form to edit existing user
            with st.form("edit_user_form"):
                # Get usernames for selection
                usernames = [user["username"] for user in users]
                edit_username = st.selectbox("Select User to Edit", usernames)
                
                # Find the selected user
                selected_user = next((user for user in users if user["username"] == edit_username), None)
                
                # Fields for editing
                if selected_user:
                    edit_password = st.text_input(
                        "New Password (leave blank to keep current)",
                        type="password"
                    )
                    edit_role = st.selectbox("Role", ["admin", "worker"], index=0 if selected_user["role"] == "admin" else 1)
                    
                    edit_submitted = st.form_submit_button("Update User", use_container_width=True)
                    
                    if edit_submitted:
                        # Update user details
                        for user in users:
                            if user["username"] == edit_username:
                                if edit_password:
                                    user["password"] = edit_password
                                user["role"] = edit_role
                                break
                        
                        save_users(users)
                        st.success(f"User '{edit_username}' updated successfully!")
                        
                        # If the current user updated their own role, log them out
                        if edit_username == st.session_state.username and edit_role != st.session_state.user_role:
                            st.warning("You've changed your own role. You'll be logged out.")
                            logout()
                            st.experimental_rerun()
                        else:
                            st.experimental_rerun()
        
        with tab3:
            # Form to delete a user
            with st.form("delete_user_form"):
                # Get usernames for selection
                usernames = [user["username"] for user in users if user["username"] != st.session_state.username]
                if not usernames:
                    st.info("No users available to delete (you cannot delete your own account).")
                    delete_submitted = st.form_submit_button("Delete User", disabled=True, use_container_width=True)
                else:
                    delete_username = st.selectbox("Select User to Delete", usernames)
                    st.warning(f"Are you sure you want to delete user '{delete_username}'? This action cannot be undone.")
                    delete_submitted = st.form_submit_button("Delete User", use_container_width=True)
                    
                    if delete_submitted:
                        # Remove user
                        users = [user for user in users if user["username"] != delete_username]
                        save_users(users)
                        st.success(f"User '{delete_username}' deleted successfully!")
                        st.experimental_rerun()

    # Footer - kept simple and minimal for mobile
    st.markdown("---")
    st.caption("© 2023 Bread Distribution System") 