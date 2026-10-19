
import json

with open("vl-3b.json") as f:
    config = json.load(f)

print(config["hidden_size"])
print(config["num_attention_heads"])
hidden_layers = (config["num_hidden_layers"])
kv_heads = (config["num_key_value_heads"])


d_head = (config["hidden_size"])/(config["num_attention_heads"])

kv_bytes = 2 * d_head * kv_heads * hidden_layers * 2
print(kv_bytes)