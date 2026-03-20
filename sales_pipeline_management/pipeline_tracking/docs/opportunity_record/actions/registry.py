"""Action registry seed for opportunity_record."""

from __future__ import annotations

from typing import Any


DOC_ID = "opportunity_record"
ALLOWED_ACTIONS = ['create', 'update', 'review', 'advance', 'win', 'lose', 'archive']
ACTION_RULES: dict[str, dict[str, Any]] = {'create': {'allowed_in_states': ['identified', 'qualified', 'proposal', 'negotiation', 'won', 'lost'], 'transitions_to': None}, 'update': {'allowed_in_states': ['identified', 'qualified', 'proposal', 'negotiation', 'won', 'lost'], 'transitions_to': None}, 'review': {'allowed_in_states': ['identified', 'qualified', 'proposal', 'negotiation', 'won', 'lost'], 'transitions_to': None}, 'advance': {'allowed_in_states': ['identified', 'qualified', 'proposal', 'negotiation', 'won', 'lost'], 'transitions_to': None}, 'win': {'allowed_in_states': ['identified', 'qualified', 'proposal', 'negotiation', 'won', 'lost'], 'transitions_to': None}, 'lose': {'allowed_in_states': ['identified', 'qualified', 'proposal', 'negotiation', 'won', 'lost'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['identified', 'qualified', 'proposal', 'negotiation', 'won', 'lost'], 'transitions_to': 'archived'}}

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
