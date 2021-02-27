# there are sphinx.spec, sphinx2.spec...  Sphinx.spec is too confusing
# therefore the name for this package is sphinx-pdg (pdg - python
# documentation generator)
# NOTE: for last python2 version see python-Sphinx.spec

#
# Conditional build:
%bcond_without	doc		# documentation
%bcond_with	tests		# unit tests (some need network)

Summary:	Sphinx - Python documentation generator
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona
Name:		sphinx-pdg
Version:	3.4.3
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/Sphinx/
Source0:	https://files.pythonhosted.org/packages/source/S/Sphinx/Sphinx-%{version}.tar.gz
# Source0-md5:	80c5176104fe0cfbd1a8430b6da308b4
Patch0:		float-ver.patch
URL:		http://www.sphinx-doc.org/
%if %{with tests} && %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	python3-babel >= 1.3
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools >= 1:7.0
%if %{with tests}
BuildRequires:	python3-Cython
BuildRequires:	python3-alabaster >= 0.7
BuildRequires:	python3-alabaster < 0.8
BuildRequires:	python3-docutils >= 0.12
# for lint only (mypy)
#BuildRequires:	python3-docutils-stubs
# for lint, not run by pytest
#BuildRequires:	python3-flake8 >= 3.5.0
BuildRequires:	python3-html5lib
# for lint
#BuildRequires:	python3-isort
BuildRequires:	python3-imagesize
BuildRequires:	python3-jinja2 >= 2.3
# for lint only, not run by pytest
#BuildRequires:	python3-mypy >= 0.790
BuildRequires:	python3-packaging
BuildRequires:	python3-pygments >= 2.0
BuildRequires:	python3-pytest >= 3.0
# for coverage tests only
#BuildRequires:	python3-pytest-cov
BuildRequires:	python3-requests >= 2.5.0
BuildRequires:	python3-six >= 1.5
BuildRequires:	python3-snowballstemmer >= 1.1
BuildRequires:	python3-sphinxcontrib-applehelp
BuildRequires:	python3-sphinxcontrib-devhelp
BuildRequires:	python3-sphinxcontrib-jsmath
BuildRequires:	python3-sphinxcontrib-htmlhelp
BuildRequires:	python3-sphinxcontrib-serializinghtml
BuildRequires:	python3-sphinxcontrib-qthelp
%if "%{py3_ver}" < "3.8"
BuildRequires:	python3-typed_ast
%endif
%endif
%if %{with doc}
BuildRequires:	python3-sphinxcontrib-applehelp
BuildRequires:	python3-sphinxcontrib-devhelp
BuildRequires:	python3-sphinxcontrib-htmlhelp
BuildRequires:	python3-sphinxcontrib-qthelp
BuildRequires:	python3-sphinxcontrib-serializinghtml
BuildRequires:	python3-sphinxcontrib-websupport
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with tests}
# for test_build_latex.py (disabled now)
#BuildRequires:	texlive-luatex
#BuildRequires:	texlive-xetex
%endif
Provides:	sphinx-pdg-3 = %{version}-%{release}
Requires:	python3-Sphinx = %{version}-%{release}
Obsoletes:	sphinx-pdg-3 < 3
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

%package -n python3-Sphinx
Summary:	Sphinx Python documentation generator (Python 3.x modules)
Summary(pl.UTF-8):	Sphinx - narzędzie do tworzenia dokumentacji dla Pythona (moduły Pythona 3.x)
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.5
Requires:	python3-devel-tools
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

# needs python-babel with at least de,en,ja locales installed
%{__rm} tests/test_util_i18n.py
# requires various latex variants, fails in a ways difficult to diagnose
%{__rm} tests/test_build_latex.py

%build
%py3_build
%{__rm} -r sphinx/__pycache__

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C doc -j1 html man
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r sphinx/__pycache__

for f in $RPM_BUILD_ROOT%{_bindir}/*; do
	%{__mv} "${f}" "${f}-3"
	ln -sf "$(basename "$f")-3" "$f"
done

%if %{with doc}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/_build/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
for f in $RPM_BUILD_ROOT%{_mandir}/man1/*.1 ; do
	ln "$f" $RPM_BUILD_ROOT%{_mandir}/man1/$(basename "$f" .1)-3.1
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
%attr(755,root,root) %{_bindir}/sphinx-apidoc-3
%attr(755,root,root) %{_bindir}/sphinx-autogen-3
%attr(755,root,root) %{_bindir}/sphinx-build-3
%attr(755,root,root) %{_bindir}/sphinx-quickstart-3
%if %{with doc}
%{_mandir}/man1/sphinx-all.1*
%{_mandir}/man1/sphinx-apidoc.1*
%{_mandir}/man1/sphinx-autogen.1*
%{_mandir}/man1/sphinx-build.1*
%{_mandir}/man1/sphinx-quickstart.1*
%{_mandir}/man1/sphinx-all-3.1*
%{_mandir}/man1/sphinx-apidoc-3.1*
%{_mandir}/man1/sphinx-autogen-3.1*
%{_mandir}/man1/sphinx-build-3.1*
%{_mandir}/man1/sphinx-quickstart-3.1*
%endif

%files -n python3-Sphinx
%defattr(644,root,root,755)
%doc AUTHORS CHANGES EXAMPLES LICENSE README.rst
%{py3_sitescriptdir}/sphinx
%{py3_sitescriptdir}/Sphinx-%{version}-py*.egg-info

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/_build/html/{_downloads,_images,_modules,_static,development,extdev,man,usage,*.html,*.js}
%endif
