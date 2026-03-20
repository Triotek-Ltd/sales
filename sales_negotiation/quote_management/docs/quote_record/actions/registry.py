"""Action registry seed for quote_record."""

from __future__ import annotations

from typing import Any


DOC_ID = "quote_record"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'issue', 'accept', 'expire', 'cancel', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': 'approved'}, 'issue': {'allowed_in_states': ['approved'], 'transitions_to': None}, 'accept': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'expire': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'cancel': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
