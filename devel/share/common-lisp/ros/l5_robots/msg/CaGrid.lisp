; Auto-generated. Do not edit!


(cl:in-package l5_robots-msg)


;//! \htmlinclude CaGrid.msg.html

(cl:defclass <CaGrid> (roslisp-msg-protocol:ros-message)
  ((grid
    :reader grid
    :initarg :grid
    :type (cl:vector l5_robots-msg:CaRow)
   :initform (cl:make-array 0 :element-type 'l5_robots-msg:CaRow :initial-element (cl:make-instance 'l5_robots-msg:CaRow))))
)

(cl:defclass CaGrid (<CaGrid>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CaGrid>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CaGrid)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name l5_robots-msg:<CaGrid> is deprecated: use l5_robots-msg:CaGrid instead.")))

(cl:ensure-generic-function 'grid-val :lambda-list '(m))
(cl:defmethod grid-val ((m <CaGrid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader l5_robots-msg:grid-val is deprecated.  Use l5_robots-msg:grid instead.")
  (grid m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CaGrid>) ostream)
  "Serializes a message object of type '<CaGrid>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'grid))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'grid))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CaGrid>) istream)
  "Deserializes a message object of type '<CaGrid>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'grid) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'grid)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'l5_robots-msg:CaRow))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CaGrid>)))
  "Returns string type for a message object of type '<CaGrid>"
  "l5_robots/CaGrid")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CaGrid)))
  "Returns string type for a message object of type 'CaGrid"
  "l5_robots/CaGrid")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CaGrid>)))
  "Returns md5sum for a message object of type '<CaGrid>"
  "d0741c1f4072196731466d956358fcef")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CaGrid)))
  "Returns md5sum for a message object of type 'CaGrid"
  "d0741c1f4072196731466d956358fcef")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CaGrid>)))
  "Returns full string definition for message of type '<CaGrid>"
  (cl:format cl:nil "CaRow[] grid~%================================================================================~%MSG: l5_robots/CaRow~%int32[] row~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CaGrid)))
  "Returns full string definition for message of type 'CaGrid"
  (cl:format cl:nil "CaRow[] grid~%================================================================================~%MSG: l5_robots/CaRow~%int32[] row~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CaGrid>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'grid) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CaGrid>))
  "Converts a ROS message object to a list"
  (cl:list 'CaGrid
    (cl:cons ':grid (grid msg))
))
