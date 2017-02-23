;; Auto-generated. Do not edit!


(when (boundp 'l5_robots::Obstacles)
  (if (not (find-package "L5_ROBOTS"))
    (make-package "L5_ROBOTS"))
  (shadow 'Obstacles (find-package "L5_ROBOTS")))
(unless (find-package "L5_ROBOTS::OBSTACLES")
  (make-package "L5_ROBOTS::OBSTACLES"))

(in-package "ROS")
;;//! \htmlinclude Obstacles.msg.html


(defclass l5_robots::Obstacles
  :super ros::object
  :slots (_angles _distances _max_range ))

(defmethod l5_robots::Obstacles
  (:init
   (&key
    ((:angles __angles) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:distances __distances) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:max_range __max_range) 0.0)
    )
   (send-super :init)
   (setq _angles __angles)
   (setq _distances __distances)
   (setq _max_range (float __max_range))
   self)
  (:angles
   (&optional __angles)
   (if __angles (setq _angles __angles)) _angles)
  (:distances
   (&optional __distances)
   (if __distances (setq _distances __distances)) _distances)
  (:max_range
   (&optional __max_range)
   (if __max_range (setq _max_range __max_range)) _max_range)
  (:serialization-length
   ()
   (+
    ;; float32[] _angles
    (* 4    (length _angles)) 4
    ;; float32[] _distances
    (* 4    (length _distances)) 4
    ;; float32 _max_range
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _angles
     (write-long (length _angles) s)
     (dotimes (i (length _angles))
       (sys::poke (elt _angles i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _distances
     (write-long (length _distances) s)
     (dotimes (i (length _distances))
       (sys::poke (elt _distances i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32 _max_range
       (sys::poke _max_range (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _angles
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _angles (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _angles i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _distances
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _distances (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _distances i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32 _max_range
     (setq _max_range (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get l5_robots::Obstacles :md5sum-) "4091faabcc1f00827c0de46a68c91753")
(setf (get l5_robots::Obstacles :datatype-) "l5_robots/Obstacles")
(setf (get l5_robots::Obstacles :definition-)
      "float32[] angles
float32[] distances
float32 max_range

")



(provide :l5_robots/Obstacles "4091faabcc1f00827c0de46a68c91753")


