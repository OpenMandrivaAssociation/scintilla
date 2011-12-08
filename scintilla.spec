%define name 	scintilla
%define version 2.02
%define release %mkrel 2
%define libname %mklibname scintilla 2
%define develname %mklibname -d scintilla

%define scintillaver %(echo %{version} | sed -e 's/\\.//')

Summary: 	Free source code editing component
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Editors
Url: 		http://www.scintilla.org/index.html
Source0: 	http://prdownloads.sourceforge.net/scintilla/scintilla%scintillaver.tgz
Source1:	scintilla.cmake
Source2:	scintilla.pc.cmake
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires:	gtk+2-devel pkgconfig
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
Obsoletes:      %{_lib}scintilla0 < 1.79-2

%description -n %{libname}
This package contains scintilla shared libraries.

%package -n	%{develname}
Group:		Development/C
Summary:	Headers and static lib for scintilla development
Requires:	%{libname} = %{version}-%{release}
Provides:	scintilla-devel = %{version}-%{release}
Conflicts:	%{_lib}scintilla0 < 1.79-2

%description -n	%{develname}
Install this package if you want do compile applications using the
scintilla library.

%prep
%setup -q -n scintilla
cp %SOURCE1 %{_builddir}/scintilla/CMakeLists.txt
cp %SOURCE2 %{_builddir}/scintilla/scintilla.pc.cmake

%build
%{cmake}
%make

%install
rm -fr $RPM_BUILD_ROOT
cd build
%{makeinstall_std}

%clean
rm -fr $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(644, root, root)
%{_libdir}/libscintilla.so.2*

%files -n %{develname}
%defattr(644, root, root)
%attr(755, root, root) %dir %{_includedir}/scintilla
%{_libdir}/libscintilla.so
%{_libdir}/pkgconfig/scintilla.pc
%{_includedir}/scintilla/*.h
