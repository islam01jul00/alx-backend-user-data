#!/usr/bin/env python3
"""
basic_auth.py
"""
from api.v1.auth.auth import Auth
import base64
import re


class BasicAuth(Auth):
    """
    BasicAuth
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        extract_base64_authorization_header
        """
        if type(authorization_header) is str:
            pattern = r"^Basic ([^\s]+)$"
            match = re.search(pattern, authorization_header)

            if match:
                return match.group(1)

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        decode_base64_authorization_header
        """
        if type(base64_authorization_header) is str:
            try:
                return base64.b64decode(
                    base64_authorization_header).decode("utf-8")
            except (Exception):
                pass

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        extract_user_credentials
        """

        if type(decoded_base64_authorization_header) is str:
            pattren = r"^([^\s]+):([^\s]+)$"
            match = re.search(pattren, decoded_base64_authorization_header)

            if match:
                return match.group(1), match.group(2)

        return None, None
