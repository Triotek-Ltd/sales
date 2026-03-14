"""Action registry seed for lead_record."""

from __future__ import annotations


DOC_ID = "lead_record"
ALLOWED_ACTIONS = ['create', 'update', 'assign', 'qualify', 'disqualify', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'update': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'qualify': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'disqualify': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': 'archived'}}

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
