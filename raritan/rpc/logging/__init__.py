# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.0.0-3.0.9-branch-20140613-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libisys/src/idl/Log.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException

# structure
class LogEntry(Structure):
    idlType = "logging.LogEntry:1.0.0"
    elements = ["id", "timestamp", "eventClass", "message"]

    def __init__(self, id, timestamp, eventClass, message):
        typecheck.is_int(id, AssertionError)
        typecheck.is_time(timestamp, AssertionError)
        typecheck.is_string(eventClass, AssertionError)
        typecheck.is_string(message, AssertionError)

        self.id = id
        self.timestamp = timestamp
        self.eventClass = eventClass
        self.message = message

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            id = json['id'],
            timestamp = raritan.rpc.Time.decode(json['timestamp']),
            eventClass = json['eventClass'],
            message = json['message'],
        )
        return obj

    def encode(self):
        json = {}
        json['id'] = self.id
        json['timestamp'] = raritan.rpc.Time.encode(self.timestamp)
        json['eventClass'] = self.eventClass
        json['message'] = self.message
        return json

# enumeration
class RangeDirection(Enumeration):
    idlType = "logging.RangeDirection:1.0.0"
    values = ["FORWARD", "BACKWARD"]

RangeDirection.FORWARD = RangeDirection(0)
RangeDirection.BACKWARD = RangeDirection(1)
# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.0.0-3.0.9-branch-20140613-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libisys/src/idl/EventLog.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.event

import raritan.rpc.logging


# value object
class EventLogClearedEvent(raritan.rpc.event.UserEvent):
    idlType = "logging.EventLogClearedEvent:1.0.0"

    def __init__(self, actUserName, actIpAddr, source):
        super(raritan.rpc.logging.EventLogClearedEvent, self).__init__(actUserName, actIpAddr, source)

    def encode(self):
        json = super(raritan.rpc.logging.EventLogClearedEvent, self).encode()
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            # for event.UserEvent
            actUserName = json['actUserName'],
            actIpAddr = json['actIpAddr'],
            # for idl.Event
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = []
        elements = elements + super(raritan.rpc.logging.EventLogClearedEvent, self).listElements()
        return elements

# interface
class EventLog(Interface):
    idlType = "logging.EventLog:1.0.1"

    def clear(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'clear', args)

    def getFirstId(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getFirstId', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getLastId(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getLastId', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getEntries(self, refId, count, direction):
        agent = self.agent
        typecheck.is_int(refId, AssertionError)
        typecheck.is_int(count, AssertionError)
        typecheck.is_enum(direction, raritan.rpc.logging.RangeDirection, AssertionError)
        args = {}
        args['refId'] = refId
        args['count'] = count
        args['direction'] = raritan.rpc.logging.RangeDirection.encode(direction)
        rsp = agent.json_rpc(self.target, 'getEntries', args)
        entries = [raritan.rpc.logging.LogEntry.decode(x0, agent) for x0 in rsp['entries']]
        for x0 in entries:
            typecheck.is_struct(x0, raritan.rpc.logging.LogEntry, DecodeException)
        return entries

    def getFilteredEntries(self, refId, count, direction, eventClasses):
        agent = self.agent
        typecheck.is_int(refId, AssertionError)
        typecheck.is_int(count, AssertionError)
        typecheck.is_enum(direction, raritan.rpc.logging.RangeDirection, AssertionError)
        for x0 in eventClasses:
            typecheck.is_string(x0, AssertionError)
        args = {}
        args['refId'] = refId
        args['count'] = count
        args['direction'] = raritan.rpc.logging.RangeDirection.encode(direction)
        args['eventClasses'] = [x0 for x0 in eventClasses]
        rsp = agent.json_rpc(self.target, 'getFilteredEntries', args)
        entries = [raritan.rpc.logging.LogEntry.decode(x0, agent) for x0 in rsp['entries']]
        for x0 in entries:
            typecheck.is_struct(x0, raritan.rpc.logging.LogEntry, DecodeException)
        return entries
# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/MEGA/px2-3.0.0-3.0.9-branch-20140613-none-release-none-pdu-raritan/fwcomponents/mkdist/tmp/px2_final/libisys/src/idl/DebugLog.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.logging


# interface
class DebugLog(Interface):
    idlType = "logging.DebugLog:1.0.0"

    def clear(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'clear', args)

    def getFirstId(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getFirstId', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getLastId(self):
        agent = self.agent
        args = {}
        rsp = agent.json_rpc(self.target, 'getLastId', args)
        _ret_ = rsp['_ret_']
        typecheck.is_int(_ret_, DecodeException)
        return _ret_

    def getEntries(self, refId, count, direction):
        agent = self.agent
        typecheck.is_int(refId, AssertionError)
        typecheck.is_int(count, AssertionError)
        typecheck.is_enum(direction, raritan.rpc.logging.RangeDirection, AssertionError)
        args = {}
        args['refId'] = refId
        args['count'] = count
        args['direction'] = raritan.rpc.logging.RangeDirection.encode(direction)
        rsp = agent.json_rpc(self.target, 'getEntries', args)
        entries = [raritan.rpc.logging.LogEntry.decode(x0, agent) for x0 in rsp['entries']]
        for x0 in entries:
            typecheck.is_struct(x0, raritan.rpc.logging.LogEntry, DecodeException)
        return entries
