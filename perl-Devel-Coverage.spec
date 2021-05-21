%define		pdir	Devel
%define		pnam	Coverage
Summary:	Devel::Coverage - Perl module to perform coverage analysis
Summary(pl.UTF-8):	Devel::Coverage - moduł Perla do wykonywania analizy pokrycia
Name:		perl-Devel-Coverage
Version:	0.2
Release:	10
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a062ec329629e5d706a3543e30bdd338
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Coverage is a Perl module to perform coverage analysis. This
software is still very early-alpha quality. Use the tool "cover-perl"
to analyze the files that result from running your scripts with
coverage enabled.

%description -l pl.UTF-8
Moduł Perla Devel::Coverage służy do wykonywania analizy pokrycia.
Jest to wciąż oprogramowanie we wczesnej fazie rozwoju (alpha).
Narzędzie "cover-perl" służy do analizy plików będących wynikiem
działania skryptów z włączonym pokryciem.

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
%{_mandir}/man1/coverperl.1p*
%{_mandir}/man3/Devel::Coverage*.3pm*
