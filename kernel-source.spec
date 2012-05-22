#
# Spec file generated by kdist version v0.4-28-gcada
#
%define name		kernel-source
%define version		3.4.0
%define src_uname_r	3.4.0-2
%define source_release	2
%define build_release	0%{nil}
%define archive		kernel-source-3.4.0-2

%define build_srpm	1
%define no_source	0

%define _source_path	/usr/src/linux-%{src_uname_r}
%if %no_source
%define source_path	%{_source_path}/
%else
%define source_path	./
%endif

Name:			%{name}
Summary:		Linux kernel source files
Version:		%{version}
Release:		%mkrel %{source_release}
License:		GPLv2
Group:			System/Kernel and hardware
URL:			http://www.kernel.org
Source0:		%{archive}.tar.bz2
Buildarch:		noarch
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
AutoReqProv:		no

%define debug_package	%{nil}
%define __check_files	%{nil}

%description
This package provides the whole kernel source files.

%install
mkdir -p %{buildroot}%{_source_path}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{_source_path}

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
%{_source_path}

%changelog
* Tue May 22 2012 Franck Bui <franck.bui@mandriva.com> 
  + Mandriva Release v3.4-2
  + radio-rtrack: fix build error (implicit declaration of function 'kzalloc')
