# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from l5_robots/CaGrid.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import l5_robots.msg

class CaGrid(genpy.Message):
  _md5sum = "d0741c1f4072196731466d956358fcef"
  _type = "l5_robots/CaGrid"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """CaRow[] grid
================================================================================
MSG: l5_robots/CaRow
int32[] row
"""
  __slots__ = ['grid']
  _slot_types = ['l5_robots/CaRow[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       grid

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CaGrid, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.grid is None:
        self.grid = []
    else:
      self.grid = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.grid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid:
        length = len(val1.row)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(struct.pack(pattern, *val1.row))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.grid is None:
        self.grid = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid = []
      for i in range(0, length):
        val1 = l5_robots.msg.CaRow()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        end += struct.calcsize(pattern)
        val1.row = struct.unpack(pattern, str[start:end])
        self.grid.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.grid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid:
        length = len(val1.row)
        buff.write(_struct_I.pack(length))
        pattern = '<%si'%length
        buff.write(val1.row.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.grid is None:
        self.grid = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid = []
      for i in range(0, length):
        val1 = l5_robots.msg.CaRow()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%si'%length
        start = end
        end += struct.calcsize(pattern)
        val1.row = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
        self.grid.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I