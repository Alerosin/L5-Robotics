// Auto-generated. Do not edit!

// (in-package l5_robots.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------

class Obstacles {
  constructor() {
    this.angles = [];
    this.distances = [];
    this.max_range = 0.0;
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type Obstacles
    // Serialize the length for message field [angles]
    bufferInfo = _serializer.uint32(obj.angles.length, bufferInfo);
    // Serialize message field [angles]
    obj.angles.forEach((val) => {
      bufferInfo = _serializer.float32(val, bufferInfo);
    });
    // Serialize the length for message field [distances]
    bufferInfo = _serializer.uint32(obj.distances.length, bufferInfo);
    // Serialize message field [distances]
    obj.distances.forEach((val) => {
      bufferInfo = _serializer.float32(val, bufferInfo);
    });
    // Serialize message field [max_range]
    bufferInfo = _serializer.float32(obj.max_range, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type Obstacles
    let tmp;
    let len;
    let data = new Obstacles();
    // Deserialize array length for message field [angles]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [angles]
    data.angles = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.float32(buffer);
      data.angles[i] = tmp.data;
      buffer = tmp.buffer;
    }
    // Deserialize array length for message field [distances]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [distances]
    data.distances = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.float32(buffer);
      data.distances[i] = tmp.data;
      buffer = tmp.buffer;
    }
    // Deserialize message field [max_range]
    tmp = _deserializer.float32(buffer);
    data.max_range = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'l5_robots/Obstacles';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4091faabcc1f00827c0de46a68c91753';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] angles
    float32[] distances
    float32 max_range
    
    `;
  }

};

module.exports = Obstacles;
