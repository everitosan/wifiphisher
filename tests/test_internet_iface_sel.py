import sys
import os
import unittest
import dbus
import pdb
import pyric.pyw as pyw

dir_of_executable = os.path.dirname(__file__)
path_to_project_root = os.path.abspath(os.path.join(dir_of_executable, '..'))
sys.path.insert(0, path_to_project_root)
os.chdir(path_to_project_root)

import wifiphisher.common.interfaces as interfaces
import wifiphisher.common.constants as constants
import wifiphisher.pywifiphisher as pywifiphisher

class TestInternetIfaceSelection(unittest.TestCase):

    def setUp(self):
        bus = dbus.SystemBus()
        nm_proxy = bus.get_object(constants.NM_APP_PATH, constants.NM_MANAGER_OBJ_PATH)
        nm = dbus.Interface(nm_proxy, dbus_interface=constants.NM_MANAGER_INTERFACE_PATH)
        devs = nm.GetDevices()
        self.internet_iface = ""
        self.other_ifaces = []

        for dev_obj_path in devs:
            dev_proxy = bus.get_object(constants.NM_APP_PATH, dev_obj_path)
            dev = dbus.Interface(dev_proxy, dbus_interface=dbus.PROPERTIES_IFACE)
            state = dev.Get(constants.NM_DEV_INTERFACE_PATH, 'State')
            iface_name = dev.Get(constants.NM_DEV_INTERFACE_PATH, 'Interface')
            #check connected device
            if state == 100:
                self.internet_iface = str(iface_name)
            elif pyw.iswireless(str(iface_name)):
                self.other_ifaces.append(str(iface_name))

    def sel_ap_iface(self, ap_iface_name):
        self.nm.set_ap_iface(ap_iface_name)
        self.nm.check_ifaces_uncontrolled_by_nm()

    def sel_jamming_and_ap_ifaces(self, ap_if_name, jam_if_name):
        self.nm.set_jam_iface(jam_if_name)
        self.nm.set_ap_iface(ap_if_name)
        self.nm.check_ifaces_uncontrolled_by_nm()
        
    def test_no_jamming_with_internet(self):
        """
        Test with -nJ case with internet connection
        """
        if not self.internet_iface:
            self.fail('Make sure to have internet access')
        self.nm = interfaces.NetworkManager()
        self.nm.set_internet_iface(self.internet_iface)
        ap_iface = self.nm.get_ap_iface()
        self.sel_ap_iface(ap_iface.get_name())

    def test_using_internet_iface_as_ap_iface(self):
        """
        Test with -nJ case and use internet iface as AP iface
        should raise InterfaceManagedByNetworkManagerError exception
        """
        if not self.internet_iface:
            self.fail('Make sure to have internet access')
        self.nm = interfaces.NetworkManager()
        self.nm.set_internet_iface(self.internet_iface)
        self.assertRaises(interfaces.InterfaceManagedByNetworkManagerError,
                self.sel_ap_iface, self.internet_iface)

    def test_jamming_with_internet_access(self):
        """
        Test three interfaces ap/deauth/internet iface
        """
        if not self.internet_iface:
            self.fail('Make sure to have internet access')
        if len(self.other_ifaces) < 2:
            self.fail('Number of adapters are not enough')
        self.nm = interfaces.NetworkManager()
        self.nm.set_internet_iface(self.internet_iface)
        mon_iface, ap_iface = self.nm.find_interface_automatically()
        self.sel_jamming_and_ap_ifaces(ap_iface.get_name(), mon_iface.get_name())

    def test_wo_internet_access(self):
        """
        Test without internet access
        """
        if len(self.other_ifaces) < 2:
            self.fail('Number of adapters are not enough')
        self.nm = interfaces.NetworkManager()
        self.nm.set_internet_iface(self.internet_iface)
        mon_iface, ap_iface = self.nm.find_interface_automatically()
        self.nm.set_jam_iface(mon_iface.get_name())
        self.nm.set_ap_iface(ap_iface.get_name())
        pywifiphisher.kill_interfering_procs()

if __name__ == '__main__':
    unittest.main()
