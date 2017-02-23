;; Auto-generated. Do not edit!


(when (boundp 'l5_robots::CaRow)
  (if (not (find-package "L5_ROBOTS"))
    (make-package "L5_ROBOTS"))
  (shadow 'CaRow (find-package "L5_ROBOTS")))
(unless (find-package "L5_ROBOTS::CAROW")
  (make-package "L5_ROBOTS::CAROW"))

(in-package "ROS")
;;//! \htmlinclude CaRow.msg.html


(defclass l5_robots::CaRow
  :super ros::object
  :slots (_row ))

(defmethod l5_robots::CaRow
  (:init
   (&key
    ((:row __row) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _row __row)
   self)
  (:row
   (&optional __row)
   (if __row (setq _row __row)) _row)
  (:serialization-length
   ()
   (+
    ;; int32[] _row
    (* 4    (length _row)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _row
     (write-long (length _row) s)
     (dotimes (i (length _row))
       (write-long (elt _row i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _row
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _row (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _row i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get l5_robots::CaRow :md5sum-) "9b20dc667218469d78f38ccd9c9712d6")
(setf (get l5_robots::CaRow :datatype-) "l5_robots/CaRow")
(setf (get l5_robots::CaRow :definition-)
      "int32[] row

")



(provide :l5_robots/CaRow "9b20dc667218469d78f38ccd9c9712d6")


