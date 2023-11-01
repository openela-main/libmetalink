Name:		libmetalink
Version:	0.1.3
Release:	7%{?dist}
Summary:	Metalink library written in C
Group:		System Environment/Libraries
License:	MIT
URL:		https://launchpad.net/libmetalink
Source0:	https://launchpad.net/libmetalink/trunk/%{name}-%{version}/+download/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	gcc
BuildRequires:	git
BuildRequires:	expat-devel
BuildRequires:	CUnit-devel

Patch0:  0001-fix-covscan-issues.patch

%description
libmetalink is a Metalink C library. It adds Metalink functionality such as
parsing Metalink XML files to programs written in C.

%package	devel
Summary:	Files needed for developing with %{name}
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Files needed for building applications with libmetalink.

%prep
%autosetup -S git

%build
%configure --disable-static
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name *.la -exec rm {} \;

%ldconfig_scriptlets

%files
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README 
%{_libdir}/libmetalink.so.*


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/metalink/
%{_includedir}/metalink/metalink_error.h
%{_includedir}/metalink/metalink.h
%{_includedir}/metalink/metalink_parser.h
%{_includedir}/metalink/metalink_types.h
%{_includedir}/metalink/metalinkver.h
%{_libdir}/libmetalink.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*


%changelog
* Tue Jul 24 2018 Martin Sehnoutka <msehnout@redhat.com> - 0.1.3-7
- Resolves: #1606986 Fix issues found by covscan

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.3-5
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Alejandro Alvarez <aalvarez@cern.ch> - 0.1.3-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 0.1.2-6
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 13 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.1.2-3
- Added BuildRequires: CUnit-devel
- Added %%check section
- Removed %%defattr
- Moved man pages to devel package. There is no need for -doc

* Mon Jun 10 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.1.2-2
- Escaped macros in changelog
- Changed packages summaries
- Renamed -docs to -doc, and changed its group to Documentation
- Fixed -devel dependencies
- Removed -docs dependency on the main package
- All header files specified explicitly

* Mon Apr 22 2013 Alejandro Alvarez <aalvarez@cern.ch> - 0.1.2-1
- Updated for new upstream release
- Man pages moved to libmetalink-docs package

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Ant Bryan <anthonybryan at gmail.com> - 0.0.3-4
- Remove Provides: libmetalink-static = %%{version}-%%{release}

* Tue May 06 2009 Ant Bryan <anthonybryan at gmail.com> - 0.0.3-3
- Use %%{_docdir} instead of /usr/share/doc
- Own /usr/include/metalink

* Wed Apr 29 2009 Ant Bryan <anthonybryan at gmail.com> - 0.0.3-2
- Incorporate suggested changes: remove .la files, --disable static.

* Mon Apr 27 2009 Ant Bryan <anthonybryan at gmail.com> - 0.0.3-1
- Initial package, 0.0.3.

