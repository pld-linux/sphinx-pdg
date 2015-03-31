# there are sphinx.spec, sphinx2.spec...  Sphinx.spec is too confusing
# therefore the name for this package is sphinx-pdg (pdg - python
# documentation generator)
Summary:	Sphinx - Python documentation generator
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona
Name:		sphinx-pdg
Version:	1.2.3
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
# Source0-md5:	a98c93124035b4cd7183604aec656cb3
Patch0:		sphinx-pdg-bug-1226.patch
URL:		http://sphinx.pocoo.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools > 7.0
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools > 7.0
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-Sphinx = %{version}-%{release}
Requires:	python-devel-tools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

%description -l pl.UTF-8
Sphinx to narzędzie ułatwiające tworzenie inteligentnej i ładnej
dokumentacji dla projektów w Pythonie (lub innych dokumentów
składających się z wielu źródeł w formacie reStructuredText), napisane
przez Georga Brandla. Pierwotnie powstało do tłumaczenia nowej
dokumentacji Pythona, ale potem zostało wyczyszczone w nadziei, że
będzie przydatne dla wielu innych projektów.

%package 3
Summary:	Sphinx Python documentation generator (Python 3 version)
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (wersja dla Pythona 3)
Group:		Development/Languages/Python
Requires:	python3-Sphinx = %{version}-%{release}

%description 3
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

%description 3 -l pl.UTF-8
Sphinx to narzędzie ułatwiające tworzenie inteligentnej i ładnej
dokumentacji dla projektów w Pythonie (lub innych dokumentów
składających się z wielu źródeł w formacie reStructuredText), napisane
przez Georga Brandla. Pierwotnie powstało do tłumaczenia nowej
dokumentacji Pythona, ale potem zostało wyczyszczone w nadziei, że
będzie przydatne dla wielu innych projektów.

%package -n python-Sphinx
Summary:	Sphinx Python documentation generator (Python 2.x modules)
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (moduły Pythona 2.x)
Group:		Development/Languages/Python
Requires:	python-setuptools > 7.0
Requires:	python-docutils >= 0.7
Requires:	python-jinja2 >= 2.3
Requires:	python-modules
Requires:	python-pygments >= 1.2
Conflicts:	sphinx-pdg < 1.0.7-2

%description -n python-Sphinx
Sphinx Python documentation generator (Python 2.x modules).

For command-line utilities, see sphinx-pdg package.

%description -n python-Sphinx -l pl.UTF-8
Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (moduły
Pythona 2.x).

Narzędzia działające z linii poleceń znajdują się w pakiecie
sphinx-pdg.

%package -n python3-Sphinx
Summary:	Sphinx Python documentation generator (Python 3.x modules)
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (moduły Pythona 3.x)
Group:		Development/Languages/Python
Requires:	python3-setuptools > 7.0
Requires:	python3-docutils >= 0.8
Requires:	python3-jinja2 >= 2.3
Requires:	python3-pygments >= 1.2
Conflicts:	sphinx-pdg-3 < 1.0.7-2

%description -n python3-Sphinx
Sphinx Python documentation generator (Python 3.x modules).

For command-line utilities, see sphinx-pdg-3 package.

%description -n python3-Sphinx -l pl.UTF-8
Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (moduły
Pythona 3.x).

Narzędzia działające z linii poleceń znajdują się w pakiecie
sphinx-pdg-3.

%prep
%setup -q -n Sphinx-%{version}
%patch0 -p1

%build
%{__python} setup.py build -b build-2
%{__rm} sphinx/__init__.pyc
%{__python3} setup.py build -b build-3
%{__rm} -r sphinx/__pycache__

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py build -b build-3 install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%{__rm} -r sphinx/__pycache__

for f in $RPM_BUILD_ROOT%{_bindir}/*; do
	mv "${f}" "${f}-3"
done

%{__python} setup.py build -b build-2 install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%{__rm} sphinx/__init__.pyc

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE PKG-INFO README.rst TODO
%attr(755,root,root) %{_bindir}/sphinx-autogen
%attr(755,root,root) %{_bindir}/sphinx-apidoc
%attr(755,root,root) %{_bindir}/sphinx-build
%attr(755,root,root) %{_bindir}/sphinx-quickstart

%files 3
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE PKG-INFO README.rst TODO
%attr(755,root,root) %{_bindir}/sphinx-autogen-3
%attr(755,root,root) %{_bindir}/sphinx-apidoc-3
%attr(755,root,root) %{_bindir}/sphinx-build-3
%attr(755,root,root) %{_bindir}/sphinx-quickstart-3

%files -n python-Sphinx
%defattr(644,root,root,755)
%{py_sitescriptdir}/sphinx
%{py_sitescriptdir}/Sphinx-%{version}-py*.egg-info

%files -n python3-Sphinx
%defattr(644,root,root,755)
%{py3_sitescriptdir}/sphinx
%{py3_sitescriptdir}/Sphinx-%{version}-py*.egg-info
