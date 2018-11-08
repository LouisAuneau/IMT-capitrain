from Storage import Storage
from procset import ProcSet
from batsim.batsim import Job

class StorageController:
    """
    Class representing the storage controller.
    """

    def __init__(self, batsim):
        self.storageSpaces = {}
        self.batsim = batsim
        self.dataTransfersCount = 0
        
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
        if not origin.isDatasetPresent(dataset):
            raise "Dataset " + dataset.getId() + " not found on " + origin.getId() + "."

        # Batsim profile definition and execution
        profile_name = "data_transfer"
        transfer_profile = {
            profile_name : 
            {
                'type' : 'data_staging', 
                'nb_bytes' : dataset.getSize(), 
                'from' : origin.getName(), 
                'to' : destination.getName()
            },
        }
        self.batsim.submit_profiles("dyn", transfer_profile)

        # Batsim job initialization and execution
        jobId = "dyn!" + str(self.dataTransfersCount)
        self.batsim.submit_job(id=jobId, res=1, walltime=-1, profile_name=profile_name)
        job = Job(jobId, 0, -1, 1, "", "", "")
        job.allocation = ProcSet(origin.getId())
        job.storage_mapping = {}
        job.storage_mapping[origin.getName()] = origin.getId()
        job.storage_mapping[destination.getName()] = destination.getId()
        self.batsim.execute_jobs([job])

        # Doing the datatransfert in our abstraction
        origin.removeDataset(dataset)
        destination.storeDataset(dataset)
        self.dataTransfersCount += 1

    def registerStorageSpace(self, storageSpace):
        """
        Register a storage space to the controller.
        @param storageSpace: Storage
        """
        self.storageSpaces[storageSpace.getId()] = storageSpace

    def getStorageSpace(self, id):
        """
        Get one particular storage space registered into the controller. Mainly used for intialization to set data in main storage.
        @param id int Id of the storage space to find
        @return Storage
        @raise Error in case the storage space is not found.
        """
        if id in self.storageSpaces:
            return self.storageSpaces[id]
        else:
            raise "Storage " + id + " not found in the controller."

    def unregisterStorageSpace(self, storageSpace):
        """
        Unregister a storage space from the controller.
        @param storageSpace: Storage
        """
        del self.storageSpaces[storageSpace]