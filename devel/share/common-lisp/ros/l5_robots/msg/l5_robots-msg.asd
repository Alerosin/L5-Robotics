
(cl:in-package :asdf)

(defsystem "l5_robots-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CaGrid" :depends-on ("_package_CaGrid"))
    (:file "_package_CaGrid" :depends-on ("_package"))
    (:file "CaRow" :depends-on ("_package_CaRow"))
    (:file "_package_CaRow" :depends-on ("_package"))
    (:file "Obstacles" :depends-on ("_package_Obstacles"))
    (:file "_package_Obstacles" :depends-on ("_package"))
  ))