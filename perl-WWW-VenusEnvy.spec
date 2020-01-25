#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_with	tests		# perform "make test" (uses network)
#
%define	pdir	WWW
%define	pnam	VenusEnvy
Summary:	WWW::VenusEnvy - Retrieve VenusEnvy comic strip images
Summary(pl.UTF-8):	WWW::VenusEnvy - pobieranie komiksu VenusEnvy
Name:		perl-WWW-VenusEnvy
Version:	1.10
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	15926752f71ac3e15a3513f2c2532633
URL:		http://search.cpan.org/dist/WWW-VenusEnvy/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module will download the latest VenusEnvy comic strip from the
Keenspace website and return a binary blob of the image, or write it
to disk.

%description -l pl.UTF-8
Ten moduł ściga ostatnią stronę komiksu VenusEnvy z serwisu WWW
Keepspace i zwraca obrazek w postaci binarnej lub zapisuje na dysku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
AUTOMATED_TESTING=1
export AUTOMATED_TESTING
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL TODO
%{perl_vendorlib}/WWW/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
