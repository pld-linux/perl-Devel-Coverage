%include	/usr/lib/rpm/macros.perl
Summary:	Devel-Coverage perl module
Summary(pl):	Modu� perla Devel-Coverage
Name:		perl-Devel-Coverage
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-Coverage-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Storable
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Storable
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-Coverage - perl module to perform coverage analysis.

%description -l pl
Modu� perla Devel-Coverage.

%prep
%setup -q -n Devel-Coverage-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/Coverage
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
	ChangeLog README ToDo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,ToDo}.gz
%attr(755,root,root) %{_bindir}/coverperl

%{perl_sitelib}/Devel/Coverage.pm
%{perl_sitelib}/Devel/Coverage
%{perl_sitearch}/auto/Devel/Coverage

%{_mandir}/man[13]/*
