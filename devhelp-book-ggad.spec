Summary:	DevHelp book: ggad
Summary(pl):	Ksi±¿ka do DevHelpa o ggad
Name:		devhelp-book-ggad
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/ggad.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share/devhelp

%description
DevHelp book about ggad.

%description -l pl
Ksi±¿ka do DevHelpa o ggad.

%prep
%setup -q -c -n ggad

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/ggad/figures,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/ggad.devhelp
install book/figures/* $RPM_BUILD_ROOT%{_prefix}/books/ggad/figures
install book/*.html $RPM_BUILD_ROOT%{_prefix}/books/ggad

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
