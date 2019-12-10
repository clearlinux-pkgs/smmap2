#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x665F99FA9D99966C (byronimo@gmail.com)
#
Name     : smmap2
Version  : 2.0.5
Release  : 7
URL      : https://files.pythonhosted.org/packages/3b/ba/e49102b3e8ffff644edded25394b2d22ebe3e645f3f6a8139129c4842ffe/smmap2-2.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/3b/ba/e49102b3e8ffff644edded25394b2d22ebe3e645f3f6a8139129c4842ffe/smmap2-2.0.5.tar.gz
Source1  : https://files.pythonhosted.org/packages/3b/ba/e49102b3e8ffff644edded25394b2d22ebe3e645f3f6a8139129c4842ffe/smmap2-2.0.5.tar.gz.asc
Summary  : A pure Python implementation of a sliding window memory map manager
Group    : Development/Tools
License  : BSD-3-Clause
Requires: smmap2-license = %{version}-%{release}
Requires: smmap2-python = %{version}-%{release}
Requires: smmap2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nosexcover

%description
When reading from many possibly large files in a fashion similar to random access, it is usually the fastest and most efficient to use memory maps.
        
        Although memory maps have many advantages, they represent a very limited system resource as every map uses one file descriptor, whose amount is limited per process. On 32 bit systems, the amount of memory you can have mapped at a time is naturally limited to theoretical 4GB of memory, which may not be enough for some applications.
        
        
        ## Limitations
        
        * **System resources (file-handles) are likely to be leaked!** This is due to the library authors reliance on a deterministic `__del__()` destructor.
        * The memory access is read-only by design.
        
        
        ## Overview

%package license
Summary: license components for the smmap2 package.
Group: Default

%description license
license components for the smmap2 package.


%package python
Summary: python components for the smmap2 package.
Group: Default
Requires: smmap2-python3 = %{version}-%{release}

%description python
python components for the smmap2 package.


%package python3
Summary: python3 components for the smmap2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the smmap2 package.


%prep
%setup -q -n smmap2-2.0.5
cd %{_builddir}/smmap2-2.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576015848
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/smmap2
cp %{_builddir}/smmap2-2.0.5/LICENSE %{buildroot}/usr/share/package-licenses/smmap2/62b7f6262d13a59f19d9e458820dd16f5bd99358
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/smmap2/62b7f6262d13a59f19d9e458820dd16f5bd99358

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
