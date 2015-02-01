Name:       m4
Summary:    The GNU macro processor
Version:    1.4.14
Release:    1
Group:      Applications/Text
License:    GPLv3+
URL:        http://www.gnu.org/software/m4/
Source0:    ftp://ftp.gnu.org/gnu/m4/m4-%{version}.tar.xz
Patch0:     m4-1.4.14-include.patch


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


