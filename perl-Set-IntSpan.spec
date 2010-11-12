%define upstream_name    Set-IntSpan
%define upstream_version 1.16

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Manage sets of integers
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Set/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Set/IntSpan.pm
%{_mandir}/*/*
