# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""Module containing collaborative optimization code."""

from tensorflow_model_optimization.python.core.quantization.keras.collab_opts.cluster_preserve.cluster_utils import (
    strip_clustering_cqat,)

from tensorflow_model_optimization.python.core.quantization.keras.collab_opts.cluster_preserve.default_8bit_cluster_preserve_quantize_scheme import (
    Default8BitClusterPreserveQuantizeScheme,)

# Deprecated import.
# Please import from tfmot.quantization.keras.collab_opts
from tensorflow_model_optimization.python.core.quantization.keras.collab_opts.prune_preserve.default_8bit_prune_preserve_quantize_scheme import (
    Default8BitPrunePreserveQuantizeScheme,)
