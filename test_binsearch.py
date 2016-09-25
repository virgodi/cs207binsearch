from pytest import raises
from binsearch import binary_search

def test_simple_BS():
	myInput = list(range(20))
	assert binary_search(myInput,10) == 10
