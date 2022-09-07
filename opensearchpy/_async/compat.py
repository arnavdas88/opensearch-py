# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.


import asyncio

from ..compat import *  # noqa

# Hack supporting Python 3.6 asyncio which didn't have 'get_running_loop()'.
# Essentially we want to get away from having users pass in a loop to us.
# Instead we should call 'get_running_loop()' whenever we need
# the currently running loop.
# See: https://aiopg.readthedocs.io/en/stable/run_loop.html#implementation
try:
    from asyncio import get_running_loop
except ImportError:

    def get_running_loop():
        loop = asyncio.get_event_loop()
        if not loop.is_running():
            raise RuntimeError("no running event loop")
        return loop


__all__ = ["get_running_loop"]
