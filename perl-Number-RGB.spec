%define upstream_name    Number-RGB
%define upstream_version 1.2

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Manipulate RGB Tuples
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Number/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Attribute::Handlers)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
This module creates RGB tuple objects and overloads their operators to make
RGB math easier. An attribute is also exported to the caller to make
construction shorter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%{make}

%check
# fails due to new attribute::handler
# cf http://rt.cpan.org/Public/Bug/Display.html?id=41394
#%{make} test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.200.0-2mdv2011.0
+ Revision: 655147
- rebuild for updated spec-helper

* Sun Aug 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 419895
- import perl-Number-RGB


* Sun Aug 23 2009 cpan2dist 1.2-1mdv
- initial mdv release, generated with cpan2dist
