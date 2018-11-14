from batsim.batsim import BatsimScheduler, Batsim, Job
from StorageController import StorageController
from Storage import Storage
from Dataset import Dataset
import sys
import os
import logging
from procset import ProcSet

class StorageScheduler(BatsimScheduler):

    def myprint(self,msg):
        print("[{time}] {msg}".format(time=self.bs.time(), msg=msg))

    def __init__(self, options):
        self.options = options

    def onSimulationBegins(self):
        self.bs.logger.setLevel(logging.ERROR)
        self.storageController = StorageController(self.bs)

        for machine in self.bs.machines["storage"]:
            storageId = machine["id"]
            storageName = machine["name"]
            storageSize = int(machine["properties"]["size_in_byte"])
            storage = Storage(storageId, storageName, storageSize)
            self.storageController.registerStorageSpace(storage)

        self.bs.wake_me_up_at(1000)

    def onJobSubmission(self, job):
        pass

    def onJobCompletion(self, job):
        self.myprint("Job " + job.id + " completed successfully.")

    def onNoMoreEvents(self):
        pass

    def onRequestedCall(self):
        # List of storage we will work with
        mainStorage = self.storageController.getStorageSpace(13)
        qBox1Storage = self.storageController.getStorageSpace(14)

        # Creating and storing a dataset as initialization
        dataset = Dataset(1, 1024*1024*1024*10) # 1GB
        mainStorage.storeDataset(dataset)

        # Moving the dataset and notify on finish
        self.storageController.doDataTransfer(dataset, mainStorage, [qBox1Storage])
        self.bs.notify_submission_finished()
