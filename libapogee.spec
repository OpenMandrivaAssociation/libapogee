%define major 2
%define libapogeee %mklibname apogeee %{major}
%define libapogeeu %mklibname apogeeu %{major}
%define devname %mklibname apogee -d

Summary:	Apogee Instruments Library
Name:		libapogee
Version:	2.2
Release:	17
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		http://indi.sourceforge.net/index.php/Main_Page
Source0:	http://downloads.sourceforge.net/indi/libapogee2_%{version}.tar.gz
Patch0:		libapogee-2.2.190-fix-lib.patch
Patch1:		libapogee2_2.2-fix-str-fmt.patch
Patch2:		apogee_sysio.patch
Patch3:		libapogee-2.2-curl-types.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libusb)

%description
Apogee Instruments Library

%package -n %{libapogeee}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libapogeee}
%{name} library

%package -n %{libapogeeu}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libapogeeu}
%{name} library

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libapogeee} = %{version}
Requires:	%{libapogeeu} = %{version}
%rename		libapogee-devel

%description  -n %{devname}
Files needed to build applications based on %{name}.

%prep
%setup -qn libapogee2-%{version}
%apply_patches

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libapogeee}
%{_libdir}/libapogeee.so.%{major}*

%files -n %{libapogeeu}
%{_libdir}/libapogeeu.so.%{major}*

%files -n %{devname}
%{_includedir}/libapogee
%{_libdir}/libapogeee.so
%{_libdir}/libapogeeu.so

