import os
import sys

if not os.path.isfile("./models/open_llama/ggml-model-f16.bin"):
    os.execl(sys.executable, 'python', "./convert.py", "./models/open_llama", *sys.argv[2:])
