"""
Deterministic fixture data for demo mode.

Provides realistic data matching actual distributions so the app works
without a live database or LLM connection. Every service method has a
matching fixture function.
"""

import uuid
from datetime import datetime

# =============================================================================
# Dashboard Fixtures
# =============================================================================


_MONTHLY_TRENDS = [
    {"label": "2024-01", "value": 385},
    {"label": "2024-02", "value": 410},
    {"label": "2024-03", "value": 392},
    {"label": "2024-04", "value": 428},
    {"label": "2024-05", "value": 445},
    {"label": "2024-06", "value": 460},
    {"label": "2024-07", "value": 475},
    {"label": "2024-08", "value": 510},
    {"label": "2024-09", "value": 498},
    {"label": "2024-10", "value": 520},
    {"label": "2024-11", "value": 545},
    {"label": "2024-12", "value": 580},
    {"label": "2025-01", "value": 560},
    {"label": "2025-02", "value": 590},
    {"label": "2025-03", "value": 610},
    {"label": "2025-04", "value": 625},
    {"label": "2025-05", "value": 640},
    {"label": "2025-06", "value": 655},
    {"label": "2025-07", "value": 660},
    {"label": "2025-08", "value": 670},
    {"label": "2025-09", "value": 685},
    {"label": "2025-10", "value": 700},
    {"label": "2025-11", "value": 715},
    {"label": "2025-12", "value": 690, "predicted": 720},
]

_AT_RISK_ACCOUNTS = [
    {
        "account_id": "ACC_00004217",
        "email": "maria.santos@email.com",
        "churn_probability": 0.94,
        "risk_tier": "high",
        "plan_type": "Regular",
        "tenure_days": 245,
        "last_payment_days": 38,
        "last_stream_days": 22,
        "open_tickets": 3,
        "top_drivers": ["payment_failure_rate", "days_since_last_stream", "support_ticket_count"],
    },
    {
        "account_id": "ACC_00012843",
        "email": "james.wilson@email.com",
        "churn_probability": 0.91,
        "risk_tier": "high",
        "plan_type": "Premium",
        "tenure_days": 89,
        "last_payment_days": 45,
        "last_stream_days": 31,
        "open_tickets": 2,
        "top_drivers": ["payment_failure_rate", "watch_hours_decline_pct", "tenure_days"],
    },
    {
        "account_id": "ACC_00008391",
        "email": "sarah.chen@email.com",
        "churn_probability": 0.88,
        "risk_tier": "high",
        "plan_type": "Premium-Multi-Screen",
        "tenure_days": 412,
        "last_payment_days": 12,
        "last_stream_days": 45,
        "open_tickets": 0,
        "top_drivers": ["days_since_last_stream", "watch_hours_decline_pct", "content_diversity_drop"],
    },
    {
        "account_id": "ACC_00019502",
        "email": "alex.kumar@email.com",
        "churn_probability": 0.86,
        "risk_tier": "high",
        "plan_type": "Regular",
        "tenure_days": 156,
        "last_payment_days": 8,
        "last_stream_days": 28,
        "open_tickets": 4,
        "top_drivers": ["support_ticket_count", "avg_resolution_hours", "support_escalation_rate"],
    },
    {
        "account_id": "ACC_00003674",
        "email": "emma.johnson@email.com",
        "churn_probability": 0.84,
        "risk_tier": "high",
        "plan_type": "Regular",
        "tenure_days": 67,
        "last_payment_days": 5,
        "last_stream_days": 14,
        "open_tickets": 1,
        "top_drivers": ["watch_hours_decline_pct", "session_frequency_drop", "tenure_days"],
    },
    {
        "account_id": "ACC_00027156",
        "email": "david.martinez@email.com",
        "churn_probability": 0.82,
        "risk_tier": "high",
        "plan_type": "Premium",
        "tenure_days": 534,
        "last_payment_days": 30,
        "last_stream_days": 18,
        "open_tickets": 1,
        "top_drivers": ["payment_failure_rate", "plan_downgrade_flag", "watch_hours_decline_pct"],
    },
    {
        "account_id": "ACC_00015829",
        "email": "lisa.park@email.com",
        "churn_probability": 0.79,
        "risk_tier": "high",
        "plan_type": "Regular",
        "tenure_days": 198,
        "last_payment_days": 15,
        "last_stream_days": 35,
        "open_tickets": 0,
        "top_drivers": ["days_since_last_stream", "content_diversity_drop", "watchlist_abandonment"],
    },
    {
        "account_id": "ACC_00031247",
        "email": "tom.nguyen@email.com",
        "churn_probability": 0.76,
        "risk_tier": "high",
        "plan_type": "Premium-Multi-Screen",
        "tenure_days": 310,
        "last_payment_days": 10,
        "last_stream_days": 8,
        "open_tickets": 2,
        "top_drivers": ["support_ticket_count", "payment_failure_rate", "plan_downgrade_flag"],
    },
    {
        "account_id": "ACC_00009812",
        "email": "rachel.brown@email.com",
        "churn_probability": 0.73,
        "risk_tier": "high",
        "plan_type": "Regular",
        "tenure_days": 121,
        "last_payment_days": 7,
        "last_stream_days": 19,
        "open_tickets": 0,
        "top_drivers": ["watch_hours_decline_pct", "session_frequency_drop", "device_count_drop"],
    },
    {
        "account_id": "ACC_00022485",
        "email": "michael.lee@email.com",
        "churn_probability": 0.71,
        "risk_tier": "high",
        "plan_type": "Premium",
        "tenure_days": 445,
        "last_payment_days": 5,
        "last_stream_days": 12,
        "open_tickets": 1,
        "top_drivers": ["content_diversity_drop", "days_since_last_stream", "watch_hours_decline_pct"],
    },
    # Medium risk
    {
        "account_id": "ACC_00041283",
        "email": "jennifer.davis@email.com",
        "churn_probability": 0.62,
        "risk_tier": "medium",
        "plan_type": "Regular",
        "tenure_days": 287,
        "last_payment_days": 3,
        "last_stream_days": 10,
        "open_tickets": 1,
        "top_drivers": ["watch_hours_decline_pct", "session_frequency_drop", "content_diversity_drop"],
    },
    {
        "account_id": "ACC_00038917",
        "email": "robert.taylor@email.com",
        "churn_probability": 0.58,
        "risk_tier": "medium",
        "plan_type": "Premium",
        "tenure_days": 178,
        "last_payment_days": 8,
        "last_stream_days": 6,
        "open_tickets": 0,
        "top_drivers": ["tenure_days", "watch_hours_decline_pct", "payment_method_change"],
    },
    {
        "account_id": "ACC_00044562",
        "email": "amy.white@email.com",
        "churn_probability": 0.55,
        "risk_tier": "medium",
        "plan_type": "Regular",
        "tenure_days": 365,
        "last_payment_days": 2,
        "last_stream_days": 15,
        "open_tickets": 2,
        "top_drivers": ["support_ticket_count", "days_since_last_stream", "watch_hours_decline_pct"],
    },
    {
        "account_id": "ACC_00050231",
        "email": "chris.garcia@email.com",
        "churn_probability": 0.51,
        "risk_tier": "medium",
        "plan_type": "Premium-Multi-Screen",
        "tenure_days": 520,
        "last_payment_days": 5,
        "last_stream_days": 9,
        "open_tickets": 0,
        "top_drivers": ["content_diversity_drop", "session_frequency_drop", "device_count_drop"],
    },
    {
        "account_id": "ACC_00046789",
        "email": "nicole.miller@email.com",
        "churn_probability": 0.47,
        "risk_tier": "medium",
        "plan_type": "Regular",
        "tenure_days": 142,
        "last_payment_days": 4,
        "last_stream_days": 7,
        "open_tickets": 1,
        "top_drivers": ["watch_hours_decline_pct", "tenure_days", "payment_method_change"],
    },
]

_SHAP_GLOBAL = [
    {"feature": "payment_failure_rate", "importance": 0.142, "direction": "positive"},
    {"feature": "days_since_last_stream", "importance": 0.128, "direction": "positive"},
    {"feature": "watch_hours_decline_pct", "importance": 0.115, "direction": "positive"},
    {"feature": "support_ticket_count", "importance": 0.098, "direction": "positive"},
    {"feature": "tenure_days", "importance": 0.087, "direction": "negative"},
    {"feature": "session_frequency_drop", "importance": 0.076, "direction": "positive"},
    {"feature": "content_diversity_drop", "importance": 0.065, "direction": "positive"},
    {"feature": "avg_resolution_hours", "importance": 0.054, "direction": "positive"},
    {"feature": "plan_downgrade_flag", "importance": 0.048, "direction": "positive"},
    {"feature": "device_count_drop", "importance": 0.039, "direction": "positive"},
]

_INTERVENTIONS: list[dict] = [
    {
        "id": "d3f8a1b2-4c5e-6f7a-8b9c-0d1e2f3a4b5c",
        "account_id": "ACC_00004217",
        "strategy": "payment_recovery",
        "status": "pending",
        "subject": "Let's get your account back on track",
        "body_html": (
            "<html><body style='font-family:DM Sans,sans-serif;'>"
            "<p>Hi Maria,</p>"
            "<p>We noticed your recent payment didn't go through. We'd hate for you "
            "to lose access to your favorite shows — especially with the new season "
            "of <em>Midnight Horizon</em> dropping next week.</p>"
            "<p>Updating your payment method takes less than a minute:</p>"
            "<p><a href='https://retain.example.com/billing' "
            "style='background:#6366f1;color:white;padding:12px 24px;"
            "border-radius:8px;text-decoration:none;'>Update Payment →</a></p>"
            "<p>If you're experiencing any issues, our support team is standing by "
            "to help.</p>"
            "<p>Best,<br/>The Retain Team</p>"
            "</body></html>"
        ),
        "body_plaintext": (
            "Hi Maria,\n\n"
            "We noticed your recent payment didn't go through. We'd hate for you "
            "to lose access to your favorite shows — especially with the new season "
            "of Midnight Horizon dropping next week.\n\n"
            "Update your payment method here: https://retain.example.com/billing\n\n"
            "If you're experiencing any issues, our support team is standing by.\n\n"
            "Best,\nThe Retain Team"
        ),
        "agent_rationale": (
            "Maria's account shows 3 consecutive failed payments over the last 38 days "
            "with an active viewing history prior to the payment issues. The account has "
            "3 open support tickets, suggesting she may be aware of the issue. A direct, "
            "empathetic payment recovery email is the highest-priority intervention."
        ),
        "created_at": "2025-12-01T10:30:00",
        "updated_at": "2025-12-01T10:30:00",
    },
    {
        "id": "e4a9b2c3-5d6f-7a8b-9c0d-1e2f3a4b5c6d",
        "account_id": "ACC_00008391",
        "strategy": "engagement_reignite",
        "status": "pending",
        "subject": "We've been saving something special for you",
        "body_html": (
            "<html><body style='font-family:DM Sans,sans-serif;'>"
            "<p>Hey Sarah,</p>"
            "<p>It's been a while since your last stream, and we've been adding "
            "incredible new content in the genres you love most — thriller and "
            "sci-fi.</p>"
            "<p>Here are 3 picks we think you'll love:</p>"
            "<ul><li><strong>Quantum Drift</strong> — A mind-bending sci-fi thriller</li>"
            "<li><strong>The Last Signal</strong> — Edge-of-your-seat suspense</li>"
            "<li><strong>Neon Requiem</strong> — Cyberpunk noir at its finest</li></ul>"
            "<p><a href='https://retain.example.com/browse?for=ACC_00008391' "
            "style='background:#6366f1;color:white;padding:12px 24px;"
            "border-radius:8px;text-decoration:none;'>Start Watching →</a></p>"
            "<p>Happy streaming,<br/>The Retain Team</p>"
            "</body></html>"
        ),
        "body_plaintext": (
            "Hey Sarah,\n\n"
            "It's been a while since your last stream, and we've been adding "
            "incredible new content in the genres you love most — thriller and sci-fi.\n\n"
            "Here are 3 picks we think you'll love:\n"
            "- Quantum Drift — A mind-bending sci-fi thriller\n"
            "- The Last Signal — Edge-of-your-seat suspense\n"
            "- Neon Requiem — Cyberpunk noir at its finest\n\n"
            "Start watching: https://retain.example.com/browse?for=ACC_00008391\n\n"
            "Happy streaming,\nThe Retain Team"
        ),
        "agent_rationale": (
            "Sarah is a long-tenured Premium-Multi-Screen subscriber (412 days) "
            "whose streaming activity dropped off 45 days ago despite no payment or "
            "support issues. Content discovery is the ideal angle — she likely hasn't "
            "seen new additions matching her preferences."
        ),
        "created_at": "2025-12-01T10:35:00",
        "updated_at": "2025-12-01T10:35:00",
    },
    {
        "id": "f5b0c3d4-6e7a-8b9c-0d1e-2f3a4b5c6d7e",
        "account_id": "ACC_00019502",
        "strategy": "vip_support_rescue",
        "status": "approved",
        "subject": "We hear you — and we're making it right",
        "body_html": (
            "<html><body style='font-family:DM Sans,sans-serif;'>"
            "<p>Hi Alex,</p>"
            "<p>We know your recent experience with our support team hasn't been "
            "up to standard, and we sincerely apologize. You deserve better.</p>"
            "<p>We've assigned a dedicated support specialist to your account who "
            "will personally resolve your open tickets within the next 24 hours.</p>"
            "<p><a href='https://retain.example.com/support/vip' "
            "style='background:#6366f1;color:white;padding:12px 24px;"
            "border-radius:8px;text-decoration:none;'>Chat with Your Specialist →</a></p>"
            "<p>As a gesture of goodwill, we've also added a free month to your subscription.</p>"
            "<p>With appreciation,<br/>The Retain Team</p>"
            "</body></html>"
        ),
        "body_plaintext": (
            "Hi Alex,\n\n"
            "We know your recent experience with our support team hasn't been up to "
            "standard, and we sincerely apologize. You deserve better.\n\n"
            "We've assigned a dedicated support specialist to your account who will "
            "personally resolve your open tickets within the next 24 hours.\n\n"
            "Chat with your specialist: https://retain.example.com/support/vip\n\n"
            "As a gesture of goodwill, we've also added a free month to your subscription.\n\n"
            "With appreciation,\nThe Retain Team"
        ),
        "agent_rationale": (
            "Alex has 4 open support tickets with an average resolution time well above "
            "normal. The escalation rate is high, suggesting frustration. VIP support "
            "rescue with a personal touch and compensation is critical to retain this customer."
        ),
        "created_at": "2025-12-01T09:15:00",
        "updated_at": "2025-12-01T11:00:00",
    },
    {
        "id": "a6c1d4e5-7f8a-9b0c-1d2e-3f4a5b6c7d8e",
        "account_id": "ACC_00012843",
        "strategy": "payment_recovery",
        "status": "sent",
        "subject": "Quick fix needed for your subscription",
        "body_html": (
            "<html><body style='font-family:DM Sans,sans-serif;'>"
            "<p>Hi James,</p>"
            "<p>Your Premium subscription payment was declined on November 25th. "
            "To avoid any interruption to your service, please update your payment "
            "details.</p>"
            "<p><a href='https://retain.example.com/billing' "
            "style='background:#6366f1;color:white;padding:12px 24px;"
            "border-radius:8px;text-decoration:none;'>Fix Payment →</a></p>"
            "<p>Questions? Reply to this email — we're here to help.</p>"
            "<p>Cheers,<br/>The Retain Team</p>"
            "</body></html>"
        ),
        "body_plaintext": (
            "Hi James,\n\nYour Premium subscription payment was declined on November "
            "25th. To avoid any interruption, please update your payment details.\n\n"
            "Fix payment: https://retain.example.com/billing\n\n"
            "Questions? Reply to this email.\n\nCheers,\nThe Retain Team"
        ),
        "agent_rationale": (
            "James is a relatively new Premium subscriber (89 days) with a 45-day "
            "payment gap. The payment method likely expired or was declined. A concise, "
            "urgent payment recovery message is appropriate."
        ),
        "created_at": "2025-11-28T14:20:00",
        "updated_at": "2025-11-29T09:00:00",
    },
]


# =============================================================================
# Fixture Functions
# =============================================================================


def get_fixture_kpis() -> dict:
    """Return dashboard KPI fixture data."""
    return {
        "total_accounts": 60000,
        "active_subscribers": 49684,
        "churned_accounts": 10316,
        "churn_rate_30d": 0.049,
        "high_risk_count": 2420,
        "at_risk_mrr": 33_880.00,
        "cac": 45.00,
        "retention_cost_per_save": 12.50,
    }


def get_fixture_trends() -> list[dict]:
    """Return monthly trend fixture data."""
    return list(_MONTHLY_TRENDS)


def get_fixture_risk_distribution() -> dict:
    """Return risk distribution fixture data."""
    return {"low": 53760, "medium": 3820, "high": 2420}


def get_fixture_active_inactive() -> dict:
    """Return active vs inactive distribution."""
    return {
        "active": 49684,
        "inactive": 10316,
        "recent_churn_30d": 690,
    }


def get_fixture_executive_summary() -> dict:
    """Return AI executive summary fixture."""
    return {
        "title": "Subscriber Health Summary",
        "content": (
            "The platform currently serves **49,684 active subscribers** across "
            "60,000 total accounts. The 30-day predicted churn rate stands at "
            "**4.9%**, up from 4.4% last quarter — a trend worth monitoring.\n\n"
            "**Key findings:**\n\n"
            "- **2,420 accounts** are flagged as high-risk, representing "
            "**$33,880 in monthly recurring revenue** at risk\n"
            "- Payment failures are the #1 churn driver this month, affecting "
            "38% of high-risk accounts\n"
            "- Engagement drop-off is accelerating among Regular plan subscribers, "
            "particularly those in the 3-6 month tenure bracket\n"
            "- Premium-Multi-Screen subscribers show the strongest retention "
            "(97.2% rate), while Regular plan churn has risen to 5.8%\n\n"
            "**Recommended focus areas:**\n\n"
            "1. Prioritize payment recovery outreach for the 920 accounts with "
            "failed payments — estimated save rate of 62% if contacted within 48 hours\n"
            "2. Deploy re-engagement campaigns for the 680 disengaged accounts "
            "before they reach the 30-day inactivity cliff\n"
            "3. Review support ticket backlog — 4 accounts have 3+ unresolved "
            "tickets and are at critical risk"
        ),
        "timestamp": "2025-12-01T10:00:00",
    }


def get_fixture_at_risk_accounts(
    risk_tier: str | None = None,
    plan_type: str | None = None,
    sort_by: str = "churn_probability",
    page: int = 1,
    per_page: int = 20,
) -> dict:
    """Return paginated at-risk accounts fixture."""
    accounts = list(_AT_RISK_ACCOUNTS)

    if risk_tier and risk_tier != "all":
        accounts = [a for a in accounts if a["risk_tier"] == risk_tier]
    if plan_type and plan_type != "all":
        accounts = [a for a in accounts if a["plan_type"] == plan_type]

    reverse = sort_by in ("churn_probability",)
    accounts.sort(key=lambda a: a.get(sort_by, 0), reverse=reverse)

    total = len(accounts)
    start = (page - 1) * per_page
    end = start + per_page
    items = accounts[start:end]

    return {"items": items, "total": total, "page": page, "per_page": per_page}


def get_fixture_account_detail(account_id: str) -> dict | None:
    """Return detailed account fixture data."""
    account = next(
        (a for a in _AT_RISK_ACCOUNTS if a["account_id"] == account_id),
        None,
    )
    if account is None:
        return None

    return {
        **account,
        "recent_payments": [
            {
                "date": "2025-11-01",
                "amount": 14.99,
                "status": "success",
                "method": "credit_card",
            },
            {
                "date": "2025-10-01",
                "amount": 14.99,
                "status": "failed",
                "method": "credit_card",
            },
        ],
        "recent_tickets": [
            {
                "id": "TKT_001",
                "date": "2025-11-20",
                "subject": "Billing issue",
                "status": "open",
                "priority": "high",
            },
        ],
        "watch_hours_30d": 4.2,
        "watch_hours_90d": 28.5,
        "sessions_30d": 6,
        "content_categories": ["thriller", "sci-fi", "drama"],
    }


def get_fixture_account_shap(account_id: str) -> list[dict] | None:
    """Return SHAP values fixture for an account as SHAPFeature list."""
    account = next(
        (a for a in _AT_RISK_ACCOUNTS if a["account_id"] == account_id),
        None,
    )
    if account is None:
        return None

    features = []
    for i, driver in enumerate(account["top_drivers"]):
        features.append({
            "feature": driver,
            "importance": round(0.15 - i * 0.02, 4),
            "direction": "negative" if driver == "tenure_days" else "positive",
        })
    return features


def get_fixture_analytics_overview() -> dict:
    """Return analytics overview bundle."""
    return {
        "kpis": get_fixture_kpis(),
        "risk_distribution": get_fixture_risk_distribution(),
        "top_shap_features": _SHAP_GLOBAL,
    }


def get_fixture_churn_trends(months: int = 12) -> list[dict]:
    """Return churn trend time series."""
    trends = get_fixture_trends()
    return trends[-months:]


def get_fixture_segments() -> dict:
    """Return segment breakdowns."""
    return {
        "by_plan": [
            {"plan": "Regular", "count": 38400, "churn_rate": 0.058},
            {"plan": "Premium", "count": 15600, "churn_rate": 0.040},
            {"plan": "Premium-Multi-Screen", "count": 6000, "churn_rate": 0.028},
        ],
        "by_tenure": [
            {"plan": "0-3 months", "count": 8400, "churn_rate": 0.080},
            {"plan": "3-6 months", "count": 12000, "churn_rate": 0.064},
            {"plan": "6-12 months", "count": 18000, "churn_rate": 0.040},
            {"plan": "12+ months", "count": 21600, "churn_rate": 0.030},
        ],
    }


def get_fixture_model_performance() -> dict:
    """Return model performance metrics."""
    return {
        "auc_roc": 0.891,
        "precision": 0.823,
        "recall": 0.756,
        "f1_score": 0.788,
        "log_loss": 0.412,
        "calibration_error": 0.034,
        "last_trained": "2025-11-28T14:30:00",
        "training_samples": 48000,
    }


def get_fixture_drift_status() -> dict:
    """Return drift monitoring status."""
    return {
        "overall_status": "ok",
        "features": [
            {"feature": "payment_failure_rate", "psi": 0.032, "status": "ok"},
            {"feature": "days_since_last_stream", "psi": 0.045, "status": "ok"},
            {"feature": "watch_hours_decline_pct", "psi": 0.028, "status": "ok"},
            {"feature": "support_ticket_count", "psi": 0.091, "status": "ok"},
            {"feature": "tenure_days", "psi": 0.015, "status": "ok"},
            {"feature": "session_frequency_drop", "psi": 0.112, "status": "warning"},
        ],
        "last_checked": "2025-12-01T08:00:00",
    }


def get_fixture_shap_global() -> list[dict]:
    """Return global SHAP feature importance."""
    return list(_SHAP_GLOBAL)


def get_fixture_prescriptions() -> list[dict]:
    """Return prescription groups."""
    high_risk = [a for a in _AT_RISK_ACCOUNTS if a["risk_tier"] == "high"]

    payment_accts = [a for a in high_risk if "payment_failure_rate" in a["top_drivers"]]
    engagement_accts = [a for a in high_risk if "days_since_last_stream" in a["top_drivers"] or "watch_hours_decline_pct" in a["top_drivers"]]
    support_accts = [a for a in high_risk if "support_ticket_count" in a["top_drivers"]]
    content_accts = [a for a in high_risk if "content_diversity_drop" in a["top_drivers"]]

    return [
        {
            "strategy": "payment_recovery",
            "display_name": "Payment Recovery",
            "account_count": max(len(payment_accts), 920),
            "estimated_mrr": 12_880.00,
            "accounts": payment_accts,
        },
        {
            "strategy": "engagement_reignite",
            "display_name": "Re-engagement Campaign",
            "account_count": max(len(engagement_accts), 680),
            "estimated_mrr": 9_520.00,
            "accounts": engagement_accts,
        },
        {
            "strategy": "vip_support_rescue",
            "display_name": "Support Escalation",
            "account_count": max(len(support_accts), 340),
            "estimated_mrr": 4_760.00,
            "accounts": support_accts,
        },
        {
            "strategy": "content_discovery",
            "display_name": "Content Recommendation",
            "account_count": max(len(content_accts), 480),
            "estimated_mrr": 6_720.00,
            "accounts": content_accts,
        },
    ]


def get_fixture_prescription_by_strategy(strategy: str) -> dict | None:
    """Return a single prescription group by strategy."""
    groups = get_fixture_prescriptions()
    return next((g for g in groups if g["strategy"] == strategy), None)


def get_fixture_interventions(status: str | None = None) -> list[dict]:
    """Return intervention drafts, optionally filtered by status."""
    items = list(_INTERVENTIONS)
    if status:
        items = [i for i in items if i["status"] == status]
    return items


def get_fixture_intervention(intervention_id: str) -> dict | None:
    """Return a single intervention by ID."""
    return next(
        (i for i in _INTERVENTIONS if i["id"] == intervention_id),
        None,
    )


def create_fixture_intervention(account_id: str, strategy: str) -> dict:
    """Create a new fixture intervention draft."""
    new_id = str(uuid.uuid4())
    now = datetime.now().isoformat()

    account = next(
        (a for a in _AT_RISK_ACCOUNTS if a["account_id"] == account_id),
        None,
    )
    email = account["email"] if account else "customer@email.com"
    name = email.split("@")[0].replace(".", " ").title()

    return {
        "id": new_id,
        "account_id": account_id,
        "strategy": strategy,
        "status": "pending",
        "subject": "We want to keep you — here's what we can do",
        "body_html": (
            f"<html><body style='font-family:DM Sans,sans-serif;'>"
            f"<p>Hi {name},</p>"
            f"<p>We've noticed some changes in your account and want to make sure "
            f"you're getting the most out of your subscription.</p>"
            f"<p><a href='https://retain.example.com/offer/{account_id}' "
            f"style='background:#6366f1;color:white;padding:12px 24px;"
            f"border-radius:8px;text-decoration:none;'>See Your Options →</a></p>"
            f"<p>Best,<br/>The Retain Team</p>"
            f"</body></html>"
        ),
        "body_plaintext": (
            f"Hi {name},\n\n"
            f"We've noticed some changes in your account and want to make sure "
            f"you're getting the most out of your subscription.\n\n"
            f"See your options: https://retain.example.com/offer/{account_id}\n\n"
            f"Best,\nThe Retain Team"
        ),
        "agent_rationale": (
            f"Account {account_id} was flagged for {strategy} intervention based on "
            f"predictive churn analysis. The selected strategy addresses the primary "
            f"risk factors identified in the account's feature profile."
        ),
        "created_at": now,
        "updated_at": now,
    }
