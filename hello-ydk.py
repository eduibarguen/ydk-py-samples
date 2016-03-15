#!/usr/bin/env python
#
# Copyright 2016 Cisco Systems, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# nc-read-oper-shellutil-10-ydk.py
# Read all data for model Cisco-IOS-XR-shellutil-oper and print system
# uptime.
#

from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.shellutil import Cisco_IOS_XR_shellutil_oper as xr_shellutil_oper
from datetime import timedelta


if __name__ == "__main__":
    """Main execution path"""

    # create NETCONF session
    session = NetconfServiceProvider(address="10.0.0.1",
                                     port=830,
                                     username="admin",
                                     password="admin",
                                     protocol="ssh")
    # create CRUD service
    crud = CRUDService()

    system_time = xr_shellutil_oper.SystemTime()  # create oper object
    system_time = crud.read(session, system_time)  # read object from NETCONF device
    print "System uptime is", str(timedelta(seconds=system_time.uptime.uptime))

    session.close()
    exit()
### End of script