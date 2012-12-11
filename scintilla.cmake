#vim: set shiftwidth=4 tabstop=4 smarttab noexpandtab foldmethod=marker textwidth=80:

# set cmake minimal version
cmake_minimum_required(VERSION 2.6)

# the project name
project(scintilla)
set(scintilla_VERSION_MAJOR "3")
set(scintilla_VERSION_MINOR "1")
set(scintilla_VERSION "${scintilla_VERSION_MAJOR}.${scintilla_VERSION_MINOR}")

# Set informations for Debug and RelWithDebInfo build type
if (NOT CMAKE_BUILD_TYPE)
	message("-- Change build type with : cmake -DCMAKE_BUILD_TYPE=(Debug|Release|RelWithDebInfo|MinSizeRel) ..")
endif()

# find and setup Gtk2for this project
#find_package(GTK2 REQUIRED) #require findgtk2.cmake
include(FindPkgConfig)
pkg_search_module(GTK gtk+-3.0 gtk+-2.0)

if (NOT GTK_FOUND)
	message(FATAL_ERROR "Unable to find gtk+-3.0 or gtk+-2.0")
else ()
	include_directories(${GTK_INCLUDE_DIRS})
	add_definitions(${GTK_DEFINITIONS})
	link_directories(${GTK_LIBRARY_DIRS})
endif ()

FIND_LIBRARY(GTHREAD2_LIBRARIES
	NAMES  gthread2 gthread20 gthread2.0 gthread-20 gthread-2.0
	PATHS  /usr/openwin/lib /opt/gnome/lib
)

if (NOT GTHREAD2_LIBRARIES)
	message(FATAL_ERROR "Unable to find gthread-2.0")
endif ()

pkg_search_module (GMODULE REQUIRED gmodule-2.0)

if (NOT GMODULE_FOUND)
	message(FATAL_ERROR "Unable to find gmodule-2.0")
endif ()

# Don't use temporary file
add_definitions(-pipe)
# Re-add old build flags
add_definitions(-Wall)
add_definitions(-pedantic)
add_definitions(-DGTK)
add_definitions(-DSCI_LEXER)

# inclusion de la source de destination
include_directories(${scintilla_SOURCE_DIR}/include)
include_directories(${scintilla_SOURCE_DIR}/src)
include_directories(${scintilla_SOURCE_DIR}/lexlib)

# create a library from the sources files.
file(GLOB_RECURSE scintilla_SRCS ${scintilla_SOURCE_DIR}/gtk/*.cxx ${scintilla_SOURCE_DIR}/src/*.cxx ${scintilla_SOURCE_DIR}/gtk/*.c ${scintilla_SOURCE_DIR}/lexlib/*.cxx ${scintilla_SOURCE_DIR}/lexers/*.cxx)
add_library(scintilla SHARED ${scintilla_SRCS})
target_link_libraries(scintilla ${GTK_LIBRARIES} ${GTHREAD2_LIBRARIES} ${GMODULE_LIBRARIES})
set_target_properties(scintilla PROPERTIES VERSION ${scintilla_VERSION} SOVERSION ${scintilla_VERSION_MAJOR})

# install the generated binary
install(TARGETS scintilla DESTINATION ${CMAKE_INSTALL_LIBDIR})

# generate scintilla.pc.cmake file
configure_file(${scintilla_SOURCE_DIR}/scintilla.pc.cmake ${scintilla_BINARY_DIR}/scintilla.pc)

# install scintilla headers
file(GLOB_RECURSE scintilla_HDRS ${scintilla_SOURCE_DIR}/include/*.h)
install(FILES ${scintilla_HDRS} DESTINATION ${INCLUDE_INSTALL_DIR}/scintilla)
install(FILES ${scintilla_BINARY_DIR}/scintilla.pc DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig)
