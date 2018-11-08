import NetworkEntity

class NetworkLink(NetworkEntity):
    """
    Class representing a network link, which is absically an internet connection between a router or a storage entity.
    """

    def getNetworkEntities():
        """
        Returns the network entities on both sides of the link.
        @type: (NetworkEntity, NetworkEntity)
        """
        pass

    def getBandwidth():
        """
        Returns the bandwidth of this link.
        """
        pass

    def getThroughput():
        """
        Returns get throughput of this link.
        """
        pass