# Copyright 2023 Sony Semiconductor Israel, Inc. All rights reserved.
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
from typing import Union

from model_compression_toolkit.core.common import Logger
from model_compression_toolkit.core.common.constants import FOUND_TF

from model_compression_toolkit.quantizers_infrastructure.common.base_trainable_quantizer import BaseTrainableQuantizer
from model_compression_toolkit.quantizers_infrastructure import TrainableQuantizerWeightsConfig, \
    TrainableQuantizerActivationConfig, BaseKerasTrainableQuantizer

if FOUND_TF:

    class BaseKerasQATTrainableQuantizer(BaseKerasTrainableQuantizer):
        """
        A base class for trainable Keras quantizer for QAT.
        """

        def __init__(self,
                     quantization_config: Union[TrainableQuantizerWeightsConfig, TrainableQuantizerActivationConfig]):
            """
            Initializes BaseKerasQATTrainableQuantizer object.

            Args:
                quantization_config: quantizer config class contains all the information about a quantizer configuration.
            """

            super().__init__(quantization_config)

else:
    class BaseKerasQATTrainableQuantizer(BaseKerasTrainableQuantizer):
        def __init__(self,
                     quantization_config: Union[TrainableQuantizerWeightsConfig, TrainableQuantizerActivationConfig]):

            super().__init__(quantization_config)
            Logger.critical('Installing tensorflow and tensorflow_model_optimization is mandatory '
                            'when using BaseKerasQATTrainableQuantizer. '
                            'Could not find Tensorflow package.')  # pragma: no cover
