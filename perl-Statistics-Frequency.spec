%include	/usr/lib/rpm/macros.perl
%define	pdir	Statistics
%define	pnam	Frequency
Summary:	Statistics::Frequency - simple counting of elements
Summary(pl):	Statistics::Frequency - proste liczenie element�w
Name:		perl-%{pdir}-%{pnam}
Version:	0.03
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small module for a small but very common task: counting things,
in another words, frequencies.  Sure, you can $freq{$elem}++ yourself,
but what if you need to normalize the frequencies, or what if you have
several frequencies you want to combine?  Statistics::Frequency to rescue.

%description -l pl
Jest to ma�y modu� do ma�ego, ale bardzo popularnego zadania:
zliczania r�nych rzeczy, a innymi s�owy, cz�stotliwo�ci. Oczywi�cie
mo�na robi� samemu $freq{$elem}++, ale je�li potrzebna jest
normalizacja cz�stotliwo�ci, albo kombinacja kilku cz�stotliwo�ci?
Modu� Statistics::Frequency jest ratunkiem.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
#perl Makefile.PL # it's broken: sixsth line prevents from generating man page
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Statistics::Frequency")'
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
