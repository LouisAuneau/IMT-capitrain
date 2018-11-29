from batsim.batsim import BatsimScheduler, Batsim, Job
from StorageController import StorageController
from Storage import Storage
from Dataset import Dataset
import sys
import os
import logging
import json
from procset import ProcSet

 # Static properties helping data size handling in bytes.
ONE_KILO_BYTE = 1024
ONE_MEGA_BYTE = 1024 * ONE_KILO_BYTE
ONE_GIGA_BYTE = 1024 * ONE_MEGA_BYTE
ONE_TERA_BYTE = 1024 * ONE_GIGA_BYTE


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

    def onSimulationEnds(self):
        # Exporting the load from machines into a csv
        with open('imt_storages_load.json', 'w') as fp:
            json.dump(self.storageController.exportLoadLog(), fp)

        return super()

    def onJobSubmission(self, job):
        pass

    def onJobCompletion(self, job):
        self.storageController.logLoad(job.id, self.bs.time())

    def onNoMoreEvents(self):
        pass

    def onRequestedCall(self):
        # List of storage we will work with
        mainStorage = self.storageController.getStorageSpace(14)
        qBox1Storage = self.storageController.getStorageSpace(13)
        qBox2Storage = self.storageController.getStorageSpace(12)

        # Creating and storing a dataset as initialization
        dataset1 = Dataset(1, ONE_GIGA_BYTE)
        dataset2 = Dataset(2, ONE_GIGA_BYTE*10)
        dataset3 = Dataset(3, ONE_GIGA_BYTE*30)
        dataset4 = Dataset(4, ONE_GIGA_BYTE*30)
        dataset5 = Dataset(5, ONE_GIGA_BYTE*30)
        dataset6 = Dataset(6, ONE_GIGA_BYTE*30)
        dataset7 = Dataset(7, ONE_GIGA_BYTE*30)
        dataset8 = Dataset(8, ONE_GIGA_BYTE*30)
        mainStorage.storeDataset(dataset1)
        mainStorage.storeDataset(dataset2)
        mainStorage.storeDataset(dataset3)
        mainStorage.storeDataset(dataset4)
        mainStorage.storeDataset(dataset5)
        mainStorage.storeDataset(dataset6)
        mainStorage.storeDataset(dataset7)
        mainStorage.storeDataset(dataset8)

        # Moving the dataset and notify on finish
        self.storageController.doDataTransfer(dataset1, mainStorage, [qBox1Storage])

        self.storageController.doDataTransfer(dataset2, mainStorage, [qBox2Storage])

        self.storageController.doDataTransfer(dataset3, mainStorage, [qBox2Storage])

        self.storageController.doDataTransfer(dataset4, mainStorage, [qBox2Storage])

        self.storageController.doDataTransfer(dataset5, mainStorage, [qBox2Storage])

        self.storageController.doDataTransfer(dataset6, mainStorage, [qBox2Storage])

        self.storageController.doDataTransfer(dataset7, mainStorage, [qBox2Storage])

        self.storageController.doDataTransfer(dataset6, mainStorage, [qBox1Storage])

        self.storageController.doDataTransfer(dataset7, mainStorage, [qBox1Storage])

        self.bs.notify_submission_finished()
