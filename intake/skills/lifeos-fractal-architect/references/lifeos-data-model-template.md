# LifeOS Data Model and Facet Source of Truth

**Purpose:** Define the canonical entities in LifeOS, their fields, their system of record per facet, and the rules for ID minting, lifecycle, and conflict resolution.  
**Owner:** Human (reviewed at monthly cadence; structural changes require human sign-off).

---

## Canonical Entities

### Task

The atomic unit of committed execution.

```yaml
task_id:            string  # minted by GitHub at issue creation; immutable
title:              string  # verb-led, imperative; ACE format required
state:              enum    # inbox | clarified | next | scheduled | inprogress | done | voided | archived
project_id:         string  # reference to owning Project; nullable if orphan task
area_id:            string  # PARA Area; inherited from project if set
estimate:           string  # e.g. "2h", "30m"; required before COG workflow
calendar_event_id:  string  # reference to GCal event; set by COG workflow
note_id:            string  # reference to context note in Obsidian; optional
risk_class:         enum    # reversible-local | reversible-external | irreversible-adjacent | blocked
confidence:         int     # 0–100; last computed confidence for this task's state
human_override_lock: bool   # true if a human manually edited this object (24h window)
sync_locked:        bool    # true if a dependency UUID is missing or reconciliation pending
```

**Canonical systems per facet:**
- Execution state (`state`) → GitHub is canonical. Obsidian is read-only mirror.
- Title, estimate, DoD → GitHub.
- Calendar linkage → Google Calendar mints `event_id`; GitHub stores reference only.
- Narrative context → Obsidian note mints `note_id`; GitHub stores reference only.

---

### Project

A bounded effort with a defined outcome and end condition.

```yaml
project_id:           string  # minted by GitHub at project creation; immutable
name:                 string  # slug format: proj-<topic>--<qualifier>
area_id:              string  # PARA Area this project belongs to
status:               enum    # active | on-hold | done | archived | voided
outcome_definition:   string  # single measurable end state; stored in Obsidian project-note
review_cadence:       enum    # weekly | biweekly | monthly
jd_address:           string  # Johnny Decimal address for Obsidian path
milestone_ids:        list    # references to GitHub milestones for this project
note_id:              string  # reference to Obsidian project-note
```

**Canonical systems per facet:**
- Project status → GitHub.
- Outcome definition → Obsidian project-note.
- Schedule and capacity claims → Google Calendar.

---

### Note

The atomic unit of knowledge.

```yaml
note_id:    string  # minted by Obsidian at note creation; immutable; never rename without redirect
title:      string  # single knowledge claim (Zettelkasten convention)
type:       enum    # fleeting | atom | molecule | project-note | evergreen
jd_address: string  # Johnny Decimal vault address
links_out:  list    # outbound Obsidian links (wikilinks or explicit ids)
links_in:   list    # inbound links (maintained by Obsidian graph)
project_id: string  # optional reference to GitHub project (for project-notes)
task_ids:   list    # optional references to GitHub issues related to this note
created_at: datetime
updated_at: datetime
state:      enum    # inbox | active | archived | quarantine
```

**Type definitions:**
- `fleeting`: raw capture; must be processed within 7 days or flagged stale.
- `atom`: single permanent idea; requires `links_out >= MIN_LINKS_PER_ATOM` (default 2).
- `molecule`: synthesis of 2+ atoms around a theme; `links_out >= 3`.
- `project-note`: context document for a specific GitHub project; carries `project_id`.
- `evergreen`: mature, stable knowledge; title is a stable claim; periodically reviewed.

**Canonical systems per facet:**
- Note content and links → Obsidian is canonical. No other system writes note content.
- `note_id` → Obsidian mints it; GitHub and GCal store reference only.

---

### Event

A time commitment in Google Calendar.

```yaml
event_id:   string    # minted by Google Calendar; immutable
title:      string    # matches linked task title where applicable
start_at:   datetime
end_at:     datetime
task_id:    string    # optional reference to GitHub issue
note_id:    string    # optional reference to Obsidian context note
staged:     bool      # true = Claude-proposed, not yet human-confirmed
confirmed:  bool      # true = human confirmed; false = still staged
```

**Rule:** `staged=true` events are Claude-generated proposals. They must not be treated as committed until `confirmed=true` by human action.

**Canonical systems per facet:**
- Time/capacity → Google Calendar is canonical.
- Obsidian daily note mirrors event summaries (read-only).

---

### Deliverable

A concrete output artifact tied to a project.

```yaml
deliverable_id:       string  # minted by GitHub (PR id or artifact convention)
project_id:           string  # owning project
title:                string
definition_of_done:   string  # explicit, measurable completion statement
evidence_links:       list    # links to artifacts, PRs, notes proving done
state:                enum    # draft | review | done | archived
```

---

### Area

An ongoing life domain with no end date.

```yaml
area_id:     string  # minted in Obsidian vault (JD top-level folder); immutable slug
name:        string  # e.g. "health", "professional", "relationships", "finance"
jd_address:  string  # Johnny Decimal address
projects:    list    # reference list of active project_ids in this area
notes:       list    # reference list of area-scoped atom/molecule notes
```

**Areas are stable containers.** They do not have lifecycle states. They only accumulate or lose projects.

---

## Facet Source of Truth (Master Table)

| Facet | Canonical system | Mirror systems | Sync direction | Conflict winner |
|---|---|---|---|---|
| Object UUIDs / identity | Originating system (minter) | All others (reference only) | Origin → mirror | Origin always wins |
| Task execution state | GitHub | Obsidian (query views) | GitHub → Obsidian | GitHub |
| Project status | GitHub | Obsidian (project-note metadata) | GitHub → Obsidian | GitHub |
| Time / scheduling | Google Calendar | Obsidian daily note | GCal → Obsidian | GCal |
| Narrative / long context | Obsidian | GitHub (snippet + link) | Obsidian → GitHub | Obsidian |
| Note graph | Obsidian | — | — | Obsidian |
| Policy variable registry | Versioned repo doc (`references/`) | — | — | Repo doc |
| Archival execution truth | GitHub (closed/archived issues) | Obsidian archive paths | GitHub → Obsidian | GitHub |

---

## UUID Minting Rules

- **GitHub** mints: `task_id`, `project_id`, `milestone_id`, `deliverable_id`.
- **Obsidian** mints: `note_id`, `area_id` (as JD address slug).
- **Google Calendar** mints: `event_id`.
- Mirrors store references only. Mirrors NEVER remint an ID for the same object facet.
- If a referenced UUID is missing: create a DLQ entry and set `sync_locked=true` on the dependent object.

---

## Conflict Resolution Order

When two systems disagree on the value of a shared field:

1. Safety and governance constraints (hard boundaries; block all other resolution).
2. Google Calendar hard commitments (time claims; block scheduling conflicts).
3. GitHub execution state (issue state overrides Obsidian checklist state).
4. Obsidian narrative and graph integrity (note links preserved; do not overwrite silently).
5. Convenience (never wins a conflict).

**Split-brain tie-break (same facet, two values):**
`canonical timestamp > monotonic version > actor priority (human > system > claude)`

---

## Lifecycle State Machine

### Execution objects (Task, Project, Deliverable)

```
inbox → clarified → next → scheduled → inprogress → done
                                                      ↓
                                               voided (rollback)
                                                      ↓
                                                  archived
```

- `transition(S,S)` = no_op; no audit row.
- Every real transition appends audit JSON:
  ```json
  {
    "transition_id": "<uuid>",
    "timestamp": "<iso8601>",
    "actor": "human | claude | system",
    "from_state": "<state>",
    "to_state": "<state>",
    "reason": "<string>",
    "evidence": {
      "schema_validation_pass": true,
      "source_coverage_count": 3,
      "conflict_check_pass": true
    }
  }
  ```
- `archived` is terminal. No transitions out.
- `voided → archived` is the only permitted path from voided.

### Knowledge objects (Note)

```
inbox → active → archived
           ↓
       quarantine (side state; hidden from queries)
           ↓
   export + exclude-from-queries (terminal)
```

- Fleeting notes older than 7 days are flagged stale and surfaced for IDI processing.
- Quarantine exit: export to cold storage + permanent exclude-from-queries. Human approval required.

---

## Retention Policy

| State | Retention | Visibility | Terminal action |
|---|---|---|---|
| Active | Indefinite | Default queries | → done / archived |
| Voided | 30 days | Hidden from default queries | → archived |
| Quarantine | 30 days | Admin / human only | Export + exclude-from-queries |
| Archived | Indefinite | Archive-specific queries | None; terminal |

**Hard delete is prohibited at every layer.** If you believe a hard delete is necessary, escalate to human. The human must document justification in the audit trail before any permanent removal.
