import time

class DatasetContainer:
    """
    Contains monitoring information for a dataset + the dataset.
    """

    def __init__(self, dataset):
        self.dataset = dataset
        self.creationTime = time.time()

    def getDataset(self):
        """
        Return the contained dataset.
        @return: int
        """
        return self.dataset

    def getCreationTime(self):
        """
        Get the container creation time.
        @return: float
        """
        return self.creationTime
