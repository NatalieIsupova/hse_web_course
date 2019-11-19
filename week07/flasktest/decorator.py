def increment(fn):
	def new_fn():
		return fn() + 1
	return new_fn

@increment
def hello():
	return 1

print(hello())