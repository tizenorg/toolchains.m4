Name:       m4
Summary:    The GNU macro processor
Version:    1.4.14
Release:    %{?release_prefix:%{release_prefix}.}1.8.%{?dist}%{!?dist:tizen}
VCS:        external/m4#submit/trunk/20121019.112917-0-g2f54725f6671008a2a6c84fd167bda09b35e306d
Group:      Applications/Text
License:    GPLv3+
URL:        http://www.gnu.org/software/m4/
Source0:    ftp://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz
Patch0:     m4-1.4.14-include.patch
Patch1:	    m4_gets.patch

%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

Install m4 if you need a macro processor.




%prep
%setup -q -n %{name}-%{version}

# m4-1.4.14-include.patch
%patch0 -p1
%patch1 -p1

%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%docs_package 

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/m4


%changelog
* Mon Sep 16 2013 UkJung Kim <ujkim@samsung.com> - submit/trunk/20121019.112917 
- PROJECT: external/m4
- COMMIT_ID: 2f54725f6671008a2a6c84fd167bda09b35e306d
- PATCHSET_REVISION: 2f54725f6671008a2a6c84fd167bda09b35e306d
- CHANGE_OWNER: \"UkJung Kim\" <ujkim@samsung.com>
- PATCHSET_UPLOADER: \"UkJung Kim\" <ujkim@samsung.com>
- CHANGE_URL: http://slp-info.sec.samsung.net/gerrit/103472
- PATCHSET_REVISION: 2f54725f6671008a2a6c84fd167bda09b35e306d
- TAGGER: UkJung Kim <ujkim@samsung.com>
- Gerrit patchset approval info:
- UkJung Kim <ujkim@samsung.com> Verified : 1
- Newton Lee <newton.lee@samsung.com> Code Review : 2
- CHANGE_SUBJECT: Initial commit
- [Version] 1.4.14
- [Project] GT-I8800
- [Title] Initial commit
- [BinType] PDA
- [Customer] Open
- [Issue#] N/A
- [Problem] N/A
- [Cause] N/A
- [Solution]
- [Team] SCM
- [Developer] UkJung Kim <ujkim@samsung.com>
- [Request] N/A
- [Horizontal expansion] N/A
- [SCMRequest] N/A
* Fri Jul 29 2011 Junfeng Dong <junfeng.dong@intel.com> -1.4.14
- Import 1.4.14 for SLP.
* Thu Apr  7 2011 Junfeng Dong <junfeng.dong@intel.com> - 1.4.16
- Update to 1.4.16
* Thu Dec 10 2009 Austin Zhang <austin.zhang@intel.com> - 1.4.13
- Remove unset LD_AS_NEEDED
* Thu Sep 24 2009 Anas Nashif <anas.nashif@intel.com> - 1.4.13
- Remove %%_infodir/dir, again
* Thu Sep 24 2009 Anas Nashif <anas.nashif@intel.com> - 1.4.13
- Fixed file list
* Sat Sep 19 2009 Anas Nashif <anas.nashif@intel.com> - 1.4.13
- Dont install infodir
* Mon Aug 17 2009 Austin Zhang <austin.zhang@intel.com> 1.4.13
- Update to version 1.4.13
* Thu Jan  8 2009 Anas Nashif <anas.nashif@intel.com> 1.4.12
- Update to version 1.4.12
* Thu Dec 18 2008 Arjan van de Ven <arjan@linux.intel.com> 1.4.10
- Use standard specfile
* Fri Sep 12 2008 Yi Yang <yi.y.yang@intel.com> 1.4.10
- Remove installation warnings of info files
* Wed Jul 23 2008 Xu Li <xu.li@intel.com>
- add %%doc to man/info in %%files
