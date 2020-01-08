#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Email-Date-Format
Version  : 1.005
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-Format-1.005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-Format-1.005.tar.gz
Summary  : 'produce RFC 2822 date strings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Email-Date-Format-license = %{version}-%{release}
Requires: perl-Email-Date-Format-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Email-Date-Format,
version 1.005:
produce RFC 2822 date strings

%package dev
Summary: dev components for the perl-Email-Date-Format package.
Group: Development
Provides: perl-Email-Date-Format-devel = %{version}-%{release}
Requires: perl-Email-Date-Format = %{version}-%{release}

%description dev
dev components for the perl-Email-Date-Format package.


%package license
Summary: license components for the perl-Email-Date-Format package.
Group: Default

%description license
license components for the perl-Email-Date-Format package.


%package perl
Summary: perl components for the perl-Email-Date-Format package.
Group: Default
Requires: perl-Email-Date-Format = %{version}-%{release}

%description perl
perl components for the perl-Email-Date-Format package.


%prep
%setup -q -n Email-Date-Format-1.005
cd %{_builddir}/Email-Date-Format-1.005

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Email-Date-Format
cp %{_builddir}/Email-Date-Format-1.005/LICENSE %{buildroot}/usr/share/package-licenses/perl-Email-Date-Format/b909b85a91cf83dce7e3bbe82457806d7c0f8146
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::Date::Format.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Email-Date-Format/b909b85a91cf83dce7e3bbe82457806d7c0f8146

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Email/Date/Format.pm
