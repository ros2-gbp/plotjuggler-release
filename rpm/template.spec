%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-plotjuggler
Version:        2.3.7
Release:        1%{?dist}
Summary:        ROS plotjuggler package

License:        LGPLv3
URL:            https://github.com/facontidavide/PlotJuggler
Source0:        %{name}-%{version}.tar.gz

Requires:       binutils-devel
Requires:       qt5-qtbase-devel
Requires:       qt5-qtdeclarative-devel
Requires:       qt5-qtmultimedia
Requires:       qt5-qtmultimedia-devel
Requires:       qt5-qtsvg-devel
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-ros-type-introspection
Requires:       ros-melodic-rosbag
Requires:       ros-melodic-rosbag-storage
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roscpp-serialization
Requires:       ros-melodic-rostime
Requires:       ros-melodic-tf
Requires:       ros-melodic-topic-tools
BuildRequires:  binutils-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtmultimedia
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-ros-type-introspection
BuildRequires:  ros-melodic-rosbag
BuildRequires:  ros-melodic-rosbag-storage
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roscpp-serialization
BuildRequires:  ros-melodic-rostime
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-topic-tools

%description
PlotJuggler: juggle with data

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Wed Oct 30 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.7-1
- Autogenerated by Bloom

* Wed Oct 16 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.6-2
- Autogenerated by Bloom

* Wed Oct 16 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.6-1
- Autogenerated by Bloom

* Fri Oct 11 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.5-2
- Autogenerated by Bloom

* Fri Oct 11 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.5-1
- Autogenerated by Bloom

* Thu Oct 03 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.4-2
- Autogenerated by Bloom

* Thu Oct 03 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.4-1
- Autogenerated by Bloom

* Tue Oct 01 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.3-2
- Autogenerated by Bloom

* Tue Oct 01 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.3-1
- Autogenerated by Bloom

* Mon Sep 30 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.2-1
- Autogenerated by Bloom

* Tue Sep 24 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.1-1
- Autogenerated by Bloom

* Thu Jul 11 2019 Davide Faconti <davide.faconti@gmail.com> - 2.3.0-1
- Autogenerated by Bloom

* Fri Mar 29 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.10-0
- Autogenerated by Bloom

* Mon Mar 25 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.9-0
- Autogenerated by Bloom

* Sun Mar 24 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.8-0
- Autogenerated by Bloom

* Wed Mar 20 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.7-0
- Autogenerated by Bloom

* Thu Mar 07 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.6-0
- Autogenerated by Bloom

* Tue Feb 26 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.5-0
- Autogenerated by Bloom

* Mon Feb 18 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.3-0
- Autogenerated by Bloom

* Wed Feb 13 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.2-0
- Autogenerated by Bloom

* Thu Feb 07 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.1-0
- Autogenerated by Bloom

* Thu Feb 07 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.0-1
- Autogenerated by Bloom

* Thu Feb 07 2019 Davide Faconti <davide.faconti@gmail.com> - 2.1.0-0
- Autogenerated by Bloom

* Wed Feb 06 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.7-0
- Autogenerated by Bloom

* Tue Feb 05 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.5-0
- Autogenerated by Bloom

* Tue Jan 29 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.4-0
- Autogenerated by Bloom

* Sat Jan 26 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.3-0
- Autogenerated by Bloom

* Wed Jan 23 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.2-1
- Autogenerated by Bloom

* Wed Jan 23 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.2-0
- Autogenerated by Bloom

* Mon Jan 21 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.1-0
- Autogenerated by Bloom

* Sun Jan 20 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.0-0
- Autogenerated by Bloom

* Mon Nov 12 2018 Davide Faconti <davide.faconti@gmail.com> - 1.9.0-0
- Autogenerated by Bloom

* Mon Sep 17 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.4-0
- Autogenerated by Bloom

* Fri Aug 24 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.3-0
- Autogenerated by Bloom

* Sun Aug 19 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.2-0
- Autogenerated by Bloom

* Sat Aug 18 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.1-0
- Autogenerated by Bloom

* Fri Aug 17 2018 Davide Faconti <davide.faconti@gmail.com> - 1.8.0-0
- Autogenerated by Bloom

* Sun Aug 12 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.3-0
- Autogenerated by Bloom

* Fri Aug 10 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.2-0
- Autogenerated by Bloom

* Sun Jul 22 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.1-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Davide Faconti <davide.faconti@gmail.com> - 1.7.0-0
- Autogenerated by Bloom

