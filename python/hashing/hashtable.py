""" Implement a hash table using lists in python. """

class HashTable(object):
	def __init__(self, size):
		self.size = size
		self.table = [None] * self.size

	def hash(self, key):
		return hash(key) % self.size

	def __setitem__(self, key, val):
		""" Uses open addressing to resolve collisions. """
		idx = self.hash(key)
		if self.table[idx] == None:
			self.table[idx] = [(key, val)]
		else:
			for i in range(len(self.table[idx])):
				if self.table[idx][i][0] == key:
					self.table[idx][i] = (key, val) # Update existing key
					return
			# Otherwise, add new keyval pair at this location.
			self.table[idx].append((key, val))

	def __getitem__(self, key):
		idx = self.hash(key)
		if self.table[idx] == None:
			return None
		else:
			if type(self.table[idx]) == list:
				for pair in self.table[idx]:
					if pair[0] == key:
						return pair[1]
				return None
			else:
				return self.table[idx][1]

	def __contains__(self, key):
		if self.__getitem__(key) == None:
			return False
		else:
			return True

if __name__ == '__main__':
	ht = HashTable(256)
	ht['milo'] = 69
	ht['milo'] = 32 # should overwrite previous key

	ht['algorithms'] = 348734987
	print(ht['milo'])
	print(ht['algorithms'])
	print(ht['unknown'])

	ht['none'] = None
	ht['string'] = 'some string'
	print(ht['none'])
	print(ht['string'])

	print('milo' in ht)
	print('asd;lkfjsdfl' in ht)