# Conditional build:
%bcond_without	tests	# unit tests

%define		module	zstandard
Summary:	Zstandard bindings for Python
Name:		python3-%{module}
Version:	0.22.0
Release:	3
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	224e2e0d5d1f0e8be28aa31c802d1543
URL:		https://github.com/indygreg/python-zstandard
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
#BuildRequires:	python3-
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides Python bindings for interfacing with the
Zstandard compression library. A C extension and CFFI interface are
provided.

%prep
%setup -q -n %{module}-%{version}

%build

%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/*.pyi
%{py3_sitedir}/%{module}/py.typed
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
