// Auto-generated. Do not edit!

// (in-package l5_robots.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class CaRow {
  constructor() {
    this.row = [];
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type CaRow
    // Serialize the length for message field [row]
    bufferInfo = _serializer.uint32(obj.row.length, bufferInfo);
    // Serialize message field [row]
    obj.row.forEach((val) => {
      bufferInfo = _serializer.int32(val, bufferInfo);
    });
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type CaRow
    let tmp;
    let len;
    let data = new CaRow();
    // Deserialize array length for message field [row]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [row]
    data.row = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.int32(buffer);
      data.row[i] = tmp.data;
      buffer = tmp.buffer;
    }
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'l5_robots/CaRow';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9b20dc667218469d78f38ccd9c9712d6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] row
    
    `;
  }

};

module.exports = CaRow;
