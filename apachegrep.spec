%define name apachegrep
%define version 0.3
%define release %mkrel 4

Summary: A grep tool for apache log files 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://switch.dl.sourceforge.net/sourceforge/apachegrep/%{name}-%{version}.tar.bz2
License: GPL
Group: File tools
Url: http://apachegrep.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Patch0: apachegrep-zcat.patch
BuildArch: noarch
Requires: gzip, bzip2

%description
apachegrep is a perl program to help webmasters go through their apache logs
and try to pullout various bits of information.
Built in the spirit of unix tools, it's designed to be used standalone or 
as part of a pipeline of tools to pore over common (or combined) logs and 
print out entire lines, specified fields or a simple count of matching lines.
You specify what fields you want and what regular expression you want applied
to that field.

It supports gzipped and bzipped log files.

%prep
%setup -q
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%{_mandir}/man1
mkdir -p %buildroot/%{_bindir}
install -m 755 apachegrep %buildroot/%{_bindir}
install -m 644 apachegrep.1 %buildroot/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc INSTALL CHANGELOG LICENSE README TODO 
%{_bindir}/apachegrep
%{_mandir}/man1/*





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-4mdv2011.0
+ Revision: 616564
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.3-3mdv2010.0
+ Revision: 423978
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 0.3-2mdv2009.0
+ Revision: 226156
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.3-1mdv2008.1
+ Revision: 135820
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 27 2007 Erwan Velu <erwan@mandriva.org> 0.3-1mdv2007.1
+ Revision: 148903
- Import apachegrep

