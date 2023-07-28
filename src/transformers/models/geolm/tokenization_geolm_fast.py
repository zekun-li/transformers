# coding=utf-8
# Copyright 2022 Zekun Li and The HuggingFace Inc. team. All rights reserved.
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
"""Tokenization classes for GeoLM."""
from ...utils import logging
from ..bert.tokenization_bert_fast import BertTokenizerFast
from .tokenization_geolm import GeoLMTokenizer


logger = logging.get_logger(__name__)

VOCAB_FILES_NAMES = {"vocab_file": "vocab.txt"}

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "zekun-li/geolm-base-cased": "https://huggingface.co/zekun-li/geolm-base-cased/resolve/main/vocab.txt",
    }
}

PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "zekun-li/geolm-base-cased": 512,
}


PRETRAINED_INIT_CONFIGURATION = {
    "zekun-li/geolm-base-cased": {"do_lower_case": False},
}


class GeoLMTokenizerFast(BertTokenizerFast):
    r"""
    Construct a "fast" GeoLM tokenizer (backed by HuggingFace's *tokenizers* library).

    [`~GeoLMTokenizerFast`] is identical to [`BertTokenizerFast`] and runs end-to-end tokenization: punctuation
    splitting and wordpiece.

    Refer to superclass [`BertTokenizerFast`] for usage examples and documentation concerning parameters.
    """

    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    slow_tokenizer_class = GeoLMTokenizer