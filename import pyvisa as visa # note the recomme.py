import pyvisa as visa # note the recommended way to import pyvisa changed as there is an unrelated visa module
import numpy as np
rm = visa.ResourceManager()
print(rm.list_resources())