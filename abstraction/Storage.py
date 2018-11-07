class Storage(NetworkEntity):
    """
    Class representing a storage unit.
    """ 

    def __init__(self, id, space):
        self.id = id
        self.space = space
        self.cache = {}

    def getId(self):
        """
        Get this storage space id
        @type: int
        """
        return self.id

    def getAvailableSpace(self):
        """
        Get remaining space of this storage space in bytes.
        @return int
        """
        availableSpace = self.getTotalSpace
        
        for datasetId in self.cache:
            availableSpace -= self.cache[datasetId].getSize()

        return availableSpace

    def getTotalSpace(self):
        """
        Get total space of this storage space in bytes.
        @return int
        """
        return self.space

    def storeDataset(self, dataset):
        """
        Add a dataset into the cache.
        @param dataset: Dataset to add.
        @return Boolean
        """
        if dataset.getSize() <= self.getAvailableSpace():
            self.cache[dataset.getId()] = dataset
            return True
        else:
            return False

    def removeDataset(self, dataset):
        """
        Remove a dataset from the cache.
        @param dataset: Dataset to remove.
        """
        del self.cache[dataset.getId()]

    def isDatasetPresent(self, dataset):
        """
        Tell if a dataset is present in the cache of this storage space.
        @return Boolean
        """
        return (dataset.getId() in self.cache)
            
