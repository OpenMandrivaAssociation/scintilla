%define name 	scintilla
%define version 3.1.0
%define release 2
%define major 3
%define libname %mklibname scintilla %{major}
%define develname %mklibname -d scintilla

%define scintillaver %(echo %{version} | sed -e 's/\\.//g')

Summary: 	Free source code editing component
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Editors
Url: 		http://www.scintilla.org/index.html
Source0: 	http://prdownloads.sourceforge.net/scintilla/scintilla%{scintillaver}.tgz
Source1:	scintilla.cmake
Source2:	scintilla.pc.cmake
BuildRequires:	gtk+3-devel pkgconfig
BuildRequires:	cmake >= 2.6

%description
Scintilla is a free source code editing component. As well as features
found in standard text editing components, Scintilla includes features
especially useful when editing and debugging source code. These include
support for syntax styling, error indicators, code completion and call
tips.

%package -n %{libname}
Summary:	Scintilla shared libraries
Group:		System/Servers

%description -n %{libname}
This package contains scintilla shared libraries.

%package -n	%{develname}
Group:		Development/C
Summary:	Headers and static lib for scintilla development
Requires:	%{libname} = %{version}
Provides:	scintilla-devel = %{EVRD}

%description -n	%{develname}
Install this package if you want do compile applications using the
scintilla library.

%prep
%setup -q -n scintilla
cp %SOURCE1 %{_builddir}/scintilla/CMakeLists.txt
cp %SOURCE2 %{_builddir}/scintilla/scintilla.pc.cmake

%build
%{cmake}
make

%install
pushd build
%makeinstall_std
popd

%files -n %{libname}
%{_libdir}/libscintilla.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/scintilla
%{_libdir}/libscintilla.so
%{_libdir}/pkgconfig/scintilla.pc
%{_includedir}/scintilla/*.h
%doc License.txt
