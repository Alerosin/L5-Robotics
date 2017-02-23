;; Auto-generated. Do not edit!


(when (boundp 'l5_robots::CaGrid)
  (if (not (find-package "L5_ROBOTS"))
    (make-package "L5_ROBOTS"))
  (shadow 'CaGrid (find-package "L5_ROBOTS")))
(unless (find-package "L5_ROBOTS::CAGRID")
  (make-package "L5_ROBOTS::CAGRID"))

(in-package "ROS")
;;//! \htmlinclude CaGrid.msg.html


(defclass l5_robots::CaGrid
  :super ros::object
  :slots (_grid ))

(defmethod l5_robots::CaGrid
  (:init
   (&key
    ((:grid __grid) (let (r) (dotimes (i 0) (push (instance l5_robots::CaRow :init) r)) r))
    )
   (send-super :init)
   (setq _grid __grid)
   self)
  (:grid
   (&rest __grid)
   (if (keywordp (car __grid))
       (send* _grid __grid)
     (progn
       (if __grid (setq _grid (car __grid)))
       _grid)))
  (:serialization-length
   ()
   (+
    ;; l5_robots/CaRow[] _grid
    (apply #'+ (send-all _grid :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; l5_robots/CaRow[] _grid
     (write-long (length _grid) s)
     (dolist (elem _grid)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; l5_robots/CaRow[] _grid
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _grid (let (r) (dotimes (i n) (push (instance l5_robots::CaRow :init) r)) r))
     (dolist (elem- _grid)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get l5_robots::CaGrid :md5sum-) "d0741c1f4072196731466d956358fcef")
(setf (get l5_robots::CaGrid :datatype-) "l5_robots/CaGrid")
(setf (get l5_robots::CaGrid :definition-)
      "CaRow[] grid
================================================================================
MSG: l5_robots/CaRow
int32[] row

")



(provide :l5_robots/CaGrid "d0741c1f4072196731466d956358fcef")


