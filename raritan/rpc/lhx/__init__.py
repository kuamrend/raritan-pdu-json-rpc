# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.0.0-3.0.9-branch-20140613-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libisys/src/idl/LhxSupport.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException

# interface
class Support(Interface):
    idlType = "lhx.Support:1.0.0"

    def setEnabled(self, enabled):
        agent = self.agent
        typecheck.is_bool(enabled, AssertionError)
        args = {}
        args['enabled'] = enabled
        rsp = agent.json_rpc(self.target, 'setEnabled', args)

    def isEnabled(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'isEnabled', args)
        _ret_ = rsp['_ret_']
        typecheck.is_bool(_ret_, DecodeException)
        return _ret_
