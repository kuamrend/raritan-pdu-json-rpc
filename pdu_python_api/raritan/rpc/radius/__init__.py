# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.0.0-3.0.9-branch-20140613-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libradius_client/src/idl/RadiusServerSettings.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.radius


# enumeration
class AuthType(Enumeration):
    idlType = "radius.AuthType:1.0.0"
    values = ["PAP", "CHAP"]

AuthType.PAP = AuthType(0)
AuthType.CHAP = AuthType(1)

# structure
class ServerSettings(Structure):
    idlType = "radius.ServerSettings:1.0.0"
    elements = ["id", "server", "sharedSecret", "udpAuthPort", "udpAccountPort", "timeout", "retries", "authType"]

    def __init__(self, id, server, sharedSecret, udpAuthPort, udpAccountPort, timeout, retries, authType):
        typecheck.is_string(id, AssertionError)
        typecheck.is_string(server, AssertionError)
        typecheck.is_string(sharedSecret, AssertionError)
        typecheck.is_int(udpAuthPort, AssertionError)
        typecheck.is_int(udpAccountPort, AssertionError)
        typecheck.is_int(timeout, AssertionError)
        typecheck.is_int(retries, AssertionError)
        typecheck.is_enum(authType, raritan.rpc.radius.AuthType, AssertionError)

        self.id = id
        self.server = server
        self.sharedSecret = sharedSecret
        self.udpAuthPort = udpAuthPort
        self.udpAccountPort = udpAccountPort
        self.timeout = timeout
        self.retries = retries
        self.authType = authType

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            id = json['id'],
            server = json['server'],
            sharedSecret = json['sharedSecret'],
            udpAuthPort = json['udpAuthPort'],
            udpAccountPort = json['udpAccountPort'],
            timeout = json['timeout'],
            retries = json['retries'],
            authType = raritan.rpc.radius.AuthType.decode(json['authType']),
        )
        return obj

    def encode(self):
        json = {}
        json['id'] = self.id
        json['server'] = self.server
        json['sharedSecret'] = self.sharedSecret
        json['udpAuthPort'] = self.udpAuthPort
        json['udpAccountPort'] = self.udpAccountPort
        json['timeout'] = self.timeout
        json['retries'] = self.retries
        json['authType'] = raritan.rpc.radius.AuthType.encode(self.authType)
        return json
