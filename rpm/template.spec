%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-plotjuggler
Version:        3.8.8
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS plotjuggler package

License:        MPL-2.0
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       cppzmq-devel
Requires:       libzstd-devel
Requires:       lz4-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtsvg-devel
Requires:       qt5-qtwebsockets-devel
Requires:       qt5-qtx11extras-devel
Requires:       ros-humble-ament-index-cpp
Requires:       ros-humble-fastcdr
Requires:       ros-humble-rclcpp
Requires:       ros-humble-ros-workspace
BuildRequires:  binutils-devel
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  cppzmq-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-ament-index-cpp
BuildRequires:  ros-humble-fastcdr
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
PlotJuggler: juggle with data

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Thu Jan 18 2024 Davide Faconti <davide.faconti@gmail.com> - 3.8.8-1
- Autogenerated by Bloom

* Tue Jan 16 2024 Davide Faconti <davide.faconti@gmail.com> - 3.8.7-1
- Autogenerated by Bloom

* Tue Jan 09 2024 Davide Faconti <davide.faconti@gmail.com> - 3.8.6-3
- Autogenerated by Bloom

* Tue Jan 09 2024 Davide Faconti <davide.faconti@gmail.com> - 3.8.6-2
- Autogenerated by Bloom

* Tue Jan 09 2024 Davide Faconti <davide.faconti@gmail.com> - 3.8.6-1
- Autogenerated by Bloom

* Wed Jan 03 2024 Davide Faconti <davide.faconti@gmail.com> - 3.8.5-1
- Autogenerated by Bloom

* Wed Dec 20 2023 Davide Faconti <davide.faconti@gmail.com> - 3.8.4-1
- Autogenerated by Bloom

* Thu Dec 14 2023 Davide Faconti <davide.faconti@gmail.com> - 3.8.3-1
- Autogenerated by Bloom

* Tue Nov 28 2023 Davide Faconti <davide.faconti@gmail.com> - 3.8.2-1
- Autogenerated by Bloom

* Wed Nov 22 2023 Davide Faconti <davide.faconti@gmail.com> - 3.8.0-1
- Autogenerated by Bloom

* Sun Nov 12 2023 Davide Faconti <davide.faconti@gmail.com> - 3.7.1-2
- Autogenerated by Bloom

* Tue May 23 2023 Davide Faconti <davide.faconti@gmail.com> - 3.7.1-1
- Autogenerated by Bloom

* Fri May 19 2023 Davide Faconti <davide.faconti@gmail.com> - 3.7.0-1
- Autogenerated by Bloom

* Mon Jul 25 2022 Davide Faconti <davide.faconti@gmail.com> - 3.5.1-1
- Autogenerated by Bloom

* Tue Jul 12 2022 Davide Faconti <davide.faconti@gmail.com> - 3.5.0-1
- Autogenerated by Bloom

* Wed Jun 29 2022 Davide Faconti <davide.faconti@gmail.com> - 3.4.5-1
- Autogenerated by Bloom

* Sun May 15 2022 Davide Faconti <davide.faconti@gmail.com> - 3.4.4-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Davide Faconti <davide.faconti@gmail.com> - 3.4.2-2
- Autogenerated by Bloom

* Sat Feb 12 2022 Davide Faconti <davide.faconti@gmail.com> - 3.4.2-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Davide Faconti <davide.faconti@gmail.com> - 3.4.0-2
- Autogenerated by Bloom

