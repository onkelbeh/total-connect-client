"""Test total_connect_client location."""

import unittest

import TotalConnectClient

LOCATION_INFO_BASIC_NORMAL = {
    "LocationID": "123456",
    "LocationName": "Home",
    "SecurityDeviceID": "987654",
}

PARTITION_DISARMED = {
    "PartitionID": "1",
    "ArmingState": TotalConnectClient.TotalConnectLocation.DISARMED,
}

PARTITION_INFO_DISARMED = {}
PARTITION_INFO_DISARMED[0] = PARTITION_DISARMED

PARTITIONS = {"PartitionInfo": PARTITION_INFO_DISARMED}

ZONE_NORMAL = {
    "ZoneID": "1",
    "ZoneDescription": "Normal",
    "ZoneStatus": TotalConnectClient.ZONE_STATUS_NORMAL,
    "PartitionId": "1",
}

ZONE_INFO = {}
ZONE_INFO[0] = ZONE_NORMAL
ZONES = {"ZoneInfo": ZONE_INFO}

METADATA_NORMAL = {
    "Partitions": PARTITIONS,
    "Zones": ZONES,
    "PromptForImportSecuritySettings": False,
    "LastUpdatedTimestampTicks": 637161937050000000,
    "ConfigurationSequenceNumber": 1,
    "IsInACLoss": False,
    "IsCoverTampered": False,
    "Bell1SupervisionFailure": False,
    "Bell2SupervisionFailure": False,
    "IsInLowBattery": False,
}


class TestTotalConnectLocation(unittest.TestCase):
    """Test TotalConnectLocation."""

    def setUp(self):
        """Set up for location testing."""
        self.auto_bypass_low_battery = False
        self.location_normal = TotalConnectClient.TotalConnectLocation(
            LOCATION_INFO_BASIC_NORMAL, self
        )
        """having trouble setting up test structure for METADATA_NORMAL"""
        #        self.location_normal.set_status(METADATA_NORMAL)

    def tearDown(self):
        """Tear down."""
        self.location_normal = None

    def tests_basic(self):
        """Test basic attributes were set properly."""
        self.assertTrue(
            self.location_normal.location_id == LOCATION_INFO_BASIC_NORMAL["LocationID"]
        )
        self.assertTrue(
            self.location_normal.location_name
            == LOCATION_INFO_BASIC_NORMAL["LocationName"]
        )
        self.assertTrue(
            self.location_normal.security_device_id
            == LOCATION_INFO_BASIC_NORMAL["SecurityDeviceID"]
        )

    def tests_panel(self):
        """Test panel attributes."""
        self.assertFalse(self.location_normal.is_low_battery())
        self.assertFalse(self.location_normal.is_ac_loss())
        self.assertFalse(self.location_normal.is_cover_tampered())

    def tests_status(self):
        """Normal zone."""
        self.assertFalse(self.location_normal.is_arming())
        self.assertFalse(self.location_normal.is_disarming())
        #        self.assertTrue(self.location_normal.is_disarmed())
        self.assertFalse(self.location_normal.is_armed_away())
        self.assertFalse(self.location_normal.is_armed_custom_bypass())
        self.assertFalse(self.location_normal.is_armed_home())
        self.assertFalse(self.location_normal.is_armed_night())
        self.assertFalse(self.location_normal.is_armed())
        self.assertFalse(self.location_normal.is_triggered_police())
        self.assertFalse(self.location_normal.is_triggered_fire())
        self.assertFalse(self.location_normal.is_triggered_gas())
        self.assertFalse(self.location_normal.is_triggered())