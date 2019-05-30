""" OVSDB Models """
import json
import interface

class Bridge(object):

    DPDK_DATAPATH_TYPE = 'netdev'

    def __init__(
            self, name, auto_attach=list(), controller=list(), datapath_id='', datapath_type='',
            datapath_version='..', external_ids=dict(), fail_mode=list(), flood_vlans=list(),
            ipfix=list(), mcast_snooping_enable=False, mirrors=list(), netflow=list(),
            other_config=dict(), ports=list(), protocols=list(), rstp_enabled=False,
            rstp_status=dict(), sflow=list(), status=dict(), stp_enable=True
        ):
        self.__auto_attach = set(auto_attach)
        self.__controller = set(controller)
        self.__datapath_id = datapath_id
        self.__datapath_type = datapath_type
        self.__datapath_version = tuple(datapath_version.split('.'))
        self.__external_ids = external_ids
        self.__fail_mode = set(fail_mode)
        self.__flood_vlans = set(flood_vlans)
        self.__ipfix = set(ipfix)
        self.__mcast_snooping_enable = mcast_snooping_enable
        self.__mirrors = set(mirrors)
        self.__name = name
        self.__netflow = set(netflow)
        self.__other_config = other_config
        self.__ports = set(ports)
        self.__protocols = set(protocols)
        self.__rstp_enabled = rstp_enabled
        self.__rstp_status = rstp_status
        self.__sflow = set(sflow)
        self.__status = status
        self.__stp_enable = stp_enable

    @property
    def auto_attach(self):
        return self.__auto_attach

    @auto_attach.setter
    def auto_attach(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('auto_attach can only be a list or a set')
        self.__auto_attach = set(value)

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('controller can only be a list or a set')
        self.__controller = set(value)

    @property
    def datapath_id(self):
        return self.__datapath_id

    @datapath_id.setter
    def datapath_id(self, value):
        if (not isinstance(value, str)):
            raise ValueError('datapath_id can only be a string')
        self.__datapath_id = value

    @property
    def datapath_type(self):
        return self.__datapath_type

    @datapath_type.setter
    def datapath_type(self, value):
        if (not isinstance(value, str)):
            raise ValueError('datapath_type can only be a string')
        self.__datapath_type = value

    @property
    def datapath_version(self):
        return self.__datapath_version

    @datapath_version.setter
    def datapath_version(self, value):
        if (not isinstance(value, str)):
            raise ValueError('datapath_verion can only be a string')
        if (len(value.split('.')) != 3):
            raise ValueError('datapath_verion should be of the format x.x.x')
        self.__datapath_version = tuple(value.split('.'))

    @property
    def external_ids(self):
        return self.__external_ids

    @external_ids.setter
    def external_ids(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('external_ids can only be a dict')
        self.__external_ids = value

    @property
    def fail_mode(self):
        return self.__fail_mode

    @fail_mode.setter
    def fail_mode(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('fail_mode can only be a list or a set')
        self.__fail_mode = value

    @property
    def flood_vlans(self):
        return self.__flood_vlans

    @flood_vlans.setter
    def flood_vlans(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('flood_vlans can only be a list or a set')
        self.__flood_vlans = set(value)

    @property
    def ipfix(self):
        return self.__ipfix

    @ipfix.setter
    def ipfix(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('ipfix can only be a list or a set')
        self.__ipfix = set(value)

    @property
    def mcast_snooping_enable(self):
        return self.__mcast_snooping_enable

    @mcast_snooping_enable.setter
    def mcast_snooping_enable(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('mcast_snooping_error can only be a bool')
        self.__mcast_snooping_enable = value

    @property
    def mirrors(self):
        return self.__mirrors

    @mirrors.setter
    def mirrors(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('mirrors can only be a list or a set')
        self.__mirrors = set(value)

    @property
    def name(self):
        return self.__name

    @property
    def netflow(self):
        return self.__netflow

    @netflow.setter
    def netflow(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('netflow can only be a list or a set')
        self.__netflow = set(value)

    @property
    def other_config(self):
        return self.__other_config

    @other_config.setter
    def other_config(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('other_config can only be a dict')
        self.__other_config = value

    @property
    def ports(self):
        return self.__ports

    @ports.setter
    def ports(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('ports can only be a list or a set')
        for val in value:
            if (not isinstance(val, interface.Interface)):
                raise ValueError('ports need to a instances of Interface class')
        self.__ports = set(value)

    @property
    def protocols(self):
        return self.__protocols
    
    @protocols.setter
    def protocols(self, value):
        if (not isinstance(value, (list, set))):
            raise ValueError('protocols can only be a list or a set')
        self.__protocols = set(value)

    @property
    def rstp_enabled(self):
        return self.__rstp_enabled

    @rstp_enabled.setter
    def rstp_enabled(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('rstp_enabled can only be a bool')
        self.__rstp_enabled = value

    @property
    def rstp_status(self):
        return self.__rstp_status

    @rstp_status.setter
    def rstp_status(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('rstp_status can only be a dict')
        self.__rstp_status = value

    @property
    def sflow(self):
        return self.__sflow

    @sflow.setter
    def sflow(self, value):
        if (not isinstance(value, (set, list))):
            raise ValueError('sflow can only be a list or a dict')
        self.__sflow = set(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if (not isinstance(value, dict)):
            raise ValueError('status can only be a dict')
        self.__status = value

    @property
    def stp_enable(self):
        return self.__stp_enable

    @stp_enable.setter
    def stp_enable(self, value):
        if (not isinstance(value, bool)):
            raise ValueError('status can only be a boolean')
        self.__status = value

    def __str__(self):
        return json.dumps({
            'auto_attach': str(self.__auto_attach),
            'controller': str(self.__controller),
            'datapath_id': str(self.__datapath_id),
            'datapath_version': str(self.__datapath_version),
            'external_ids': str(self.__external_ids),
            'fail_mode': str(self.__fail_mode),
            'flood_vlans': str(self.__flood_vlans),
            'ipfix': str(self.__ipfix),
            'mcast_snooping_enable': str(self.__mcast_snooping_enable),
            'mirrors': str(self.__mirrors),
            'name': str(self.__name),
            'netflow': str(self.__netflow),
            'other_config': str(self.__other_config),
            'ports': str(self.__ports),
            'protocols': str(self.__protocols),
            'rstp_enabled': str(self.__rstp_enabled),
            'sflow': str(self.__sflow),
            'status': str(self.__status),
            'stp_enable': str(self.__stp_enable)
        })
