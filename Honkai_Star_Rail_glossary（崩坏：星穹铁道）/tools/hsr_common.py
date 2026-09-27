#!/usr/bin/env python3
"""Shared helpers for the Honkai: Star Rail terminology build (TextMap hashing, cleaning)."""

from __future__ import annotations

import html
import re
import struct

_MASK = (1 << 64) - 1
_P1 = 0x9E3779B185EBCA87
_P2 = 0xC2B2AE3D27D4EB4F
_P3 = 0x165667B19E3779F9
_P4 = 0x85EBCA77C2B2AE63
_P5 = 0x27D4EB2F165667C5


def _rotl(value: int, bits: int) -> int:
    return ((value << bits) | (value >> (64 - bits))) & _MASK


def xxh64(data: str | bytes, seed: int = 0) -> int:
    """Reference xxHash64 (the hash used by HoYoverse TextMap keys)."""
    buf = data.encode("utf-8") if isinstance(data, str) else data
    length = len(buf)
    index = 0

    if length >= 32:
        v1 = (seed + _P1 + _P2) & _MASK
        v2 = (seed + _P2) & _MASK
        v3 = seed & _MASK
        v4 = (seed - _P1) & _MASK
        while index + 32 <= length:
            v1 = (_rotl((v1 + struct.unpack_from("<Q", buf, index)[0] * _P2) & _MASK, 31) * _P1) & _MASK
            index += 8
            v2 = (_rotl((v2 + struct.unpack_from("<Q", buf, index)[0] * _P2) & _MASK, 31) * _P1) & _MASK
            index += 8
            v3 = (_rotl((v3 + struct.unpack_from("<Q", buf, index)[0] * _P2) & _MASK, 31) * _P1) & _MASK
            index += 8
            v4 = (_rotl((v4 + struct.unpack_from("<Q", buf, index)[0] * _P2) & _MASK, 31) * _P1) & _MASK
            index += 8
        acc = (_rotl(v1, 1) + _rotl(v2, 7) + _rotl(v3, 12) + _rotl(v4, 18)) & _MASK
        for part in (v1, v2, v3, v4):
            acc = ((acc ^ ((_rotl((part * _P2) & _MASK, 31) * _P1) & _MASK)) * _P1 + _P4) & _MASK
    else:
        acc = (seed + _P5) & _MASK

    acc = (acc + length) & _MASK

    while index + 8 <= length:
        lane = (_rotl((struct.unpack_from("<Q", buf, index)[0] * _P2) & _MASK, 31) * _P1) & _MASK
        acc = ((_rotl(acc ^ lane, 27) * _P1) + _P4) & _MASK
        index += 8
    if index + 4 <= length:
        acc = ((_rotl(acc ^ ((struct.unpack_from("<I", buf, index)[0] * _P1) & _MASK), 23) * _P2) + _P3) & _MASK
        index += 4
    while index < length:
        acc = (_rotl(acc ^ ((buf[index] * _P5) & _MASK), 11) * _P1) & _MASK
        index += 1

    acc ^= acc >> 33
    acc = (acc * _P2) & _MASK
    acc ^= acc >> 29
    acc = (acc * _P3) & _MASK
    acc ^= acc >> 32
    return acc


_TAG_RE = re.compile(r"<[^>]*>")
_BRACE_RE = re.compile(r"[{}]")
_PARAM_RE = re.compile(r"#\d+\[")
_DANGLING_RE = re.compile(
    r"\b(?:by|of|to|into|and|or|with|from|for|um|de|da|do|der|die|das|una|un|une|le|la|les|des|per)$",
    re.I,
)
_BAD_LITERALS = {"n/a", "na", "none", "null", "undefined", "nil", "-", "--", "/", "\\", "...", "?", "??", "tbd", "todo"}


def text_key(value) -> str | None:
    """Resolve a config field to its TextMap hash string.

    Name-like fields are either {"Hash": <int>} or a raw localization key such as
    "SkillPointName_1001101" that must be hashed with xxh64.
    """
    if isinstance(value, dict):
        hashed = value.get("Hash")
        if isinstance(hashed, int):
            return str(hashed)
        return None
    if isinstance(value, str):
        raw = value.strip()
        if not raw:
            return None
        if raw.isdigit():
            return raw
        return str(xxh64(raw))
    return None


def clean_text(value) -> str:
    """Strip markup from a TextMap/localization string, keep the readable text."""
    if not isinstance(value, str):
        return ""
    text = value.replace("\\n", " ").replace("\u00a0", " ")
    text = html.unescape(text)
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.I)
    text = _TAG_RE.sub("", text)
    # Keep the visible text of furigana annotations, drop the markup itself.
    text = re.sub(r"\{RUBY_B#[^}]*\}", "", text)
    text = text.replace("{RUBY_E#}", "")
    text = text.replace("\\u00a0", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_valid_term(text: str, max_len: int) -> bool:
    if not text or len(text) > max_len:
        return False
    low = text.casefold()
    if low in _BAD_LITERALS:
        return False
    if _BRACE_RE.search(text) or _PARAM_RE.search(text):
        return False
    if "http://" in low or "https://" in low:
        return False
    bare = text.strip('"\u201c\u201d\'\u300c\u300d ')
    if bare.startswith(("@", chr(92), "#", "$")):
        return False
    if not re.search(r"[0-9A-Za-z\u00c0-\u024f\u0370-\u03ff\u0400-\u04ff\u0600-\u06ff\u0900-\u0dff\u0e00-\u0e7f\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]", text):
        return False
    if re.fullmatch(r"[\d\s.,%:/+-]+", text):
        return False
    if _DANGLING_RE.search(text.strip()):
        return False
    return True
