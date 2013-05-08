Name:			rasdaemon
Version:		0.2.0
Release:		1%{?dist}
Summary:		Utility to receive RAS error tracings
Group:			Applications/System
License:		GPLv2
URL:			https://git.fedorahosted.org/git/rasdaemon.git
Source0:		https://git.fedorahosted.org/cgit/rasdaemon.git/snapshot/%{name}-%{version}.tar.bz2
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}
Requires:		hwdata, dmidecode
ExclusiveArch:		%{ix86} x86_64
Requires(post):		systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units

%description
%{name} is a RAS (Reliability, Availability and Serviceability) logging tool.
It currently records memory errors, using the EDAC tracing events.
EDAC is drivers in the Linux kernel that handle detection of ECC errors
from memory controllers for most chipsets on i386 and x86_64 architectures.
EDAC drivers for other architectures like arm also exists.
This userspace component consists of an init script which makes sure
EDAC drivers and DIMM labels are loaded at system startup, as well as
an utility for reporting current error counts from the EDAC sysfs files.

%prep
%setup -q

%build
autoreconf -vfi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D -p -m 0644 misc/rasdaemon.service $RPM_BUILD_ROOT%{_unitdir}/rasdaemon.service
install -D -p -m 0644 misc/ras-mc-ctl.service $RPM_BUILD_ROOT%{_unitdir}/ras-mc-ctl.service
rm %{buildroot}/usr/include/*.h

%files
%doc AUTHORS ChangeLog INSTALL COPYING README TODO
%{_sbindir}/rasdaemon
%{_sbindir}/ras-mc-ctl
%{_mandir}/*/*
%{_unitdir}/*.service

%changelog
* Wed May  8 2013 Mauro Carvalho Chehab <mchehab@redhat.com> 0.2.0.fc19
- Package created

