class StorageController:
    """
    Class representing the storage controller.
    """

    def __init__(self):
        self.storageSpaces = {}

    def estimateDataTransfer(self, dataset):
        """
        Estimate for each storage space, how much time it would take to move this dataset to it.
        @param dataset: Dataset
        """
        # First find the dataset.
        # Then for each storage space, find how much time it would talk to move the dataset from its current position to it.
        # Return restult in a map
        pass 

    def doDataTransfer(self, dataset, origin, destination):
        """
        Do a datatransfer, and update the index accordingly.
        @param dataset: Dataset
        @param origin: Storage
        @param destination: Storage
        """
        pass

    def registerStorageSpace(self, storageSpace):
        """
        Register a storage space to the controller.
        @param storageSpace: Storage
        """
        self.storageSpaces[storageSpace.getId()] = storageSpace


    def unregisterStorageSpace(self, storageSpace):
        """
        Unregister a storage space from the controller.
        @param storageSpace: Storage
        """
        del self.storageSpaces[storageSpace]