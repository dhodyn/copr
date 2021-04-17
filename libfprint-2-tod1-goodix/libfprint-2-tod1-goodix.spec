Name:           libfprint-2-tod1-goodix

Version:        0.0.6
Release:        1%{?dist}
Summary:        Proprietary driver for the Goodix fingerprint reader on the Dell XPS 13 - direct from Dell's Ubuntu repo

License:        custom
URL:            https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-goodix/+git/libfprint-2-tod1-goodix

BuildRequires:  git

%description
Proprietary driver for the Goodix fingerprint reader on the Dell XPS 13 - direct from Dell's Ubuntu repo

%prep
git clone %{url}
cd libfprint-2-tod1-goodix
git checkout 0.0.6-0ubuntu1_somerville1

%install
install -Dm 755 libfprint-2-tod1-goodix/usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-tod-goodix-53xc-%{version}.so %{buildroot}/usr/lib/libfprint-2/tod-1/
install -Dm 644 libfprint-2-tod1-goodix/lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules %{buildroot}/usr/lib/udev/rules.d/

%files
/usr/lib/libfprint-2/tod-1/libfprint-tod-goodix-53xc-%{version}.so
/usr/lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules

%changelog
* Tue Apr 04 2021 Navneet Dhody <navneet.dhody@gmail.com> - 0.0.6-1
- First release

