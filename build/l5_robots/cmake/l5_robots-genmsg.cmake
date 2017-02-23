# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "l5_robots: 3 messages, 0 services")

set(MSG_I_FLAGS "-Il5_robots:/home/alex/catkin_ws/src/l5_robots/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(l5_robots_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg" NAME_WE)
add_custom_target(_l5_robots_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "l5_robots" "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg" "l5_robots/CaRow"
)

get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg" NAME_WE)
add_custom_target(_l5_robots_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "l5_robots" "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg" ""
)

get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg" NAME_WE)
add_custom_target(_l5_robots_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "l5_robots" "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/l5_robots
)
_generate_msg_cpp(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/l5_robots
)
_generate_msg_cpp(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/l5_robots
)

### Generating Services

### Generating Module File
_generate_module_cpp(l5_robots
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/l5_robots
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(l5_robots_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(l5_robots_generate_messages l5_robots_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_cpp _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_cpp _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_cpp _l5_robots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(l5_robots_gencpp)
add_dependencies(l5_robots_gencpp l5_robots_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS l5_robots_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/l5_robots
)
_generate_msg_eus(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/l5_robots
)
_generate_msg_eus(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/l5_robots
)

### Generating Services

### Generating Module File
_generate_module_eus(l5_robots
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/l5_robots
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(l5_robots_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(l5_robots_generate_messages l5_robots_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_eus _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_eus _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_eus _l5_robots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(l5_robots_geneus)
add_dependencies(l5_robots_geneus l5_robots_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS l5_robots_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/l5_robots
)
_generate_msg_lisp(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/l5_robots
)
_generate_msg_lisp(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/l5_robots
)

### Generating Services

### Generating Module File
_generate_module_lisp(l5_robots
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/l5_robots
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(l5_robots_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(l5_robots_generate_messages l5_robots_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_lisp _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_lisp _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_lisp _l5_robots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(l5_robots_genlisp)
add_dependencies(l5_robots_genlisp l5_robots_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS l5_robots_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/l5_robots
)
_generate_msg_nodejs(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/l5_robots
)
_generate_msg_nodejs(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/l5_robots
)

### Generating Services

### Generating Module File
_generate_module_nodejs(l5_robots
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/l5_robots
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(l5_robots_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(l5_robots_generate_messages l5_robots_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_nodejs _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_nodejs _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_nodejs _l5_robots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(l5_robots_gennodejs)
add_dependencies(l5_robots_gennodejs l5_robots_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS l5_robots_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg"
  "${MSG_I_FLAGS}"
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/l5_robots
)
_generate_msg_py(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/l5_robots
)
_generate_msg_py(l5_robots
  "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/l5_robots
)

### Generating Services

### Generating Module File
_generate_module_py(l5_robots
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/l5_robots
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(l5_robots_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(l5_robots_generate_messages l5_robots_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaGrid.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_py _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/CaRow.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_py _l5_robots_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/alex/catkin_ws/src/l5_robots/msg/Obstacles.msg" NAME_WE)
add_dependencies(l5_robots_generate_messages_py _l5_robots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(l5_robots_genpy)
add_dependencies(l5_robots_genpy l5_robots_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS l5_robots_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/l5_robots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/l5_robots
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(l5_robots_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/l5_robots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/l5_robots
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(l5_robots_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/l5_robots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/l5_robots
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(l5_robots_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/l5_robots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/l5_robots
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(l5_robots_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/l5_robots)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/l5_robots\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/l5_robots
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(l5_robots_generate_messages_py std_msgs_generate_messages_py)
endif()
