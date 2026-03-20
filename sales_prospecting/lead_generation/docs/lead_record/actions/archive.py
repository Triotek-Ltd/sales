"""Action handler seed for lead_record:archive."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "lead_record"
ACTION_ID = "archive"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['new', 'contacted', 'qualified', 'disqualified'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'turn raw prospects into qualified leads with documented outreach and qualification evidence', 'actors': ['sales rep', 'sales manager', 'reviewer'], 'start_condition': 'a target customer or lead source is identified', 'ordered_steps': ['Capture the lead and basic prospect context.', 'Advance qualified prospects into opportunity management.'], 'primary_actions': ['create', 'update', 'convert', 'close'], 'primary_transitions': ['lead_record: draft -> active', 'lead_record: active -> qualified -> converted'], 'downstream_effects': ['feeds opportunity, negotiation, and forecast workflows'], 'action_actors': {'create': ['sales rep'], 'update': ['sales rep'], 'assign': ['sales rep'], 'archive': ['sales manager']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
