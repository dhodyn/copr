%define soname libfprint-tod-goodix-53xc

Name:           libfprint-2-tod1-goodix
Version:        0.0.6
Release:        %autorelease
Summary:        Goodix driver module for libfprint-2 Touch OEM Driver for XPS 13 9310
License:        NonFree
Group:          Hardware/Mobile
Source0:        http://dell.archive.canonical.com/updates/pool/public/libf/libfprint-2-tod1-goodix/libfprint-2-tod1-goodix_%{version}.orig.tar.gz
BuildRequires:  git
BuildRequires:  pkgconfig(udev)
Requires:       libfprint-tod
ExclusiveArch:  x86_64
Supplements:    modalias(usb:v27C6p538Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p533Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p530Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p5840d*dc*dsc*dp*ic*isc*ip*)

%description
This is user space driver for Goodix finger print module. Proprietary driver for the fingerprint reader on the Dell XPS 13 9310 - direct from Dell's Ubuntu repo. It should work for 27c6:538c, 27c6:533c, 27c6:530c, 27c6:5840.

%prep
git clone %{url}
cd libfprint-2-tod1-goodix

%build

%install
cd libfprint-2-tod1-goodix
install -dm 0755 %{buildroot}%{_udevrulesdir} %{buildroot}%{_libdir}/libfprint-2/tod-1/
install -m 0644 lib/udev/rules.d/60-%{name}.rules %{buildroot}%{_udevrulesdir}/60-%{name}.rules
install -m 0755 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/%{soname}-%{version}.so %{buildroot}%{_libdir}/libfprint-2/tod-1/%{soname}-%{version}.so

%files
%{_udevrulesdir}/60-%{name}.rules
%dir %{_libdir}/libfprint-2
%dir %{_libdir}/libfprint-2/tod-1
%{_libdir}/libfprint-2/tod-1/%{soname}-%{version}.so

%changelog
%autochangelog
