"""Action handler seed for qualification_case:review."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "qualification_case"
ACTION_ID = "review"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['open', 'in_review', 'qualified', 'disqualified'], 'transitions_to': 'in_review'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'turn raw prospects into qualified leads with documented outreach and qualification evidence', 'actors': ['sales rep', 'sales manager', 'reviewer'], 'start_condition': 'a target customer or lead source is identified', 'ordered_steps': ['Open and progress the qualification case.'], 'primary_actions': ['create', 'assign', 'qualify', 'disqualify', 'close'], 'primary_transitions': ['qualification_case: opened -> in_review -> qualified or disqualified -> closed'], 'downstream_effects': ['feeds opportunity, negotiation, and forecast workflows'], 'action_actors': {'create': ['sales rep'], 'assign': ['sales rep'], 'review': ['reviewer'], 'close': ['sales manager'], 'archive': ['sales manager']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
