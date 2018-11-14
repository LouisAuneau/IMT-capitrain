from NetworkEntity import NetworkEntity
from DatasetContainer import DatasetContainer

class Storage(NetworkEntity):
    """
    Class representing a storage unit.
    """ 

    def __init__(self, id, name, space):
        self.id = id
        self.name = name #name is used by batsim for jobs
        self.space = space
        self.store = {} #a map of DatasetContainer by dataset id

    def getId(self):
        """
        Get this storage space id
        @type: int
        """
        return self.id

    def getName(self):
        """
        Get the name of the storage space.
        @type: string
        """
        return self.name

    def getStore(self):
        """
        Get the store of dataset containers indexed by dataset id.
        @type: dictionary
        """
        return self.store

    def getAvailableSpace(self):
        """
        Get remaining space of this storage space in bytes.
        @return int
        """
        availableSpace = self.getTotalSpace()
        
        for datasetId in self.store:
            availableSpace -= self.store[datasetId].getDataset().getSize()

        return availableSpace

    def getTotalSpace(self):
        """
        Get total space of this storage space in bytes.
        @return int
        """
        return self.space

    def storeDataset(self, dataset):
        """
        Add a dataset into the store.
        @param dataset: Dataset to add.
        """
        if dataset.getSize() <= self.getAvailableSpace():
            self.store[dataset.getId()] = DatasetContainer(dataset)
        else:
            raise "Unable to add " + dataset.getId() + " dataset due to unsuficient space in the storage " + self.getId() + "."

    def removeDataset(self, dataset):
        """
        Remove a dataset from the store.
        @param dataset: Dataset to remove.
        """
        del self.store[dataset.getId()]

    def isDatasetPresent(self, dataset):
        """
        Tell if a dataset is present in the store of this storage space.
        @return Boolean
        """
        return (dataset.getId() in self.store)
            
