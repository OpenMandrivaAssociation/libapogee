%define svn   190

Name:          libapogee
Summary:       Apogee Instruments Library
Version:       2.2
Release:       %mkrel 0.%svn.1
Url:           http://indi.sourceforge.net/index.php/Main_Page
License:       GPLv2+
Group:         Development/KDE and Qt
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       %{name}-%{version}.%svn.tar.bz2
BuildRequires: kde4-macros
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
%_kde_libdir/libapogeee.so.%{apogeee_major}*

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
%_kde_libdir/libapogeeu.so.%{apogeeu_major}*

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
%_kde_includedir/libapogee
%_kde_libdir/libapogeee.so
%_kde_libdir/libapogeeu.so

#---------------------------------------------

%prep
%setup -q  -n %name

%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
