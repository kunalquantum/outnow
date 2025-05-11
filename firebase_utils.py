import json
import os
import streamlit as st

# Use local JSON storage instead of Firebase
# This avoids the compatibility issue with Pyrebase4 and requests

# File paths for JSON storage
ADMIN_DATA_PATH = "admin_data.json"
WORKER_DATA_PATH = "worker_data.json"

def save_to_json(data, filename):
    """Save data to a local JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        st.error(f"Local save error: {e}")
        return False

def load_from_json(filename):
    """Load data from a local JSON file"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return []
    except Exception as e:
        st.error(f"Local load error: {e}")
        return []

# Functions to save and load admin data
def save_admin_data(data):
    """Save admin data to JSON file"""
    with open(ADMIN_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def load_admin_data():
    """Load admin data from JSON file"""
    if os.path.exists(ADMIN_DATA_PATH):
        with open(ADMIN_DATA_PATH, "r") as f:
            return json.load(f)
    return []

# Functions to save and load worker data
def save_worker_data(data):
    """Save worker data to JSON file"""
    with open(WORKER_DATA_PATH, "w") as f:
        json.dump(data, f, indent=4)

def load_worker_data():
    """Load worker data from JSON file"""
    if os.path.exists(WORKER_DATA_PATH):
        with open(WORKER_DATA_PATH, "r") as f:
            return json.load(f)
    return [] 