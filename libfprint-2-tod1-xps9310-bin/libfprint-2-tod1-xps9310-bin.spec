Name:           libfprint-2-tod1-xps9310-bin

Version:        0.0.6
Release:        1%{?dist}
Summary:        Proprietary driver for the fingerprint reader on the Dell XPS 13 9310 - direct from Dell's Ubuntu repo

License:        custom
URL:            https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-goodix/+git/libfprint-2-tod1-goodix/
Source0:        git+https://git.launchpad.net/~oem-solutions-engineers/libfprint-2-tod1-goodix/+git/libfprint-2-tod1-goodix/#branch=droped-lp1880058

BuildRequires:  libfprint-tod
BuildRequires:  git

%description
Proprietary driver for the fingerprint reader on the Dell XPS 13 9310 - direct from Dell's Ubuntu repo

%prep
%autosetup -S git -n libfprint-2-tod1-xps9310-bin-v%{version}

%build
sed -n -r '/Shenzhen/,/^\s*$/p' debian/copyright > LICENSE
if [[ ! -s LICENSE ]]; then
    cp debian/copyright LICENSE
fi

%install
install -dm 755 %{buildroot}/usr/lib/libfprint-2/tod-1/
install -dm 755 %{buildroot}/usr/lib/udev/rules.d/
install -Dm 644 LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE
install -Dm 755 /usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-tod-goodix-53xc-%{version}.so %{buildroot}/usr/lib/libfprint-2/tod-1/
install -Dm 755 /lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules %{buildroot}/usr/lib/udev/rules.d/

%files
%license LICENSE
/usr/lib/libfprint-2/tod-1/libfprint-tod-goodix-53xc-*.so
/usr/lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules

%changelog
* Tue Apr 04 2021 Navneet Dhody <navneet.dhody@gmail.com> - 0.0.6-1
- First release

