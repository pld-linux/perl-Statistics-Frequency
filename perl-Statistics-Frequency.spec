#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Statistics
%define		pnam	Frequency
%include	/usr/lib/rpm/macros.perl
Summary:	Statistics::Frequency - simple counting of elements
Summary(pl.UTF-8):	Statistics::Frequency - proste liczenie elementów
Name:		perl-Statistics-Frequency
Version:	0.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b67d54fb3db4787f170f3700e5362417
URL:		http://search.cpan.org/dist/Statistics-Frequency/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small module for a small but very common task: counting
things, in another words, frequencies. Sure, you can $freq{$elem}++
yourself, but what if you need to normalize the frequencies, or what
if you have several frequencies you want to combine?
Statistics::Frequency to rescue.

%description -l pl.UTF-8
Jest to mały moduł do małego, ale bardzo popularnego zadania:
zliczania różnych rzeczy, a innymi słowy, częstotliwości. Oczywiście
można robić samemu $freq{$elem}++, ale jeśli potrzebna jest
normalizacja częstotliwości, albo kombinacja kilku częstotliwości?
Moduł Statistics::Frequency jest ratunkiem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
#perl Makefile.PL # it's broken: sixsth line prevents from generating man page
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Statistics::Frequency")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
