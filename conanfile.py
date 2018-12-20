#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostXpressiveConan(base.BoostBaseConan):
    name = "boost_xpressive"
    url = "https://github.com/bincrafters/conan-boost_xpressive"
    lib_short_names = ["xpressive"]
    header_only_libs = ["xpressive"]
    b2_requires = [
        "boost_assert",
        "boost_config",
        "boost_conversion",
        "boost_core",
        "boost_exception",
        "boost_fusion",
        "boost_integer",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_mpl",
        "boost_numeric_conversion",
        "boost_optional",
        "boost_preprocessor",
        "boost_proto",
        "boost_range",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_traits",
        "boost_typeof",
        "boost_utility"
    ]
