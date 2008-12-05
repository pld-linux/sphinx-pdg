
# there are sphinx.spec, sphinx2.spec...  Sphinx.spec is too confusing
# therefore the name for this package is sphinx-pdg (pdg - python
# documentation generator)
Summary:	Python documentation generator
Name:		sphinx-pdg
Version:	0.5
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
# Source0-md5:	55a33cc13b5096c8763cd4a933b30ddc
URL:		http://pypi.python.org/pypi/Sphinx
Requires:	python-docutils >= 0.5
Requires:	python-jinja >= 1.1
Requires:	python-pygments >= 0.11.1
BuildRequires:	python-devel
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
