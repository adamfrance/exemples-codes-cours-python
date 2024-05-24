from datetime import datetime, timezone
from unittest.mock import patch
import pytest
from core.models import (
    Exam,
    Exercise,
    Solution
)

from math import * # pbe perf, conflits de nom

