%define name 	scintilla
%define version 3.2.2
%define release 0
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


%changelog
* Tue Oct  2 2012 Sergey Sokolov <sokol@mtik.ru> 3.2.2-0
- update to 3.2.2

* Mon May 14 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.1.0-2
+ Revision: 798793
- use gtk+3 instead gtk+2
- update to 3.1.0

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.02-2mdv2011.0
+ Revision: 614825
- the mass rebuild of 2010.1 packages

* Fri Feb 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.02-1mdv2010.1
+ Revision: 505083
- update to 202

* Sat Dec 12 2009 Funda Wang <fwang@mandriva.org> 2.01-1mdv2010.1
+ Revision: 477834
- new version 2.01

* Tue Oct 27 2009 Funda Wang <fwang@mandriva.org> 1.79-2mdv2010.0
+ Revision: 459454
- move so file into devel package

* Mon Jul 20 2009 Raphaël Gertz <rapsys@mandriva.org> 1.79-1mdv2010.0
+ Revision: 398016
- Fix install path
- Add cmake dep
- Import new scintilla library
  Use an alternative cmake build system
- Created package structure for scintilla.

