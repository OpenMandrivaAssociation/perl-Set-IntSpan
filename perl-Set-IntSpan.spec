%define module  Set-IntSpan
%define name    perl-%{module}
%define version 1.13
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Manage sets of integers
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Set/%{module}-%{version}.tar.gz
Buildarch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

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
