// Auto-generated. Do not edit!

// (in-package l5_robots.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let CaRow = require('./CaRow.js');

//-----------------------------------------------------------

class CaGrid {
  constructor() {
    this.grid = [];
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type CaGrid
    // Serialize the length for message field [grid]
    bufferInfo = _serializer.uint32(obj.grid.length, bufferInfo);
    // Serialize message field [grid]
    obj.grid.forEach((val) => {
      bufferInfo = CaRow.serialize(val, bufferInfo);
    });
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type CaGrid
    let tmp;
    let len;
    let data = new CaGrid();
    // Deserialize array length for message field [grid]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [grid]
    data.grid = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = CaRow.deserialize(buffer);
      data.grid[i] = tmp.data;
      buffer = tmp.buffer;
    }
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'l5_robots/CaGrid';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd0741c1f4072196731466d956358fcef';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    CaRow[] grid
    ================================================================================
    MSG: l5_robots/CaRow
    int32[] row
    
    `;
  }

};

module.exports = CaGrid;
