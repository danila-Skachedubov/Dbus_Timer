Name: dbustimer
Version: 0.1
Release: alt1

Summary: Display system time
License: GPLv3+
Group: Other
BuildArch: noarch

BuildRequires: rpm-build-python3
#Requires: python3-module-pydbus

Source0: %name-%version.tar

%description
This program displays notifications about the system time with a frequency of one hour.

%prep
%setup -q

%install

mkdir -p \
	%buildroot%python3_sitelibdir_noarch/%name/
install -Dm0644 script_dbus.py \
	%buildroot%python3_sitelibdir_noarch/%name/

mkdir -p \
	%buildroot%_sysconfdir/xdg/systemd/user/
cp script_dbus.timer script_dbus.service \
	%buildroot%_sysconfdir/xdg/systemd/user/
ls -l %buildroot%_sysconfdir/xdg/systemd/user/


%files
%python3_sitelibdir_noarch/%name/script_dbus.py
/etc/xdg/systemd/user/script_dbus.service
/etc/xdg/systemd/user/script_dbus.timer

%changelog
* Thu Apr 13 2023 Danila Skachedubov <dan@altlinux.org> 0.1-alt1
- Update system