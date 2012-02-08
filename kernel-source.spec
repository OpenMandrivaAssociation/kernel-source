#
# Spec file generated by kdist version v0.2
#
%define name		kernel-source
%define version		3.2.5

%define src_uname_r	3.2.5-1
%define uname_r		%{nil}

%define source_release	1
%define build_release	0%{nil}

%define archive		kernel-source-3.2.5-1

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
License:		GPL v2
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
* Wed Feb 08 2012 Franck Bui <franck.bui@mandriva.com> 
  + Mandriva Release v3.2.5-1
  + cpupower tools: add install target to the debug tools' makefiles
  + cpupower tools: allow to build debug tools in a separate directory too
  + cpupower tool: allow to build in a separate directory
  + cpupower tool: makefile: simplify the recipe used to generate cpupower.pot target
  + cpupower tool: remove use of undefined variables from the clean target of the top makefile
  + perf evsel: Fix an issue where perf report fails to show the proper percentage
  + perf tools: Fix prefix matching for kernel maps
  + perf tools: Fix perf stack to non executable on x86_64
  + perf doc: allow producing documentation in a specified output directory
  + ACPICA: Fix to allow region arguments to reference other scopes
  + Prevent BCMA from taking the BCM4313 device
  + Revert "staging: brcm80211: only enable brcmsmac if bcma is not set"
  + [overlayfs] fs: limit filesystem stacking depth
  + [overlayfs] overlay filesystem documentation
  + [overlayfs] implement show_options
  + [overlayfs] add statfs support
  + [overlayfs] overlay filesystem
  + [overlayfs] vfs: introduce clone_private_mount()
  + [overlayfs] vfs: export do_splice_direct() to modules
  + [overlayfs] vfs: add i_op->open()
  + [overlayfs] vfs: pass struct path to __dentry_open()
  + usb: ehci: make HC see up-to-date qh/qtd descriptor ASAP
  + Mandriva Linux boot logo.
  + media video pwc no ads in dmesg
  + media video pwc lie in proc usb devices
  + usb storage unusual_devs add id 2.6.37 buildfix
  + Change to usb storage of unusual_dev.
  + Add blacklist of usb hid modules
  + bluetooth hci_usb disable isoc transfers
  + sound alsa hda ad1884a hp dc model
  + Support a Bluetooth SCO.
  + Include kbuild export pci_ids
  + platform x86 add shuttle wmi driver
  + net netfilter psd 2.6.35 buildfix
  + ipt_psd: Mandriva changes
  + net netfilter psd
  + net netfilter IFWLOG 2.6.37 buildfix
  + IFWLOG netfilter: fix return value of ipt_IFWLOG_checkentry()
  + net netfilter IFWLOG 2.6.35 buildfix
  + netfilter ipt_IFWLOG: Mandriva changes
  + net netfilter IFWLOG
  + net sis190 fix list usage
  + kbuild compress kernel modules on installation
  + gpu drm mach64 3.2 buildfix
  + gpu drm mach64 2.6.39 buildfix
  + gpu drm mach64 2.6.37 buildfix
  + gpu drm mach64 2.6.36 buildfix
  + gpu drm mach64 fix for changed drm_ioctl
  + gpu drm mach64 fix for changed drm_pci_alloc
  + gpu drm mach64 2.6.31 buildfix
  + gpu drm mach64 fixes
  + gpu drm mach64
  + agp/intel: add new host bridge id for Q57 system
  + mpt scsi modules for VMWare's emulated
  + ppscsi: build fix for 2.6.39
  + scsi megaraid new sysfs name
  + scsi ppscsi mdvbz45393
  + scsi ppscsi update for scsi_data_buffer
  + scsi ppscsi sg helper update
  + scsi ppscsi_fixes
  + scsi ppscsi-2.6.2
  + acpi video add blacklist to use vendor driver
  + acpi processor M720SR limit to C2
  + CLEVO M360S acpi irq workaround
  + acpi add proc event regs
  + acpi dsdt initrd v0.9c fixes
  + acpi dsdt initrd v0.9c 2.6.28
  + UBUNTU: SAUCE: isapnp_init: make isa PNP scans occur async
  + pnp pnpbios off by default
  + PCI: Add ALI M5229 IDE comaptibility mode quirk
  + Card bus's PCI last bus
  + x86, cpufreq: set reasonable default for scaling_min_freq with p4-clockmod
  + x86 cpufreq speedstep dothan 3
  + default to "power_off" when SMP kernel is used on single processor machines
  + x86 boot video 80x25 if break
  + x86 pci toshiba equium a60 assign busses
  + kdist: make the config name part of the localversion
  + kdist: give a name to the config file
