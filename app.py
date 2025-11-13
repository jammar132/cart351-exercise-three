import os
import importlib.util

# Path to exercise-three.py (name stays EXACTLY as-is)
BASE_DIR = os.path.dirname(__file__)
EX3_PATH = os.path.join(BASE_DIR, "exercise-three.py")

# Dynamically load exercise-three.py as module "ex3"
spec = importlib.util.spec_from_file_location("ex3", EX3_PATH)
ex3 = importlib.module_from_spec(spec)
spec.loader.exec_module(ex3)

# Get the Flask app defined in exercise-three.py
app = ex3.app