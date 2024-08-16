# detect the Python version at runtime
import sys; 
print(sys.version+'\n')

"""
Check the Python site-packages folder location used.
"""

import pydantic_core as _; 
print(_.__path__)
