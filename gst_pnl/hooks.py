# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "gst_pnl"
app_title = "Erpnext Gst Tax Ledger Pnl Analytics"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Gst Tax Ledger Pnl Analytics for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/gst_pnl/css/gst_pnl.bundle.css"
app_include_js = "/assets/gst_pnl/js/gst_pnl.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "gst_pnl.engine.on_document_submit",
        "on_cancel": "gst_pnl.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "gst_pnl.engine.daily_scheduled_sync"
    ]
}
