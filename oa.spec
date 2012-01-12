Summary:	Toy to experiment with wave-forms
Summary(pl.UTF-8):	Zabawka do eksperymentowania z kształtami fal
Name:		oa
Version:	1.0.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://sed.free.fr/oa/%{name}-%{version}.tar.gz
# Source0-md5:	463eb8469b41d2c2ee14517b9ae8f92c
URL:		http://sed.free.fr/oa/
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Toy to experiment with wave-forms.

%description -l pl.UTF-8
Zabawka do eksperymentowania z kształtami fal.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install oa $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS README TODO
%attr(755,root,root) %{_bindir}/*
