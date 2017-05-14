import sys
import os
import unittest
import mock

dir_of_executable = os.path.dirname(__file__)
path_to_project_root = os.path.abspath(os.path.join(dir_of_executable, '..'))
sys.path.insert(0, path_to_project_root)
os.chdir(path_to_project_root)

import wifiphisher.common.interfaces as interfaces

def is_managed_with_correct_setting(iface):
    """
    Test with the unmanaged-property is correctly set for AP and Deauth interfaces
    """
    return False

def is_managed_with_incorrect_setting(iface_obj):
    """
    Test with the un-managed property is not correctly set for AP
    """
    if iface_obj._support_ap_mode:
        return True
    else:
        return False

def fake_check_iface_managed_by_nm(nm, check_managed_func):
    for iface, iface_obj in nm._interfaces.iteritems():
        if iface == nm.jam_iface or iface == nm.ap_iface:
            if check_managed_func(nm.interfaces[iface]):
                raise interfaces.InterfaceManagedByNetworkManagerError

class TestInternetIfaceSelection(unittest.TestCase):

    def setUp(self):
        #setup NetworkManager
        ap_iface_obj = mock.MagicMock()
        ap_iface_obj._name = 'wlan0'
        ap_iface_obj._support_ap_mode = True
        ap_iface_obj._support_monitor_mode = False
        ap_iface_obj.is_internet_iface = False

        conn_iface_obj = mock.MagicMock()
        conn_iface_obj._name = 'wlan1'
        conn_iface_obj._support_ap_mode = False
        conn_iface_obj._support_monitor_mode = False
        conn_iface_obj.is_internet_iface = True


        self.nm = mock.MagicMock()
        self.nm.ap_iface = 'wlan0'
        self.nm.jam_iface = ""
        self.nm._interfaces = {}

        for iface_obj in [ap_iface_obj, conn_iface_obj]:
            self.nm._interfaces[iface_obj._name] = iface_obj

    def test_no_jamming_with_internet(self):
        """
        Test with -nJ case with internet connection
        And the managed property is correctly set
        """
        fake_check_iface_managed_by_nm(self.nm, is_managed_with_correct_setting)

    def test_using_internet_iface_as_ap_iface(self):
        """
        Test with -nJ case and use internet iface as AP iface
        should raise InterfaceManagedByNetworkManagerError exception
        """
        self.assertRaises(interfaces.InterfaceManagedByNetworkManagerError,
            fake_check_iface_managed_by_nm, self.nm, is_managed_with_incorrect_setting)

    def test_jamming_with_internet_access(self):
        """
        Test three interfaces ap/deauth/internet iface
        """
        deauth_iface_obj = mock.MagicMock()
        deauth_iface_obj._name = 'wlan2'
        deauth_iface_obj._support_ap_mode = False
        deauth_iface_obj._support_monitor_mode = True
        deauth_iface_obj.is_internet_iface = False
        self.nm.jam_iface = 'wlan2'
        self.nm._interfaces[deauth_iface_obj._name] = deauth_iface_obj

        fake_check_iface_managed_by_nm(self.nm, is_managed_with_correct_setting)

    @mock.patch('wifiphisher.pywifiphisher.kill_interfering_procs', return_value=0)
    def test_wo_internet_access(self, kill_proc):
        """
        Test without internet access
        """
        deauth_iface_obj = mock.MagicMock()
        deauth_iface_obj._name = 'wlan2'
        deauth_iface_obj._support_ap_mode = False
        deauth_iface_obj._support_monitor_mode = True
        deauth_iface_obj.is_internet_iface = False
        self.nm.jam_iface = 'wlan2'
        self.nm._interfaces[deauth_iface_obj._name] = deauth_iface_obj

        kill_proc()

if __name__ == '__main__':
    unittest.main()
