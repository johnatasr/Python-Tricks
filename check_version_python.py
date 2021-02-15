import sys

if not sys.version_info > (2, 7):
    # raises a advertence about the oldest python version
elif not sys.version_info >= (3, 5):
   # Show a message to python's version to be higher than 3.5
