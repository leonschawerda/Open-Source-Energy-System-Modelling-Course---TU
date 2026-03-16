import simpleCalculator


def test_add():
	assert simpleCalculator.add(2, 4) == 6
	
def test_substract():
	assert simpleCalculator.subtract(6, 4) == 2
	
def test_multiply():
	assert simpleCalculator.multiply(2, 4) == 8
	
def test_divide():
	assert simpleCalculator.divide(8, 4) == 2