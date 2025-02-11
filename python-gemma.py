import keras_nlp

# Load model and generate text
gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma_2b_en")
gemma_lm.generate("It was a dark and stormy night.", max_length=64)