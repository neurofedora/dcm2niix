%global commit ebc72ae10a3f9e4cc7500decf9966b2a04caad5d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dcm2niix
Version:        0.0.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        DICOM to NIfTI converter

# No license text
# https://github.com/neurolabusc/dcm2niix/issues/7
License:        BSD
URL:            http://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage
Source0:        https://github.com/neurolabusc/dcm2niix/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/neurolabusc/dcm2niix/pull/6
Patch0:         0001-allow-nifti-openjpeg2-be-system.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  nifticlib-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  zlib-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}

# console/ujpeg.{h,cpp}
# https://github.com/neurolabusc/dcm2niix/issues/8
Provides:       bundled(nanojpeg)

%description
dcm2nii is a designed to convert neuroimaging data from the NIfTI format to
the DICOM format.

%prep
%autosetup -n %{name}-%{commit} -p1

chmod -x README.md

rm -rf build/
mkdir build/

%build
pushd build/
  %cmake ../
  %make_build
popd

%install
pushd build/
  %make_install
popd

%files
%doc README.md
%{_bindir}/%{name}

%changelog
* Sat Dec 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.gitebc72ae
- Initial package
