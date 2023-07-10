import requests
import sys
import shutil
from tqdm.auto import tqdm
import os

base_dir = "./models/open_llama"
urls = [
    "https://huggingface.co/openlm-research/open_llama_7b_v2/resolve/main/pytorch_model-00001-of-00002.bin",
    "https://huggingface.co/openlm-research/open_llama_7b_v2/resolve/main/pytorch_model-00002-of-00002.bin",
    "https://huggingface.co/openlm-research/open_llama_7b_v2/resolve/main/tokenizer.model",
]

urls = [u for u in urls if not os.path.isfile(f"{base_dir}/{os.path.basename(u)}")]

if len(urls) == 0:
    print("Models downloaded")
    sys.exit(0)


print("Downloading model files..")
# Create dir if does not exist
os.makedirs(base_dir, exist_ok=True)

for url in urls:
    print(f"Downloading from: {url}\n")
    # make an HTTP request within a context manager
    with requests.get(url, stream=True) as r:
        # check header to get content length, in bytes
        total_length = int(r.headers.get("Content-Length") or 0)

        # implement progress bar via tqdm
        with tqdm.wrapattr(r.raw, "read", total=total_length, desc="") as raw:
            # save the output to a file
            with open(f"{base_dir}/{os.path.basename(url)}", "wb") as output:
                shutil.copyfileobj(raw, output)
print("Done")
