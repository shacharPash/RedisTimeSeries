import os
import sys
from RLTest import Defaults

if sys.version_info > (3, 0):
    Defaults.decode_responses = True

try:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../deps/readies"))
    import paella
except:
    pass

RLEC_CLUSTER = os.getenv('RLEC_CLUSTER') == '1'
