# there are sphinx.spec, sphinx2.spec...  Sphinx.spec is too confusing
# therefore the name for this package is sphinx-pdg (pdg - python
# documentation generator)
#
# Conditional build:
%bcond_without	python2		# CPython 2.x version
%bcond_without	python3		# CPython 3.x version
%bcond_without	python3_default	# Use Python 3.x for easy_install executable

Summary:	Sphinx - Python documentation generator
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona
Name:		sphinx-pdg
Version:	1.3.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/pypi/Sphinx
Source0:	https://pypi.python.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
# Source0-md5:	3800ffa038a1eedb5139f9c247e7ee2f
URL:		http://sphinx.pocoo.org/
%if %{with python2}
BuildRequires:	python-babel >= 1.3
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools >= 7.0
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-babel >= 1.3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools >= 7.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python3_default}
Requires:	sphinx-pdg-3 = %{version}-%{release}
%else
Requires:	sphinx-pdg-2 = %{version}-%{release}
%endif
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

%package 2
Summary:	Sphinx Python documentation generator (Python 2 version)
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (wersja dla Pythona 2)
Group:		Development/Languages/Python
Requires:	python-Sphinx = %{version}-%{release}
Conflicts:	sphinx-pdg < 1.3.2

%description 2
Sphinx is a tool that makes it easy to create intelligent and
beautiful documentation for Python projects (or other documents
consisting of multiple reStructuredText sources), written by Georg
Brandl. It was originally created to translate the new Python
documentation, but has now been cleaned up in the hope that it will be
useful to many other projects.

%description 2 -l pl.UTF-8
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
Conflicts:	sphinx-pdg < 1.3.2

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
Requires:	python-modules
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

%build
%if %{with python2}
%py_build
%{__rm} sphinx/__init__.pyc
%endif

%if %{with python3}
%py3_build
%{__rm} -r sphinx/__pycache__
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%{__rm} sphinx/__init__.pyc
%py_postclean

for f in $RPM_BUILD_ROOT%{_bindir}/*; do
	%{__mv} "${f}" "${f}-2"
done
%endif

%if %{with python3}
%py3_install
%{__rm} -r sphinx/__pycache__

for f in $RPM_BUILD_ROOT%{_bindir}/*; do
	[ "${f%%-2}" == "$f" ] || continue
	%{__mv} "${f}" "${f}-3"
done
%endif

%if %{with python3_default}
for f in $RPM_BUILD_ROOT%{_bindir}/*-3; do
	ln -sf "$(basename "$f")" "${f%%-3}"
done
%else
for f in $RPM_BUILD_ROOT%{_bindir}/*-2; do
	ln -sf "$(basename "$f")" "${f%%-2}"
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sphinx-apidoc
%attr(755,root,root) %{_bindir}/sphinx-autogen
%attr(755,root,root) %{_bindir}/sphinx-build
%attr(755,root,root) %{_bindir}/sphinx-quickstart

%if %{with python2}
%files 2
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE PKG-INFO README.rst
%attr(755,root,root) %{_bindir}/sphinx-apidoc-2
%attr(755,root,root) %{_bindir}/sphinx-autogen-2
%attr(755,root,root) %{_bindir}/sphinx-build-2
%attr(755,root,root) %{_bindir}/sphinx-quickstart-2
%endif

%if %{with python3}
%files 3
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE PKG-INFO README.rst
%attr(755,root,root) %{_bindir}/sphinx-apidoc-3
%attr(755,root,root) %{_bindir}/sphinx-autogen-3
%attr(755,root,root) %{_bindir}/sphinx-build-3
%attr(755,root,root) %{_bindir}/sphinx-quickstart-3
%endif

%if %{with python2}
%files -n python-Sphinx
%defattr(644,root,root,755)
%{py_sitescriptdir}/sphinx
%{py_sitescriptdir}/Sphinx-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-Sphinx
%defattr(644,root,root,755)
%{py3_sitescriptdir}/sphinx
%{py3_sitescriptdir}/Sphinx-%{version}-py*.egg-info
%endif
