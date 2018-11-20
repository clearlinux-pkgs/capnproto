#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : capnproto
Version  : 0.7.0
Release  : 6
URL      : https://capnproto.org/capnproto-c++-0.7.0.tar.gz
Source0  : https://capnproto.org/capnproto-c++-0.7.0.tar.gz
Summary  : Basic utility library called KJ
Group    : Development/Tools
License  : MIT
Requires: capnproto-bin = %{version}-%{release}
Requires: capnproto-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : openssl-dev

%description
Cap'n Proto - Insanely Fast Data Serialization Format
https://capnproto.org
Cap'n Proto is an insanely fast data interchange format and capability-based
RPC system.  Think JSON, except binary.  Or think of Google's Protocol Buffers
(http://protobuf.googlecode.com), except faster.  In fact, in benchmarks,
Cap'n Proto is INFINITY TIMES faster than Protocol Buffers.

%package bin
Summary: bin components for the capnproto package.
Group: Binaries
Requires: capnproto-license = %{version}-%{release}

%description bin
bin components for the capnproto package.


%package dev
Summary: dev components for the capnproto package.
Group: Development
Requires: capnproto-bin = %{version}-%{release}
Provides: capnproto-devel = %{version}-%{release}

%description dev
dev components for the capnproto package.


%package license
Summary: license components for the capnproto package.
Group: Default

%description license
license components for the capnproto package.


%prep
%setup -q -n capnproto-c++-0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542677518
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1542677518
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/capnproto
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/capnproto/LICENSE.txt
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/capnp
/usr/bin/capnpc
/usr/bin/capnpc-c++
/usr/bin/capnpc-capnp

%files dev
%defattr(-,root,root,-)
/usr/include/capnp/any.h
/usr/include/capnp/blob.h
/usr/include/capnp/c++.capnp
/usr/include/capnp/c++.capnp.h
/usr/include/capnp/capability.h
/usr/include/capnp/common.h
/usr/include/capnp/compat/json.capnp.h
/usr/include/capnp/compat/json.h
/usr/include/capnp/dynamic.h
/usr/include/capnp/endian.h
/usr/include/capnp/ez-rpc.h
/usr/include/capnp/generated-header-support.h
/usr/include/capnp/json.capnp
/usr/include/capnp/layout.h
/usr/include/capnp/list.h
/usr/include/capnp/membrane.h
/usr/include/capnp/message.h
/usr/include/capnp/orphan.h
/usr/include/capnp/persistent.capnp
/usr/include/capnp/persistent.capnp.h
/usr/include/capnp/pointer-helpers.h
/usr/include/capnp/pretty-print.h
/usr/include/capnp/raw-schema.h
/usr/include/capnp/rpc-prelude.h
/usr/include/capnp/rpc-twoparty.capnp
/usr/include/capnp/rpc-twoparty.capnp.h
/usr/include/capnp/rpc-twoparty.h
/usr/include/capnp/rpc.capnp
/usr/include/capnp/rpc.capnp.h
/usr/include/capnp/rpc.h
/usr/include/capnp/schema-lite.h
/usr/include/capnp/schema-loader.h
/usr/include/capnp/schema-parser.h
/usr/include/capnp/schema.capnp
/usr/include/capnp/schema.capnp.h
/usr/include/capnp/schema.h
/usr/include/capnp/serialize-async.h
/usr/include/capnp/serialize-packed.h
/usr/include/capnp/serialize-text.h
/usr/include/capnp/serialize.h
/usr/include/kj/arena.h
/usr/include/kj/array.h
/usr/include/kj/async-inl.h
/usr/include/kj/async-io.h
/usr/include/kj/async-prelude.h
/usr/include/kj/async-unix.h
/usr/include/kj/async-win32.h
/usr/include/kj/async.h
/usr/include/kj/common.h
/usr/include/kj/compat/gtest.h
/usr/include/kj/compat/gzip.h
/usr/include/kj/compat/http.h
/usr/include/kj/compat/readiness-io.h
/usr/include/kj/compat/tls.h
/usr/include/kj/compat/url.h
/usr/include/kj/debug.h
/usr/include/kj/encoding.h
/usr/include/kj/exception.h
/usr/include/kj/filesystem.h
/usr/include/kj/function.h
/usr/include/kj/hash.h
/usr/include/kj/io.h
/usr/include/kj/main.h
/usr/include/kj/map.h
/usr/include/kj/memory.h
/usr/include/kj/mutex.h
/usr/include/kj/one-of.h
/usr/include/kj/parse/char.h
/usr/include/kj/parse/common.h
/usr/include/kj/refcount.h
/usr/include/kj/std/iostream.h
/usr/include/kj/string-tree.h
/usr/include/kj/string.h
/usr/include/kj/table.h
/usr/include/kj/test.h
/usr/include/kj/thread.h
/usr/include/kj/threadlocal.h
/usr/include/kj/time.h
/usr/include/kj/timer.h
/usr/include/kj/tuple.h
/usr/include/kj/units.h
/usr/include/kj/vector.h
/usr/include/kj/windows-sanity.h
/usr/lib64/cmake/CapnProto/CapnProtoConfig.cmake
/usr/lib64/cmake/CapnProto/CapnProtoConfigVersion.cmake
/usr/lib64/cmake/CapnProto/CapnProtoMacros.cmake
/usr/lib64/cmake/CapnProto/CapnProtoTargets.cmake
/usr/lib64/libcapnp-0.7.0.so
/usr/lib64/libcapnp-json-0.7.0.so
/usr/lib64/libcapnp-json.so
/usr/lib64/libcapnp-rpc-0.7.0.so
/usr/lib64/libcapnp-rpc.so
/usr/lib64/libcapnp.so
/usr/lib64/libcapnpc-0.7.0.so
/usr/lib64/libcapnpc.so
/usr/lib64/libkj-0.7.0.so
/usr/lib64/libkj-async-0.7.0.so
/usr/lib64/libkj-async.so
/usr/lib64/libkj-http-0.7.0.so
/usr/lib64/libkj-http.so
/usr/lib64/libkj-test-0.7.0.so
/usr/lib64/libkj-test.so
/usr/lib64/libkj-tls-0.7.0.so
/usr/lib64/libkj-tls.so
/usr/lib64/libkj.so
/usr/lib64/pkgconfig/capnp-json.pc
/usr/lib64/pkgconfig/capnp-rpc.pc
/usr/lib64/pkgconfig/capnp.pc
/usr/lib64/pkgconfig/kj-async.pc
/usr/lib64/pkgconfig/kj-http.pc
/usr/lib64/pkgconfig/kj-test.pc
/usr/lib64/pkgconfig/kj.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/capnproto/LICENSE.txt
