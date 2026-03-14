"""Integration-service seed for pricing_exception_request."""

from __future__ import annotations


DOC_ID = "pricing_exception_request"
INTEGRATION_RULES = {'external_refs': [], 'sync_rules': []}

class IntegrationService:
    def sync_rules(self) -> list:
        return INTEGRATION_RULES.get("sync_rules", [])

    def integration_profile(self) -> dict:
        return {'external_sync_enabled': False}
