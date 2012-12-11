%define upstream_name    Set-IntSpan
%define upstream_version 1.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Manage sets of integers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Set/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch: noarch

%description
Set::IntSpan manages sets of integers.  It is optimized for sets that
have long runs of consecutive integers.  These arise, for example, in
.newsrc files, which maintain lists of articles:

    alt.foo: 1-21,28,31
    alt.bar: 1-14192,14194,14196-14221

Sets are stored internally in a run-length coded form.  This provides
for both compact storage and efficient computation.  In particular,
set operations can be performed directly on the encoded
representation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Set/IntSpan.pm
%{_mandir}/*/*


%changelog
* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2011.0
+ Revision: 596643
- update to 1.16

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.140.0-1mdv2011.0
+ Revision: 552631
- update to 1.14

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.130.0-1mdv2010.0
+ Revision: 401610
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.13-2mdv2010.0
+ Revision: 375902
- rebuild

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 1.13-1mdv2010.0
+ Revision: 370912
- import perl-Set-IntSpan


