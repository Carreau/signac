#!/usr/bin/env python

from tests import test_token

from compdb.contrib import find_jobs
jobs = find_jobs(None, test_token)
for job in jobs:
    job.remove()
