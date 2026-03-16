"""Action handler seed for quote_record:cancel."""

from __future__ import annotations


DOC_ID = "quote_record"
ACTION_ID = "cancel"
ACTION_RULE = {'allowed_in_states': ['draft', 'submitted', 'approved', 'accepted', 'expired', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'manage proposal revisions, negotiation decisions, and final agreement closure with a prospect', 'actors': ['sales rep', 'approver', 'customer negotiator'], 'start_condition': 'a proposal is presented to a prospect', 'ordered_steps': ['Issue the sales proposal and opening quote.', 'Revise quote and commercial terms as needed.'], 'primary_actions': ['create', 'review', 'issue', 'update', 'approve'], 'primary_transitions': ['quote_record: draft -> active', 'quote_record: active -> revised -> approved'], 'downstream_effects': ['feeds order capture, billing, and relationship management'], 'action_actors': {'create': ['sales rep'], 'review': ['approver'], 'approve': ['approver'], 'issue': ['sales rep'], 'cancel': ['sales rep'], 'archive': ['sales rep']}}

def handle_cancel(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
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
