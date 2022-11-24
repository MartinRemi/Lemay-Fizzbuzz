from transformers import pipeline, set_seed

class MLModel:
	def __init__(self, seed=42):
		self.generator = pipeline('text-generation', model='gpt2')
		set_seed(seed)

	def predict(self, input_sentence, max_length = 30, num_return_sequences = 5):
		return self.generator(input_sentence)

if __name__ == "__main__":

	model = MLModel()
	print(model.predict("Hello, my name is Remi"))
