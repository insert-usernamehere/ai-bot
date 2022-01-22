from aitextgen import aitextgen
import sys

s = sys.argv[1:]

prompt1 = "" 
for ele in s: 
    prompt1 += ele

ai = aitextgen(model_folder="trained_model", tokenizer_file="aitextgen.tokenizer.json")

ai.generate(n=1, prompt=prompt1, max_length=500)
