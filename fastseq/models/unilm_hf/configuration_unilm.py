# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
""" UniLM model configuration """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import json
import logging
import sys
from io import open

from fastseq.logging import get_logger
from transformers import PretrainedConfig

logger = get_logger(__name__, logging.INFO)

UNILM_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "unilm-large-cased":
    "https://unilm.blob.core.windows.net/ckpt/unilm-large-cased-config.json",
    "unilm-base-cased":
    "https://unilm.blob.core.windows.net/ckpt/unilm-base-cased-config.json",
    "unilm1-large-cased":
    "https://unilm.blob.core.windows.net/ckpt/unilm1-large-cased-config.json",
    "unilm1-base-cased":
    "https://unilm.blob.core.windows.net/ckpt/unilm1-base-cased-config.json",
    "unilm1.2-base-uncased":
    "https://unilm.blob.core.windows.net/ckpt/unilm1.2-base-uncased-config.json",
    "cnndm-unilm-base-cased":
    "https://huggingface.co/fuliucansheng/unilm/resolve/main/cnndm-unilm-base-cased-config.json"
}


class UnilmConfig(PretrainedConfig):
    r"""
    :class:`~transformers.UnilmConfig` is the configuration class to store the configuration of a
    `UnilmModel`.
    Arguments:
        vocab_size_or_config_json_file: Vocabulary size of `inputs_ids` in `UnilmModel`.
        hidden_size: Size of the encoder layers and the pooler layer.
        num_hidden_layers: Number of hidden layers in the Transformer encoder.
        num_attention_heads: Number of attention heads for each attention layer in
            the Transformer encoder.
        intermediate_size: The size of the "intermediate" (i.e., feed-forward)
            layer in the Transformer encoder.
        hidden_act: The non-linear activation function (function or string) in the
            encoder and pooler. If string, "gelu", "relu", "swish" and "gelu_new" are supported.
        hidden_dropout_prob: The dropout probabilitiy for all fully connected
            layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob: The dropout ratio for the attention
            probabilities.
        max_position_embeddings: The maximum sequence length that this model might
            ever be used with. Typically set this to something large just in case
            (e.g., 512 or 1024 or 2048).
        type_vocab_size: The vocabulary size of the `token_type_ids` passed into
            `UnilmModel`.
        initializer_range: The sttdev of the truncated_normal_initializer for
            initializing all weight matrices.
        layer_norm_eps: The epsilon used by LayerNorm.
    """
    pretrained_config_archive_map = UNILM_PRETRAINED_CONFIG_ARCHIVE_MAP

    def __init__(
        self,
        vocab_size=28996,
        hidden_size=768,
        num_hidden_layers=12,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=512,
        type_vocab_size=6,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        source_type_id=0,
        target_type_id=1,
        bos_token_id=101,
        mask_token_id=103,
        eos_token_id=102,
        pad_token_id=0,
        **kwargs,
    ):
        super(UnilmConfig, self).__init__(**kwargs)
        self.bos_token_id = bos_token_id
        self.mask_token_id = mask_token_id
        self.eos_token_id = eos_token_id
        self.pad_token_id = pad_token_id
        if isinstance(vocab_size,
                      str) or (sys.version_info[0] == 2
                               and isinstance(vocab_size, unicode)):
            with open(vocab_size, "r", encoding="utf-8") as reader:
                json_config = json.loads(reader.read())
            for key, value in json_config.items():
                self.__dict__[key] = value
        elif isinstance(vocab_size, int):
            self.vocab_size = vocab_size
            self.hidden_size = hidden_size
            self.num_hidden_layers = num_hidden_layers
            self.num_attention_heads = num_attention_heads
            self.hidden_act = hidden_act
            self.intermediate_size = intermediate_size
            self.hidden_dropout_prob = hidden_dropout_prob
            self.attention_probs_dropout_prob = attention_probs_dropout_prob
            self.max_position_embeddings = max_position_embeddings
            self.type_vocab_size = type_vocab_size
            self.initializer_range = initializer_range
            self.layer_norm_eps = layer_norm_eps
            self.source_type_id = source_type_id
            self.target_type_id = target_type_id
        else:
            raise ValueError(
                "First argument must be either a vocabulary size (int)"
                " or the path to a pretrained model config file (str)")

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path,
                        **kwargs) -> "PretrainedConfig":
        if pretrained_model_name_or_path in cls.pretrained_config_archive_map:
            pretrained_model_name_or_path = cls.pretrained_config_archive_map[
                pretrained_model_name_or_path]
        return super().from_pretrained(pretrained_model_name_or_path, **kwargs)