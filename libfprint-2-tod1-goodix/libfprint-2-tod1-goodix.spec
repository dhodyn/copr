%define soname libfprint-tod-goodix-53xc

Name:           libfprint-2-tod1-goodix
Version:        0.0.6
Release:        2%{?dist}
Summary:        Goodix driver module for libfprint-2 Touch OEM Driver for XPS 13 9310
License:        NonFree
Group:          Hardware/Mobile
URL:            https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-goodix/+git/libfprint-2-tod1-goodix
BuildRequires:  git
BuildRequires:  pkgconfig(udev)
ExclusiveArch:  x86_64
Supplements:    modalias(usb:v27C6p538Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p533Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p530Cd*dc*dsc*dp*ic*isc*ip*)
Supplements:    modalias(usb:v27C6p5840d*dc*dsc*dp*ic*isc*ip*)

%description
This is user space driver for Goodix finger print module. Proprietary driver for the fingerprint reader on the Dell XPS 13 9310 - direct from Dell's Ubuntu repo.

%prep
git clone %{url}
cd libfprint-2-tod1-goodix

%build

%install
cd libfprint-2-tod1-goodix
install -dm 0755 %{buildroot}%{_udevrulesdir} %{buildroot}%{_libdir}/libfprint-2/tod-1/
install -m 0644 lib/udev/rules.d/60-%{name}.rules %{buildroot}%{_udevrulesdir}/60-%{name}.rules
install -m 0755 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/%soname-%{version}.so %{buildroot}%{_libdir}/libfprint-2/tod-1/%soname-%{version}.so

%files
%{_udevrulesdir}/60-%{name}.rules
%dir %{_libdir}/libfprint-2
%dir %{_libdir}/libfprint-2/tod-1
%{_libdir}/libfprint-2/tod-1/%soname-%{version}.so

%changelog
* Tue Mar 22 2021 Navneet Dhody <navneet.dhody@gmail.com> - 0.0.6-2
* Tue Apr 04 2021 Navneet Dhody <navneet.dhody@gmail.com> - 0.0.6-1
- First release
