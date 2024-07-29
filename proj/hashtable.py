from collections.abc import MutableMapping


class Hashtable(MutableMapping):
    """A class to represent a Hash table"""

    # polynomial constant, used for _hash
    P_CONSTANT = 37

    def __init__(self, capacity, default_value, load_factor, growth_factor):
        """Creates a Hashtable object."""
        # Check to ensure that load_factor is a floating point number that is greater than 0 and less than 1
        if (
            (load_factor <= 0)
            or (load_factor > 1)
            or (isinstance(load_factor, float) == False)
        ):
            raise Exception(
                "load_factor must be greater than 0 and less than or equal to 1."
            )

        # Check to ensure that load_factor is a floating point number that is greater than 0 and less than 1
        if growth_factor <= 1 or isinstance(growth_factor, int) == False:
            raise Exception("growth_factor must be an integer value greater than 1.")

        # Store the capacity, default value, load_factor, and growth_factor as attributes
        self.capacity = capacity
        self.default_value = default_value
        self.load_factor = load_factor
        self.growth_factor = growth_factor
        # create attribute validitems_count that will keep a count of the number of valid items that are added to the hashtable
        self.validitems_count = 0

        # Update self._items with length established by the capacity and comprised of default values
        self._items = [None] * capacity

    def _hash(self, key):
        """
        This method takes in a string and returns an integer value
        between 0 and self.capacity.

        This particular hash function uses Horner's rule to compute a large polynomial.

        See https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect10-hash-basics.pdf
        """
        val = 0
        for letter in key:
            val = self.P_CONSTANT * val + ord(letter)
        return val % self.capacity

    def __setitem__(self, key, val):
        """Receives a key and value and creates a key-value pair in the hashtable"""
        # Get the hash value for the key, which will align with the index value where the value should be stored. That said, save the hash value to a variable called index
        index = self._linear_probe(key)

        # Increase self.validitems_count by 1 if the value is currently None (i.e. this is a new entry)
        if self._items[index] == None:
            self.validitems_count += 1

        # Use the index to assign the value
        self._items[index] = (key, val, True)

        # Check if current load exceeds load factor
        current_load = len(self) / self.capacity
        if current_load > self.load_factor:
            self._resize()

    def _linear_probe(self, key):
        """Identifies the index that should be used with the provided key"""
        index = self._hash(key)
        for i in range(self.capacity):

            # If the value at the index is None, then we have an open splot available for the key. Return that index.
            if self._items[index] == None:
                return index

            # If the item is not None and the key matches at the index provided and the item is a valid item, then return the index
            elif self._items[index][0] == key and self._items[index][2] == True:
                return index
            else:

                # If the above two conditions are not met, update the index
                index = (index + 1) % self.capacity

    def _resize(self):
        """Resizes the Hashtable based on its assigned growth factor and updates its capacity. This process includes re-indexing existing valid key-value pairs and removing invalid key-value pairs."""
        # Create a new Hashtable called new_hash
        new_hash = Hashtable(
            default_value=self.default_value,
            capacity=self.capacity * self.growth_factor,
            load_factor=self.load_factor,
            growth_factor=self.growth_factor,
        )

        # Iterate over the items in self, add them to new_hash
        for item in self:
            new_hash[item[0]] = item[1]

        # Update self to now be new_hash
        self._items = new_hash._items

        # delete new_hash
        del new_hash

        # Update self._capacity
        self.capacity = self.capacity * self.growth_factor

    def __getitem__(self, key):
        """Returns the value associated with the key provided. In the case when the key is not found, the function will return the default value that was provided when the Hashtable was constructed."""

        # Get index --- note that the linear probe only returns items that are valid or that are None. It will not return an index for an item that is invalid (deleted).
        index = self._linear_probe(key)

        # Check whether item at that index is a tuple. If so, return the item.
        if isinstance(self._items[index], tuple):
            return self._items[index][1]
        # Otherwise, return the default value
        else:
            return self.default_value

    def __delitem__(self, key):
        """Deletes the item at the key provided. In this case, deletion means setting the third item in the tuple (indicating whether the item is valid) to be False"""
        # Get index --- note that the linear probe only returns items that are valid or that are None. It will not return an index for an item that is invalid (deleted).
        index = self._linear_probe(key)

        # Check whether the item is a tuple. If so, assign the item a new tuple that has the same key and value; however, the third item indicating whether the item is valid will be set to False.
        if isinstance(self._items[index], tuple):
            value = self._items[index][1]
            self._items[index] = (key, value, False)
            self.validitems_count -= 1

        # If the index returns None, indicate that the user that the key was not found
        else:
            raise KeyError("Key not found")

    def __len__(self):
        """Returns the number of objects in the Hashtable that are valid key-value pairs"""

        # Use a generator to sum all the valid elements. Note that self is an iterator that will only return valid items
        return self.validitems_count

    def __iter__(self):
        """Returns an iterator object that allows the user to traverse over the valid items in the Hashtable"""

        for item in self._items:
            if isinstance(item, tuple) and item[2] == True:
                yield item


if __name__ == "__main__":
    pass