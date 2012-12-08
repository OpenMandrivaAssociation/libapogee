Name:          libapogee
Summary:       Apogee Instruments Library
Version:       2.2
Release:       %mkrel 8
Url:           http://indi.sourceforge.net/index.php/Main_Page
License:       GPLv2+
Group:         Development/KDE and Qt
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       http://downloads.sourceforge.net/indi/libapogee2_%version.tar.gz
Patch0:        libapogee-2.2.190-fix-lib.patch
Patch1:        libapogee2_2.2-fix-str-fmt.patch
Patch2:        apogee_sysio.patch
Patch3:        libapogee-2.2-curl-types.patch
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
%patch2 -p1
%patch3 -p1

%build
%cmake
%make

%install
rm -rf "%{buildroot}"
%makeinstall_std -C build

%clean
rm -rf "%{buildroot}"


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2-6mdv2011.0
+ Revision: 660210
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-5mdv2011.0
+ Revision: 602519
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-4mdv2010.1
+ Revision: 520748
- rebuilt for 2010.1

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.2-3mdv2010.0
+ Revision: 455874
- rebuild for new curl SSL backend

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 2.2-2mdv2010.0
+ Revision: 449849
- remove sys/io.h include. useless for usb and breaks build on
  platforms without it (from Arnaud Patard)

* Wed May 20 2009 Funda Wang <fwang@mandriva.org> 2.2-1mdv2010.0
+ Revision: 377906
- fix str fmt

* Tue Nov 25 2008 Funda Wang <fwang@mandriva.org> 2.2-1mdv2009.1
+ Revision: 306532
- 2.2 final

* Wed Oct 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2.2-0.190.3mdv2009.1
+ Revision: 298354
- Enhance lib patch
- Fix lib install on x86_64
- import libapogee


