# there are sphinx.spec, sphinx2.spec...  Sphinx.spec is too confusing
# therefore the name for this package is sphinx-pdg (pdg - python
# documentation generator)
#
# Conditional build:
%bcond_without	python2		# CPython 2.x version
%bcond_without	python3		# CPython 3.x version
%bcond_without	python3_default	# Use Python 3.x for easy_install executable
%bcond_without	doc		# documentation
%bcond_with	tests		# unit tests (some fail on import of existing module???)

Summary:	Sphinx - Python documentation generator
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona
Name:		sphinx-pdg
# note: Sphinx 2+ doesn't support Python 2
Version:	1.8.5
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/Sphinx/
Source0:	https://files.pythonhosted.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
# Source0-md5:	554f7a4e752f48b2601e5ef5ab463346
Patch0:		float-ver.patch
Patch1:		%{name}-mock.patch
URL:		http://www.sphinx-doc.org/
%if %{with tests} && %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python-babel >= 1.3
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:7.0
%if %{with tests}
BuildRequires:	python-alabaster >= 0.7
BuildRequires:	python-alabaster < 0.8
BuildRequires:	python-docutils >= 0.11
BuildRequires:	python-enum34
# for style checks, not run by pytest
#BuildRequires:	python-flake8 >= 3.5.0
#BuildRequires:	python-flake8-import-order
BuildRequires:	python-html5lib
BuildRequires:	python-imagesize
BuildRequires:	python-jinja2 >= 2.3
BuildRequires:	python-mock
BuildRequires:	python-packaging
BuildRequires:	python-pygments >= 2.0
BuildRequires:	python-pytest >= 3.0
# for coverage tests only
#BuildRequires:	python-pytest-cov
BuildRequires:	python-requests >= 2.0.0
BuildRequires:	python-six >= 1.5
BuildRequires:	python-snowballstemmer >= 1.1
BuildRequires:	python-sphinxcontrib-websupport
BuildRequires:	python-typing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-babel >= 1.3
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools >= 1:7.0
%if %{with tests}
BuildRequires:	python3-alabaster >= 0.7
BuildRequires:	python3-alabaster < 0.8
BuildRequires:	python3-docutils >= 0.11
# for style checks, not run by pytest
#BuildRequires:	python3-flake8 >= 3.5.0
#BuildRequires:	python3-flake8-import-order
BuildRequires:	python3-html5lib
BuildRequires:	python3-imagesize
BuildRequires:	python3-jinja2 >= 2.3
# for type checks only, not run by pytest
#BuildRequires:	python3-mypy
BuildRequires:	python3-packaging
BuildRequires:	python3-pygments >= 2.0
BuildRequires:	python3-pytest >= 3.0
# for coverage tests only
#BuildRequires:	python3-pytest-cov
BuildRequires:	python3-requests >= 2.0.0
BuildRequires:	python3-six >= 1.5
BuildRequires:	python3-snowballstemmer >= 1.1
BuildRequires:	python3-sphinxcontrib-websupport
BuildRequires:	python3-typed_ast
%if "%{py3_ver}" < "3.5"
BuildRequires:	python3-typing
%endif
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with tests}
# for test_build_latex.py (disabled now)
#BuildRequires:	texlive-luatex
#BuildRequires:	texlive-xetex
%endif
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
Requires:	python-modules >= 1:2.7
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
Requires:	python3-modules >= 1:3.4
Conflicts:	sphinx-pdg-3 < 1.0.7-2

%description -n python3-Sphinx
Sphinx Python documentation generator (Python 3.x modules).

For command-line utilities, see sphinx-pdg-3 package.

%description -n python3-Sphinx -l pl.UTF-8
Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (moduły
Pythona 3.x).

Narzędzia działające z linii poleceń znajdują się w pakiecie
sphinx-pdg-3.

%package doc
Summary:	Documentation for Sphinx Python documentation generator
Summary(pl.UTF-8):	Dokumentacja do generatora dokumentacji pythonowej Sphinx
Group:		Documentation

%description doc
Documentation for Sphinx Python documentation generator.

%description doc -l pl.UTF-8
Dokumentacja do generatora dokumentacji pythonowej Sphinx.

%prep
%setup -q -n Sphinx-%{version}
%patch0 -p1
%patch1 -p1

# needs python-babel with at least de,en,ja locales installed
%{__rm} tests/test_util_i18n.py
# requires various latex variants, fails in a ways difficult to diagnose
%{__rm} tests/test_build_latex.py

%build
%if %{with python2}
%py_build
%{__rm} sphinx/__init__.pyc

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTHONPATH=$(pwd) \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build
%{__rm} -r sphinx/__pycache__

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C doc -j1 html man
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

%if "%{py3_ver}" >= "3.5"
# avoid python3egg(typing) dependency
%{__sed} -i -e '/^\[:python_version<"3\.5"]/,/^$/ d' $RPM_BUILD_ROOT%{py3_sitescriptdir}/Sphinx-%{version}-py*.egg-info/requires.txt
%endif
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

%if %{with doc}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/_build/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sphinx-apidoc
%attr(755,root,root) %{_bindir}/sphinx-autogen
%attr(755,root,root) %{_bindir}/sphinx-build
%attr(755,root,root) %{_bindir}/sphinx-quickstart
%if %{with doc}
%{_mandir}/man1/sphinx-all.1*
%{_mandir}/man1/sphinx-apidoc.1*
%{_mandir}/man1/sphinx-autogen.1*
%{_mandir}/man1/sphinx-build.1*
%{_mandir}/man1/sphinx-quickstart.1*
%endif

%if %{with python2}
%files 2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sphinx-apidoc-2
%attr(755,root,root) %{_bindir}/sphinx-autogen-2
%attr(755,root,root) %{_bindir}/sphinx-build-2
%attr(755,root,root) %{_bindir}/sphinx-quickstart-2
%endif

%if %{with python3}
%files 3
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sphinx-apidoc-3
%attr(755,root,root) %{_bindir}/sphinx-autogen-3
%attr(755,root,root) %{_bindir}/sphinx-build-3
%attr(755,root,root) %{_bindir}/sphinx-quickstart-3
%endif

%if %{with python2}
%files -n python-Sphinx
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE README.rst
%{py_sitescriptdir}/sphinx
%{py_sitescriptdir}/Sphinx-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-Sphinx
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE README.rst
%{py3_sitescriptdir}/sphinx
%{py3_sitescriptdir}/Sphinx-%{version}-py*.egg-info
%endif

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/{_images,_static,extdev,man,usage,web,*.html,*.js}
%endif
