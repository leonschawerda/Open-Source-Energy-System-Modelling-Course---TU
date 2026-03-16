import simpleCalculator

def test_add():
	values = [1,2,3,4]
	assert simpleCalculator.add(values) == 10
	
def test_substract():
	values = [2,2,2,2]
	assert simpleCalculator.subtract(10, values) == 2
	
def test_multiply():
	values = [2,2,2,2]
	assert simpleCalculator.multiply(values) == 16
	
def test_divide():
	assert simpleCalculator.divide(8, 4) == 2