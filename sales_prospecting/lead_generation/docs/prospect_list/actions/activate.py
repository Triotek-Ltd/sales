"""Action handler seed for prospect_list:activate."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "prospect_list"
ACTION_ID = "activate"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft'], 'transitions_to': 'active'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['lead_record', 'outreach_activity'], 'borrowed_fields': ['segment or campaign context from marketing docs'], 'inferred_roles': ['account owner']}, 'actors': ['account owner'], 'action_actors': {'create': ['account owner'], 'review': ['account owner'], 'activate': ['account owner'], 'close': ['account owner'], 'archive': ['account owner']}}

def handle_activate(payload: dict, context: dict | None = None) -> dict:
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
