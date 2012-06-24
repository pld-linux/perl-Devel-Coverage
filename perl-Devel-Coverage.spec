%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Coverage
Summary:	Devel::Coverage - Perl module to perform coverage analysis
Summary(pl):	Devel::Coverage - modu� Perla do wykonywania analizy pokrycia
Name:		perl-Devel-Coverage
Version:	0.2
Release:	7
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a062ec329629e5d706a3543e30bdd338
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Storable
Requires:	perl-Storable
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Coverage is a Perl module to perform coverage analysis. This
software is still very early-alpha quality. Use the tool "cover-perl"
to analyze the files that result from running your scripts with
coverage enabled.

%description -l pl
Modu� Perla Devel::Coverage s�u�y do wykonywania analizy pokrycia.
Jest to wci�� oprogramowania we wczwsnej fazie rozwoju (alpha).
Narz�dzie "cover-perl" s�u�y do analizy plik�w b�d�cych wynikiem
dzia�ania skrypt�w z w��czonym pokryciem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README ToDo
%attr(755,root,root) %{_bindir}/coverperl
%{perl_vendorlib}/Devel/Coverage.pm
%{perl_vendorlib}/Devel/Coverage
%{_mandir}/man[13]/*
