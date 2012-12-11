prefix=@CMAKE_INSTALL_PREFIX@
libdir=@CMAKE_INSTALL_LIBDIR@
includedir=@INCLUDE_INSTALL_DIR@

Name: Scintilla
Description: Scintilla Library ($\{target\} target)
Version: @scintilla_VERSION@
Requires: gtk+-2.0
Libs: -L@CMAKE_INSTALL_LIBDIR@ -lscintilla 
Cflags: -I@INCLUDE_INSTALL_DIR@/scintilla 
