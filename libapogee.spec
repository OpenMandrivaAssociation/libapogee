Name:          libapogee
Summary:       Apogee Instruments Library
Version:       2.2
Release:       %mkrel 1
Url:           http://indi.sourceforge.net/index.php/Main_Page
License:       GPLv2+
Group:         Development/KDE and Qt
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       http://downloads.sourceforge.net/indi/libapogee2_%version.tar.gz
Patch0:        libapogee-2.2.190-fix-lib.patch
Patch1:        libapogee2_2.2-fix-str-fmt.patch
BuildRequires: cmake
BuildRequires: libusb-devel
BuildRequires: curl-devel

%description
Apogee Instruments Library

#---------------------------------------------

%define apogeee_major 2
%define libapogeee %mklibname apogeee %{apogeee_major}

%package -n %libapogeee
Summary: KDE 4 library
Group: System/Libraries

%description -n %libapogeee
%name library

%files -n %libapogeee
%defattr(-,root,root)
%_libdir/libapogeee.so.%{apogeee_major}*

#---------------------------------------------

%define apogeeu_major 2
%define libapogeeu %mklibname apogeeu %{apogeeu_major}

%package -n %libapogeeu
Summary: KDE 4 library
Group: System/Libraries

%description -n %libapogeeu
%name library

%files -n %libapogeeu
%defattr(-,root,root)
%_libdir/libapogeeu.so.%{apogeeu_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: %libapogeee = %version
Requires: %libapogeeu = %version
%description  devel
Files needed to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_includedir/libapogee
%_libdir/libapogeee.so
%_libdir/libapogeeu.so

#---------------------------------------------

%prep
%setup -q  -n libapogee2-%version
%patch0 -p1
%patch1 -p0

%build
%cmake
%make

%install
rm -rf "%{buildroot}"
%makeinstall_std -C build

%clean
rm -rf "%{buildroot}"
