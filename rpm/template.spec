%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-launch-testing
Version:        1.0.7
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS launch_testing package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-pytest
Requires:       ros-humble-ament-index-python
Requires:       ros-humble-launch
Requires:       ros-humble-launch-xml
Requires:       ros-humble-launch-yaml
Requires:       ros-humble-osrf-pycommon
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-copyright
BuildRequires:  ros-humble-ament-flake8
BuildRequires:  ros-humble-ament-pep257
BuildRequires:  ros-humble-launch
%endif

%description
A package to create tests which involve launch files and multiple processes.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Nov 25 2024 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.7-1
- Autogenerated by Bloom

* Fri May 17 2024 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.6-1
- Autogenerated by Bloom

* Fri Feb 16 2024 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.5-1
- Autogenerated by Bloom

* Tue Jan 10 2023 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.4-1
- Autogenerated by Bloom

* Tue Oct 18 2022 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.3-1
- Autogenerated by Bloom

* Wed May 11 2022 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.2-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.1-2
- Autogenerated by Bloom

* Wed Apr 13 2022 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.1-1
- Autogenerated by Bloom

* Tue Apr 12 2022 Aditya Pande <aditya.pande@openrobotics.org> - 1.0.0-1
- Autogenerated by Bloom

* Fri Apr 08 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.23.1-1
- Autogenerated by Bloom

* Wed Mar 30 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.23.0-1
- Autogenerated by Bloom

* Mon Mar 28 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.22.0-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.21.1-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Aditya Pande <aditya.pande@openrobotics.org> - 0.21.0-2
- Autogenerated by Bloom

