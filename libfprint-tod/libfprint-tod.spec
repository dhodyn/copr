%define install_fp_udev_hwdb 0

Name:           libfprint-tod
 
Version:        1.94.9+tod1
Release:        %autorelease
Summary:        Toolkit for fingerprint scanner (TOD version)
 
License:        LGPLv2+
URL:            http://www.freedesktop.org/wiki/Software/fprint/libfprint
Source0:        https://gitlab.freedesktop.org/3v1n0/libfprint/-/archive/v%{version}/libfprint-v%{version}.tar.gz
ExcludeArch:    s390 s390x
 
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gusb) >= 0.3.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  gtk-doc
BuildRequires:  libgudev-devel
# For the udev.pc to install the rules
BuildRequires:  systemd
BuildRequires:  gobject-introspection-devel
# For internal CI tests; umockdev 0.13.2 has an important locking fix
BuildRequires:  python3-cairo python3-gobject cairo-devel
BuildRequires:  umockdev >= 0.13.2
 
%description
libfprint-tod offers support for consumer fingerprint reader devices.
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
 
%prep
%autosetup -S git -n libfprint-v%{version}
 
%build
# Include the virtual image driver for integration tests
%meson \
        -Ddrivers=all \
	-Dinstalled-tests=false \
%if %{install_fp_udev_hwdb}
	-Dudev_hwdb=enabled \
%else
	-Dudev_hwdb=disabled \
%endif
	%{nil}
%meson_build
%install
%meson_install
%ldconfig_scriptlets
 
%files
%license COPYING
%doc NEWS THANKS AUTHORS README.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%if %{install_fp_udev_hwdb}
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%endif
%{_udevrulesdir}/70-libfprint-2.rules
 
%files devel
%doc HACKING.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfprint-2.pc
%{_libdir}/pkgconfig/libfprint-2-tod-1.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libfprint-2/
 
%changelog
%autochangelog
