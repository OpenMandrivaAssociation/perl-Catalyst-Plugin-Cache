%define upstream_name    Catalyst-Plugin-Cache
%define upstream_version 0.12

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	4

Summary:	Choose a cache backend based on key regexes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.shadowcat.co.uk/catagits/Catalyst-Plugin-Cache
Source0:	https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Plugin-Cache-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(ok)

BuildArch: noarch

%description
This plugin gives you access to a variety of systems for caching data. It
allows you to use a very simple configuration API, while maintaining the
possibility of flexibility when you need it later.

Among its features are support for multiple backends, segmentation based on
component or controller, keyspace partitioning, and so more, in various
subsidiary plugins.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 658738
- rebuild for updated spec-helper

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 554158
- update to 0.10

* Mon Mar 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 515657
- update to 0.09

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 471410
- adding missing buildrequires:
- import perl-Catalyst-Plugin-Cache


* Sun Nov 29 2009 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

