class Dataset:
    """
    Class representing a dataset.
    """

    def __init__(self, id, size):
        self.id = id
        self.size = size

    def getId(self):
        """
        The id of the dataset that will be used to locate it in caches.
        @type: int
        """
        return self.id

    def getSize(self):
        """
        Get the size in bytes of the dataset.
        @type: int
        """
        return self.size