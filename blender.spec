#
# spec file for package blender
#
# Copyright (c) 2021 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

# Turn off the brp-python-bytecompile automagic
%global _python_bytecompile_extra 0

%define _legacy_common_support 1
%global debug_package %{nil}

%global commit0 28bf1d4037496397e3bc5d69ce51d8ac9b8a2738
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

%global blender_api 2.93.0

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

# Reduce compression level and build time
%define _source_payload w5.gzdio
%define _binary_payload w5.gzdio

# Macros
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%ifarch %{ix86} x86_64
%global cyclesflag ON
%else
%global cyclesflag OFF
%endif


# Enable this or rebuild the package with "--with=ffmpeg" to enable FFmpeg
# support.
%global _with_ffmpeg 1

# Enable this or rebuild the package with "--with=openvdb" to enable OpenVDB
# support.
%global _with_openvdb 1

Name:       blender
Epoch:      1
Version:    %{blender_api}
Release:    7%{?dist}

Summary:    3D modeling, animation, rendering and post-production
License:    GPLv2
URL:        http://www.blender.org

Source0:    http://download.%{name}.org/source/%{name}-%{version}.tar.xz
Source1:    %{name}.thumbnailer
Source2:    %{name}-fonts.metainfo.xml
Source3:    https://github.com/blender/blender-addons-contrib/archive/v%{version}.tar.gz#/blender-addons-contrib.tar.gz
Source4:    https://developer.download.nvidia.com/redist/optix/v7.0/OptiX-7.0.0-include.zip
Source5:    %{name}.xml
Source6:    %{name}.appdata.xml
Source10:   macros.%{name}


Patch1:     blender-2.91-eigen3-log1p-ifelse.patch
Patch2:     embree.patch


# Development stuff
BuildRequires:  boost-devel
BuildRequires:  blosc-devel
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc-c++
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:	ninja-build
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  jemalloc-devel
BuildRequires:  libtool
BuildRequires:  libspnav-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pugixml-devel

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-rpm-macros
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(requests)
%if 0%{?fedora} <= 32
BuildRequires:  python3.9
%else
BuildRequires:  python3-devel
%endif
BuildRequires:  python3.9
BuildRequires:  subversion-devel
BuildRequires:	help2man
BuildRequires:	vulkan-loader

# Compression stuff
BuildRequires:  lzo-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

# 3D modeling stuff
%ifarch x86_64
BuildRequires:  embree-devel
BuildRequires:  cmake(embree)
%endif
BuildRequires:  fftw-devel
BuildRequires:  ftgl-devel
BuildRequires:  glew-devel
BuildRequires:  freeglut-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXi-devel
BuildRequires:  openCOLLADA-devel >= svn825
BuildRequires:  ode-devel
BuildRequires:  SDL2-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  opensubdiv-devel

# Picture/Video stuff
BuildRequires:  alembic-devel
BuildRequires:  libvulkan.so.1
%{?_with_ffmpeg:
BuildRequires:  ffmpeg-devel >= 4.4
}
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtiff-devel
BuildRequires:  libwebp-devel
BuildRequires:  OpenColorIO-devel >= 1.1.1
BuildRequires:  OpenEXR-devel
BuildRequires:  OpenImageIO-devel >= 2.2.14.0
BuildRequires:  openjpeg2-devel
%if 0%{?fedora} >= 30 || 0%{?rhel} >= 8
BuildRequires:  openvdb-devel >= 7.0.0
%endif
BuildRequires:  tbb-devel
# New
BuildRequires:  libXxf86vm-devel
BuildRequires:	libXrender-devel
BuildRequires:	gmp-devel
BuildRequires:	potrace-devel
BuildRequires:	libharu-devel
BuildRequires:  oidn-devel
%if 0%{?fedora} >= 32
BuildRequires:  openxr-devel
%endif
BuildRequires:  pkgconfig(oslcomp)
BuildRequires:  openshadinglanguage
BuildRequires:  openshadinglanguage-common-headers
BuildRequires:  alembic-devel

# Audio stuff
BuildRequires:  freealut-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libao-devel
BuildRequires:  libogg-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel

# Typography stuff
BuildRequires:  fontpackages-devel
BuildRequires:  freetype-devel

# packages-devel
BuildRequires:  freetype-devel

%if 0%{?fedora} || 0%{?rhel} >= 8

# Appstream stuff
BuildRequires:  libappstream-glib

%endif


Requires:       google-droid-sans-fonts
Requires:       %{name}-fonts = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       fontpackages-filesystem
Requires:       python3dist(requests)
Requires:       python3dist(numpy)
%if 0%{?fedora} <= 32
Requires:	python3.9
%endif
%if 0%{?fedora} >= 35
Requires:	python3.9
%endif
Provides:       blender(ABI) = %{blender_api}

%description
Blender is the essential software solution you need for 3D, from modeling,
animation, rendering and post-production to interactive creation and playback.

Professionals and novices can easily and inexpensively publish stand-alone,
secure, multi-platform content to the web, CD-ROMs, and other media.


%package rpm-macros
Summary:        RPM macros to build third-party blender addons packages
BuildArch:      noarch

%description rpm-macros
This package provides rpm macros to support the creation of third-party addon
packages to extend Blender.

%package fonts
Summary:        International Blender mono space font
License:        ASL 2.0 and GPLv3 and Bitstream Vera and Public Domain
BuildArch:      noarch
Obsoletes:      fonts-%{name} < 1:2.78-3
Provides:       fonts-%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description fonts
This package contains an international Blender mono space font which is a
composition of several mono space fonts to cover several character sets.


%prep
%setup -n blender-%{version} -a3 -a4
%patch1 -p1
%patch2 -p1

mv -f blender-addons-contrib-%{version} release/scripts/addons_contrib

# Delete the bundled FindOpenJPEG to make find_package use the system version
# instead (the local version hardcodes the openjpeg version so it is not update
# proof)
rm -f build_files/cmake/Modules/FindOpenJPEG.cmake


# Change shebang in all relevant files in this directory and all subdirectories
# See `man find` for how the `-exec command {} +` syntax works

%if 0%{?fedora} >= 35 
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!/usr/bin/python3.9=' {} +
%endif

%if 0%{?fedora} <= 34
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +
%endif

%if 0%{?fedora} <= 32
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!/usr/bin/python3.9=' {} +
%endif

%build

#     -DCMAKE_INSTALL_LIBDIR=%{_lib} \
#    -DCMAKE_INSTALL_FULL_LIBDIR=%{_lib} \
#    -GNinja \
mkdir -p build
cmake -B build \
    -GNinja \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=OFF \
    -DWITH_LLVM:BOOL=ON \
    -DENABLE_CCACHE=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DOPTIX_ROOT_DIR=$PWD/include \
%if 0%{?fedora}
    -DWITH_CYCLES_EMBREE=%{cyclesflag} \
    %endif
    -DWITH_CYCLES=%{cyclesflag} \
    -DBOOST_ROOT=%{_prefix} \
    -DBUILD_SHARED_LIBS=OFF \
    -DCMAKE_SKIP_RPATH=ON \
    -DOpenGL_GL_PREFERENCE=GLVND \
    -DWITH_ALEMBIC=ON \
    -DWITH_BUILDINFO=ON \
    %{?_with_ffmpeg:-DWITH_CODEC_FFMPEG=ON} \
    -DWITH_CODEC_SNDFILE=ON \
    -DWITH_CXX_GUARDEDALLOC=OFF \
    -DWITH_DOC_MANPAGE=ON \
    -DWITH_INTERNATIONAL=ON \
    -DWITH_FFTW3=ON \
    -DWITH_IMAGE_OPENJPEG=ON \
    -DWITH_INPUT_NDOF=ON \
    -DWITH_INSTALL_PORTABLE=OFF \
    -DWITH_JACK=ON \
    -DWITH_MEM_JEMALLOC=ON \
    -DWITH_MOD_OCEANSIM=ON \
    -DWITH_OPENCOLLADA=ON \
    -DWITH_OPENCOLORIO=ON \
    -DWITH_OPENIMAGEIO=ON \
    -DWITH_OPENVDB=ON \
    -DWITH_OPENVDB_BLOSC=ON \
    -DWITH_PYTHON=ON \
    %if 0%{?fedora} <= 32
    -DWITH_PYTHON_INSTALL=ON \
    -DPYTHON_LIBRARY=python3.9 \
    -DPYTHON_INCLUDE_DIRS=/usr/include/python3.9 \
    -DWITH_PYTHON_INSTALL_NUMPY=OFF  \
    %else
    -DWITH_PYTHON_INSTALL=OFF \
    -DWITH_PYTHON_INSTALL_NUMPY=OFF  \
    %endif
    %if 0%{?fedora} >= 35
    -DWITH_PYTHON_INSTALL=ON \
    -DPYTHON_LIBRARY=python3.9 \
    -DPYTHON_INCLUDE_DIRS=/usr/include/python3.9 \
    -DWITH_PYTHON_INSTALL_NUMPY=OFF  \
    %endif
    %if 0%{?fedora} <= 31
    -DWITH_DOC_MANPAGE=OFF \
    %endif
    -DWITH_PYTHON_INSTALL_REQUESTS=OFF \
    -DWITH_PYTHON_SAFETY=ON \
    -DWITH_SDL=ON \
    -DWITH_SYSTEM_LZO=ON \
    -DPYTHON_LIBPATH=/usr/lib64 \
    -D_osl_LIBRARIES=%{_libdir} \
    -DOSL_INCLUDE_DIR=%{_includedir} \
    -DOSL_COMPILER=%{_bindir}/oslc \
    %ifnarch %{ix86} x86_64
    -DWITH_RAYOPTIMIZATION=OFF \
    -DWITH_CPU_SSE=OFF \
%endif
    -DCYCLES_CUDA_BINARIES_ARCH="sm_30;sm_35;sm_37;sm_50;sm_52;sm_60;sm_61;sm_70;sm_75" -Wno-dev  .


%ninja_build -C build -j2 


%install
%ninja_install -C build -j2

# Thumbnailer
install -p -D -m 644 %{S:1} %{buildroot}%{_datadir}/thumbnailers/%{name}.thumbnailer

# Mime support
install -p -D -m 644 %{S:5} %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# Desktop icon
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

# Deal with docs in the files section
rm -rf %{buildroot}%{_docdir}/%{name}/*

# rpm macros
mkdir -p %{buildroot}%{macrosdir}
sed -e 's/@VERSION@/%{blender_api}/g' %{S:10} > %{buildroot}%{macrosdir}/macros.%{name}

%if 0%{?fedora} || 0%{?rhel} >= 8

# AppData
install -p -m 644 -D %{S:6} %{buildroot}%{_metainfodir}/%{name}.appdata.xml

install -p -m 644 -D %{S:2} %{buildroot}%{_metainfodir}/%{name}-fonts.metainfo.xml
%endif

# Localization
%find_lang %{name}


# Avoid having locales listed twice
rm -fr %{buildroot}%{_datadir}/%{blender_api}/locale

# rpmlint fixes
# find %{buildroot}%{_datadir}/%{name}/%{blender_api}/scripts -name "*.py" -exec chmod 755 {} \;
#find %{buildroot}%{_datadir}/%{name}/scripts -type f -exec sed -i -e 's/\r$//g' {} \;


%files -f %{name}.lang
%license COPYING
%license doc/license/*-license.txt
%license release/text/copyright.txt
%doc release/text/readme.html
%{_bindir}/%{name}
%{_bindir}/%{name}-thumbnailer.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
#exclude {_datadir}/{name}/{blender_api}/scripts/addons/cycles/lib/*.cubin
%{_datadir}/icons/hicolor/*/apps/%{name}*.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/thumbnailers/%{name}.thumbnailer
%if 0%{?fedora} >= 32
%{_mandir}/man1/%{name}.*
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
%{_metainfodir}/%{name}.appdata.xml
%endif

%files rpm-macros
%{macrosdir}/macros.%{name}


%files fonts
#license release/datafiles/LICENSE-*.ttf.txt
#{_fontbasedir}/#{name}/
%if 0%{?fedora} || 0%{?rhel} >= 8
%{_metainfodir}/%{name}-fonts.metainfo.xml
%endif


%changelog

* Mon Jun 14 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1:2.93.0-7
- Updated to 2.93.0

* Wed May 12 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1:2.92.0-8
- Rebuilt for ffmpeg 

* Sat May 01 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1:2.92.0-7
- Updated to 2.92.0
- OpenColorIO disabled no yet ready for 2.0

* Sat Dec 26 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1:2.91.0-7
- Updated to 2.91.0
- Enabled OPTIX

* Thu Nov 05 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1:2.90.0-8
- Rebuilt for opencv 

* Tue Sep 01 2020 David Va <davidva AT tuta DOT io> - 1:2.90.0-7
- Updated to 2.90.0
- Disable Embree, 3.11 is not yet supported.

* Sun Aug 23 2020 David Va <davidva AT tuta DOT io> - 1:2.83.5-7
- Updated to 2.83.5

* Thu Jul 09 2020 David Va <davidva AT tuta DOT io> - 1:2.83.2-10
- Updated to 2.83.2

* Thu Jun 04 2020 David Va <davidva AT tuta DOT io> - 1:2.83-10
- Sync to stable
- Go back to python3.8 in rawhide

* Tue Jun 02 2020 David Va <davidva AT tuta DOT io> - 1:2.83-9
- Rebuilt for python3.9

* Mon May 18 2020 David Va <davidva AT tuta DOT io> - 1:2.83-8
- Rebuilt for LibRaw

* Thu Apr 30 2020 David Va <davidva AT tuta DOT io> - 1:2.83-7
- Updated to 2.83

* Sun Feb 16 2020 David Va <davidva AT tuta DOT io> - 1:2.82.a-7
- Updated to 2.82.a

* Sun Feb 16 2020 David Va <davidva AT tuta DOT io> - 1:2.82-7
- Updated to 2.82

* Tue Feb 11 2020 David Va <davidva AT tuta DOT io> - 1:2.81.a-7
- Updated to 2.81.a

* Sun Dec 29 2019 David Va <davidva AT tuta DOT io> - 1:2.81-8
- Rebuilt for openvdb

* Sun Nov 24 2019 David Va <davidva AT tuta DOT io> - 1:2.81-7
- Updated to 1:2.81-7

* Fri Nov 15 2019 David Va <davidva AT tuta DOT io> - 1:2.80-20
- Rebuilt for alembic 

* Sat Oct 12 2019 David Va <davidva AT tuta DOT io> - 1:2.80-11
- Rebuilt for openvdb

* Thu Sep 05 2019 David Va <davidva AT tuta DOT io> - 1:2.80-10
- Enabled ffmpeg
- Upstream
- Disabled CUDA

* Tue Aug 20 2019 Simone Caronni <negativo17@gmail.com> - 2:2.80-6
- Enable OpenVDB.

* Sun Aug 18 2019 Simone Caronni <negativo17@gmail.com> - 1:2.80-5
- Clean up patches/sources.
- Fix installation of locales, scripts, thumbnailer, etc.
- Rpmlint fixes.
- Add ppc64le and s390x support.

* Thu Aug 15 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.80-4
- Restore broken international fonts support

* Wed Aug 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.80-3
- Set embree dependency to x86_64 architecture
- Temporarily disable build for ppc64le and s390x

* Tue Jul 30 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.80-2
- Enable embree, webp and bzip support
- Remove game engine support dropped from upstream
- Drop blenderplayer standalone package

* Tue Jul 30 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.80-1
- Update to 2.80

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.79b-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79b-17
- Rebuild for alembic 1.7.11

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 1:2.79b-16
- Rebuild for OpenEXR 2.3.0.

* Thu Apr 04 2019 Richard Shaw <hobbes1069@gmail.com> - 1:2.79b-15
- Rebuild for OpenColorIO 1.1.1.

* Wed Apr 03 01:33:05 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1:2.79b-14
- Fix build for GCC9 new OpenMP data sharing

* Thu Mar 14 2019 Mohan Boddu <mboddu@bhujji.com> - 1:2.79b-13
- Rebuild for OpenImageIO 2.0.5

* Thu Mar 14 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79b-12
- Rebuild for boost 1.69

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.79b-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Richard Shaw <hobbes1069@gmail.com> - 1:2.79b-10
- Add patch for OpenImageIO 2.0 API changes.

* Fri Nov 02 2018 Petr Viktorin <pviktori@redhat.com> - 1:2.79b-9
- Apply workaround for "no text in GUI" bug (#1631922)

* Tue Aug 28 2018 Patrik Novotný <panovotn@redhat.com> - 1:2.79b-8
- change requires to minizip-compat(-devel), rhbz#1609830, rhbz#1615381

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1:2.79b-7
- Rebuilt for glew-2.1.0

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 1:2.79b-6
- Allow rebuilding with OpenVDB support.
- Be consistent with spaces/tabs (rpmlint).

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.79b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1:2.79b-4
- Rebuilt for Python 3.7

* Tue Apr 24 2018 Richard Shaw <hobbes1069@gmail.com> - 1:2.79b-3
- Rebuild for openCOLLADA 1.6.62.

* Thu Mar 29 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79b-2
- Rebuild with applied upstream patches

* Thu Mar 22 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79b-1
- Update to 2.79b
- Reenable openvdb

* Wed Feb 28 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79a-1
- Update to 2.79a
- Add gcc-c++
- Temporarily disable openvdb due failure to build
- Upstream patch for compile fix with GCC 8.0

* Mon Feb 26 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79-8
- Rebuild for boost 1.66

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.79-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 17 2018 Sandro Mani <manisandro@gmail.com> - 1:2.79-6
- Switch to openjpeg2

* Sun Jan 07 2018 Richard Shaw <hobbes1069@gmail.com> - 1:2.79-5
- Rebuild for OpenImageIO 1.8.7.

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.79-4
- Remove obsolete scriptlets

* Mon Dec 25 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79-3
- Rebuilt for alembic 1.7.5

* Sat Oct 28 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.79-2
- Rebuilt for alembic 1.7.4

* Tue Sep 12 2017 Simone Caronni <negativo17@gmail.com> - 1:2.79-1
- Update to 2.79.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.78c-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.78c-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Björn Esser <besser82@fedoraproject.org> - 1:2.78c-6
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.78c-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Wed Apr 26 2017 Simone Caronni <negativo17@gmail.com> - 1:2.78c-4
- Enable OpenVDB and Alembic support.

* Fri Apr 21 2017 Simone Caronni <negativo17@gmail.com> - 1:2.78c-3
- Remove redundant fonts directory in blender-fonts package.
- Enable rebuilding of the package with FFmpeg support enabled.

* Mon Mar 06 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.78c-2
- Restore broken international fonts support (rhbz#1429196)

* Mon Feb 27 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 1:2.78c-1
- New upstream release
- Add modules directory macro

* Sat Feb 25 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 1:2.78b-2
- Patch for handling flickering UI on AMD GPUs (rhbz#1425146)

* Thu Feb 09 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 1:2.78b-1
- New upstream release

* Tue Feb 07 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 1:2.78a-12
- Add presets for RPM macros

* Mon Feb 06 2017 Simone Caronni <negativo17@gmail.com> - 1:2.78a-11
- Update RPM macros.

* Wed Feb 01 2017 Simone Caronni <negativo17@gmail.com> - 1:2.78a-10
- Adjust files section.
- Use system lzo.

* Mon Jan 30 2017 Simone Caronni <negativo17@gmail.com> - 1:2.78a-9
- Use cmake macro.
- Remove redundant GCC options.
- Update scriptlets as per packaging guidelines (mimeinfo only on RHEL 7 and
  Fedora 23, desktop database only on RHEL 7, Fedora 23 and 24).

* Sun Jan 29 2017 Simone Caronni <negativo17@gmail.com> - 1:2.78a-8
- Use system locale directory for translations. This also removes the warning
  about duplicate translations at package assembly time.
- Do not use the Blender API version in the installation folder.
- Install noarch components in /usr/share/blender.
- Install blender-thumbnailer.py in the scripts directory instead of deleting it.

* Sun Jan 29 2017 Simone Caronni <negativo17@gmail.com> - 1:2.78a-7
- Split out main AppStream metadata in its own file, like the fonts subpackage.
- Make sure rpmlint does not fail when checking the SPEC file.
- Simplify fonts packaging and fix font package rename upgrade.
- Clean up build options (sorting, duplicates, obsolete options, etc.).
- Enable buildinfo.
- Remove manual installation of manpages and use CMake option.
- Add blenderplayer man page.
- Remove manual installation of icons, the install target is already installing
  them in the same way.
- Fix -std=c++11 warning during build.

* Tue Jan 10 2017 Luya Tshimbalanga <luya_tfz@thefinalzone.net> - 1:2.78a-6
- rebuilt

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:2.78a-5
- Rebuild for Python 3.6

* Sat Dec 17 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.78a-4
- Add minizip dependency (rhbz#1398451)

* Sat Nov 12 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:2.78a-3
- Disable altivec support on ppc64le for now to avoid "bool" being converted
  (bug 1393157)
- Use __linux__ , gcc does not define __linux on ppc (gcc bug 28314)

* Tue Nov 08 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.78a-2
- Corrected versioning of obsoleted fonts-blender (rhbz#1393006)

* Thu Oct 27 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.78a-1
- New upstream release with several bug fixes

* Thu Oct 20 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.78-3
- Added appdata for blender fonts
- Fixed path for international fonts issue (rhbz#1382428)
- Cleaned up and reworked spec file

* Mon Oct 03 2016 Richard Shaw <hobbes1069@gmail.com> - 1:2.78-2
- Rebuild for new OpenImageIO release.

* Thu Sep 29 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.78-1
- New upstream release
- Added pugixml as dependency

* Fri Jul 29 2016 Luya Tshimbalanga <luya@fedoraproject.org> - 1:2.77a-1
- New upstream release
- Drop patches

* Tue Feb 16 2016 Richard Shaw <hobbes1069@gmail.com> - 1:2.76-7
- Rebuild for updated openCOLLADA.
- Add patch for GCC 6 issues.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.76-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.76-5
- Rebuilt to fix dep. issues

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1:2.76-4
- Rebuild for glew 1.13

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.76-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 12 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:2.76-1
- Update to 2.76
- Clean up specfile
- Enable SDL2

* Tue Sep 01 2015 Jonathan Wakely <jwakely@redhat.com> - 1:2.75-6
- Rebuilt for jemalloc-4.0.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1:2.75-5
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.75-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Thu Jul 23 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1:2.75-3
- Drop esound dep

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1:2.75-2
- rebuild for Boost 1.58

* Tue Jul  7 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.75-1
- New upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 16 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.74-5
- Add dependency to numpy (#1222122I

* Tue May  5 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.74-4
- Fix regression for 3D mice support

* Mon May  4 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.74-3
- Enable 3D mice support

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 1:2.74-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr  1 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.74-1
- New upstream release

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:2.73a-5
- Add an AppData file for the software center

* Wed Feb 04 2015 Petr Machata <pmachata@redhat.com> - 1:2.73a-4
- Bump for rebuild.

* Wed Jan 28 2015 Richard Shaw <hobbes1069@gmail.com> - 1:2.73a-3
- Rebuild for OpenImageIO 1.5.10.

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 1:2.73a-2
- Rebuild for boost 1.57.0

* Wed Jan 21 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.73a-1
- New minor bug-fixing release from upstream

* Thu Jan  8 2015 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.73-1
- New upstream release

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:2.72b-4
- rebuild (openexr)

* Thu Nov  6 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.72b-3
- Fix odd dependy issue

* Sun Nov  2 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.72b-2
- Fix dependency issue (#1157600)

* Thu Oct 23 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.72b-1
- New upstream release

* Sat Oct 11 2014 Dan Horák <dan[at]danny.cz> - 1:2.72-3
- fix size_t inconsistency (upstream issue T42183)

* Thu Oct  9 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.72-2
- Remove OpenCOLLADA patch

* Tue Sep 30 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.72-1
- New upstream release
- Add patch to fix FTBFS with current OpenCOLLADA release

* Sat Sep 06 2014 François Cami <fcami@fedoraproject.org> - 1:2.71-4
- Rebuilt for openCOLLADA 0-19.git69b844d

* Sat Aug 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1:2.71-3
- fix/update icon/mime scriptlets

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 29 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.71-1
- New upstream release
- Use blender.1.py to build man page
- Disable parallel build

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.70a-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1:2.70a-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 1:2.70a-4
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1:2.70a-3
- rebuild for boost 1.55.0

* Wed May 21 2014 Richard Shaw <hobbes1069@gmail.com> - 1:2.70a-2
- Rebuild for updated OpenImageIO 1.4.7.

* Wed Apr 16 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.70a-1
- Minor upstream update

* Mon Mar 24 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.70-2
- Disable CYCLES for non-Intel processors

* Thu Mar 20 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.70-1
- New upstream releasw
- Exclude armv7hl

* Sun Mar  9 2014 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.69-7
- Use new rpm macro for rpm macro direcgory  (#1074263)

* Mon Jan 13 2014 Richard Shaw <hobbes1069@gmail.com> - 1:2.69-6
- Rebuild for updated OpenImageIO 1.3.11.

* Tue Dec 31 2013 François Cami <fcami@fedoraproject.org> - 1:2.69-5
- Enable parallel building.

* Tue Dec 31 2013 François Cami <fcami@fedoraproject.org> - 1:2.69-4
- Add Ocean Simulation (#1047589).
- Fix mixed use of tabs and spaces in blender.spec (rpmlint).

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:2.69-3
- rebuild (openexr)

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1:2.69-2
- rebuilt for GLEW 1.10

* Thu Oct 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.69-1
- New upsream release

* Mon Sep  9 2013 François Cami <fcami@fedoraproject.org> - 1:2.68a-6
- Rebuild.

* Wed Sep  4 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.68a-5
- Include derived DoridSans font for CJK support (#867205)

* Sun Sep  1 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.68a-4
- Aboid twice occurance of locale files
- Fix typo in DroideSans font name

* Wed Aug 28 2013 François Cami <fcami@fedoraproject.org> - 1:2.68a-3
- Enable jemalloc and OpenColorIO. (#1002197)
- Re-enable localization (#867285)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.68a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.68a-1
- New minor upstream bugfix release

* Mon Jul 29 2013 Petr Machata <pmachata@redhat.com> - 1:2.68-4
- Rebuild for boost 1.54.0

* Tue Jul 23 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.68-3
- Rebuilt again

* Mon Jul 22 2013 Richard Shaw <hobbes1069@gmail.com> - 1:2.68-2
- Rebuild for updated OpenImageIO.

* Fri Jul 19 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.68-1
- New upstream release

* Sun Jul  7 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.67b-3
- Suppress output of update-mime-database (#541041)

* Fri Jun  7 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.67b-1
- Minor upstream bugfix update

* Mon Jun  3 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.67a-3
- Fix crash in blender/makerna/intern/rna_access.c (ä969043)

* Sun May 26 2013 Dan Horák <dan[at]danny.cz> - 1:2.67a-2
- fix build on non-x86 arches

* Fri May 24 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.67a-1
- New minor upstream release

* Fri May 17 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.67-2
- Fix dependency issues with fonts subpackage
- Make fonts subpackage noarch

* Wed May  8 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.67-1
- New upstream release
- Add subpackage for international mono space font

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:2.66a-2
- rebuild (OpenEXR)

* Wed Mar  6 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.66a-1
- New upstream release

* Sat Feb 23 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.66-2
- Fix wrong font name for international feature (#867205)

* Thu Feb 21 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1:2.66-1
- New upstream release
- Remove unnecessaries patches
- Add Patch to remove '//' in includes

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1:2.65a-5
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1:2.65a-4
- Rebuild for Boost-1.53.0

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1:2.65a-3
- rebuild due to "jpeg8-ABI" feature drop

* Tue Jan 15 2013 Richard Shaw <hobbes1069@gmail.com> - 1:2.65a-2
- Rebuild for updated OpenImageIO library.
