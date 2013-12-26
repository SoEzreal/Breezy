Summary: A simple audio streaming tool 
%define version 1.0
License: GPLv3
Group: Productivity/Multimedia/Sound/Utilities 
Name: breezy
Prefix: /usr 
BuildRequires: gcc-c++ libpulse-devel gstreamer-0_10-devel
Requires: libpulse0 libgstreamer-0_10-0 gstreamer-plugins-good gstreamer-plugins-base
Release: 1 
Source: breezy-%{version}.tar.gz 
URL: http://ibm.com/developerworks/opensource/jikes 
Version: %{version} 
Buildroot: /tmp/breezyrpm 
%description 
Breezy is a simple audio streaming tool that lets you stream your local audio to remote machines.

%prep 
%setup -q

%build 
make

%install 
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root) 
/usr/bin/breezy
