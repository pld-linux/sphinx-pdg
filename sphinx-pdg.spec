Summary:	Python documentation generator
Name:		sphinx-pdg
Version:	0.4.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
# Source0-md5:	b3c17f1b5be0b76c373a2474488f1662
URL:		http://pypi.python.org/pypi/Sphinx
#BuildRequires:	python-devel
#BuildRequires:	python-pygtk-gtk >= 2.8.4
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources), written by Georg Brandl. It was
originally created to translate the new Python documentation, but has now
been cleaned up in the hope that it will be useful to many other projects.

%prep
%setup -q -n Sphinx-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

%{__python} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README PKG-INFO TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/sphinx
%{py_sitescriptdir}/Sphinx*egg*
#%{_desktopdir}/%{name}.desktop
#%{_pixmapsdir}/*.png
