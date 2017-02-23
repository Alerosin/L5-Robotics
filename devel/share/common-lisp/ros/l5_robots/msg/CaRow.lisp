; Auto-generated. Do not edit!


(cl:in-package l5_robots-msg)


;//! \htmlinclude CaRow.msg.html

(cl:defclass <CaRow> (roslisp-msg-protocol:ros-message)
  ((row
    :reader row
    :initarg :row
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass CaRow (<CaRow>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CaRow>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CaRow)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name l5_robots-msg:<CaRow> is deprecated: use l5_robots-msg:CaRow instead.")))

(cl:ensure-generic-function 'row-val :lambda-list '(m))
(cl:defmethod row-val ((m <CaRow>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader l5_robots-msg:row-val is deprecated.  Use l5_robots-msg:row instead.")
  (row m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CaRow>) ostream)
  "Serializes a message object of type '<CaRow>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'row))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'row))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CaRow>) istream)
  "Deserializes a message object of type '<CaRow>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'row) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'row)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CaRow>)))
  "Returns string type for a message object of type '<CaRow>"
  "l5_robots/CaRow")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CaRow)))
  "Returns string type for a message object of type 'CaRow"
  "l5_robots/CaRow")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CaRow>)))
  "Returns md5sum for a message object of type '<CaRow>"
  "9b20dc667218469d78f38ccd9c9712d6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CaRow)))
  "Returns md5sum for a message object of type 'CaRow"
  "9b20dc667218469d78f38ccd9c9712d6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CaRow>)))
  "Returns full string definition for message of type '<CaRow>"
  (cl:format cl:nil "int32[] row~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CaRow)))
  "Returns full string definition for message of type 'CaRow"
  (cl:format cl:nil "int32[] row~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CaRow>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'row) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CaRow>))
  "Converts a ROS message object to a list"
  (cl:list 'CaRow
    (cl:cons ':row (row msg))
))
