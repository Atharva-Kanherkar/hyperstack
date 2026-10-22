from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-VL-3B-Instruct")
msgs = [{"role": "user", "content": "What is the total on this receipt?"}]
text = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
print(text)
print(len(tok(text).input_ids), "tokens after template;",
      len(tok("What is the total on this receipt?").input_ids), "without")



from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained()