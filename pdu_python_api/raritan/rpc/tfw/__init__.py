# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.0.0-3.0.9-branch-20140613-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libidl_client/topofw/core/idl/ScannerCtrl.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException

# interface
class ScannerCtrl(Interface):
    idlType = "tfw.ScannerCtrl:1.0.0"

    def getScanInterval(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getScanInterval', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def setScanInterval(self, interval):
        agent = self.agent
        typecheck.is_int(interval, AssertionError)
        args = {}
        args['interval'] = interval
        rsp = agent.json_rpc(self.target, 'setScanInterval', args)
# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.0.0-3.0.9-branch-20140613-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libidl_client/topofw/core/idl/CoreCtrl.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.tfw


# interface
class CoreCtrl(Interface):
    idlType = "tfw.CoreCtrl:1.0.0"

    def getScanner(self, name):
        agent = self.agent
        typecheck.is_string(name, AssertionError)
        args = {}
        args['name'] = name
        rsp = agent.json_rpc(self.target, 'getScanner', args)
        _ret_ = Interface.decode(rsp['_ret_'], agent)
        typecheck.is_interface(_ret_, raritan.rpc.tfw.ScannerCtrl, DecodeException)
        return _ret_

    def startAllScanners(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'startAllScanners', args)

    def stopAllScanners(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'stopAllScanners', args)

    def startAllBackWorkers(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'startAllBackWorkers', args)

    def stopAllBackWorkers(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'stopAllBackWorkers', args)