%define upstream_name    Number-RGB
%define upstream_version 1.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Manipulate RGB Tuples
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Number/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Attribute::Handlers)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module creates RGB tuple objects and overloads their operators to make
RGB math easier. An attribute is also exported to the caller to make
construction shorter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
# fails due to new attribute::handler
# cf http://rt.cpan.org/Public/Bug/Display.html?id=41394
#%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


