
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# cwd = os.getcwd()
# print(cwd)
# print(BASE_DIR)
dirname, filename = os.path.split(os.path.abspath(__file__))
print(dirname)
# model = os.path.join(BASE_DIR, "/CMPRS/model/haarcascade_frontalface_alt.xml")
# print(model)
