%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           twingly
Version:        1.0.0
Release:        %{?dist}
Summary:        Python Interface for Twingly Search API

Group:          Development/Libraries
License:        MIT
URL:            http://github.com/bearburger/twingly-search-api-python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       python >= 2.6,
BuildRequires:  python-setuptools


%description
This library provides a pure python interface for the Twingly Search API.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
chmod a-x README
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.md
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
- Initial package.