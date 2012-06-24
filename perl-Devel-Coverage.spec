%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Coverage
Summary:	Devel::Coverage perl module
Summary(pl):	Modu� perla Devel::Coverage
Name:		perl-Devel-Coverage
Version:	0.2
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Storable
Requires:	perl-Storable
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Coverage - perl module to perform coverage analysis.

%description -l pl
Modu� perla Devel::Coverage.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README ToDo
%attr(755,root,root) %{_bindir}/coverperl
%{perl_sitelib}/Devel/Coverage.pm
%{perl_sitelib}/Devel/Coverage
%{_mandir}/man[13]/*
