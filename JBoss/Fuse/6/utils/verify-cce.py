#!/usr/bin/env python

import sys

# always use shared/modules version
SHARED_MODULE_PATH = "../../../../shared/modules"
sys.path.insert(0, SHARED_MODULE_PATH)
import verify_cce_module

if __name__ == "__main__":
    verify_cce_module.main()
