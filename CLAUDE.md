# AI-Resilient Course Modernization Pipeline — Claude Project Context

## What This Is

A multi-agent pipeline that ingests a legacy course assignment and outputs a fully redesigned, AI-resilient version. The core argument: standard essay/discussion-post assignments let LLMs produce a "Mask of Perfection" — fluent, plausible text that bypasses the actual learning objective. The redesigned assignments require students to act as **Architects** who direct, correct, and defend AI output using hyper-local data and course theory.

This project integrates into the global Gemini OS ecosystem but operates as a self-contained local pipeline. Zero-Trust applies: no agent may make external web calls without explicit user permission.

---

## Pipeline Architecture

Sequential handoff — each stage must complete before the next starts:

```
input/legacy_syllabus.md
        │
        ▼
[1] Vulnerability Assessor  ──uses──▶ predictability-scorer
        │ writes
        ▼
output/vulnerabilities.json
        │
        ▼
[2] Resilient Designer  ──uses──▶ local-context-fetcher
        │                          mermaid-baseline-generator
        │ writes
        ▼
output/resilient_activities.md
        │
        ▼
[3] Blueprint Compiler  ──uses──▶ constraint-auditor
        │ reads: input/legacy_syllabus.md + output/resilient_activities.md
        │ writes
        ▼
output/modernized_assignment.md   ← final student-facing document
```

**Before each fresh run:** invoke the Pipeline Cleaner to wipe `output/`. Stale JSON from a prior run will corrupt the next pipeline stage.

---

## Agents

| Agent | Model Tier | Reads | Writes | Role |
|---|---|---|---|---|
| `vulnerability-assessor` | pro | `input/legacy_syllabus.md` | `output/vulnerabilities.json` | Diagnoses and scores — does NOT redesign |
| `resilient-designer` | pro | `output/vulnerabilities.json` | `output/resilient_activities.md` | Designs the 3-Gate replacement — structural, not polished |
| `blueprint-compiler` | flash | `input/` + `output/resilient_activities.md` | `output/modernized_assignment.md` | Final QA pass + student-facing formatting |
| `context-manager` | flash | user input | `mock_payload.json` | Updates institutional context store |
| `pipeline-cleaner` | flash | — | deletes `output/*` | Resets workspace between runs |

**Critical constraint:** The Vulnerability Assessor must **never** write new assignment text. The Resilient Designer must **never** output polished student prose — that belongs to the Blueprint Compiler. Enforce the role boundary strictly.

---

## Skills

All skill scripts return a JSON string. The `__main__` block in each script is a CLI convenience wrapper.

| Skill | Script | Key Function | Notes |
|---|---|---|---|
| `predictability-scorer` | `evaluate_predictability.py` | `evaluate_predictability(text)` | Calls `evaluate_metacognition.py` internally; both must be in sys.path |
| `predictability-scorer` | `evaluate_metacognition.py` | `evaluate_metacognition(text)` | Returns a dict (not JSON string) — called by evaluate_predictability |
| `mermaid-baseline-generator` | `generate_diagram.py` | `generate_mermaid_code(framework_type)` | Pass `"list"` to see available templates |
| `local-context-fetcher` | `fetch_policies.py` | `fetch_local_context()` | Returns mock_payload.json wrapped in MCP-style envelope |
| `constraint-auditor` | `audit_text.py` | `audit_assignment_constraints(text)` | Regex is Mode A — always follow with LLM semantic check (Mode B) |
| `mock-payload-updater` | `update_payload.py` | `update_mock_payload(json_str)` | Writes to `local-context-fetcher/assets/mock_payload.json` — deep merge |
| `workspace-resetter` | `reset_workspace.py` | `reset_workspace()` | Deletes all files under `output/` |

### Running a skill script directly

```bash
# From any working directory:
python .gemini/skills/predictability-scorer/scripts/evaluate_predictability.py --file input/legacy_syllabus.md

# Or pipe stdin:
cat input/legacy_syllabus.md | python .gemini/skills/predictability-scorer/scripts/evaluate_predictability.py

# List available Mermaid templates:
python .gemini/skills/mermaid-baseline-generator/scripts/generate_diagram.py list
```

---

## Key Pedagogical Concepts (Non-Obvious Domain Knowledge)

**Mask of Perfection** — AI-generated text that appears flawless but contains no genuine student cognition. The pipeline's primary threat model.

**Architectural Agency** — The measurable skill being assessed: can the student direct, correct, and defend AI output against course-specific theory? Graded on corrections and defense, not final polish.

**Cognitive Offload Multiplier** — The `evaluate_metacognition` script returns a scalar (can go below 1.0). A score below 1.0 means the assignment has protective features (high Bloom's verbs, relational context, constraint density) that reduce LLM automation risk. The multiplier is applied to the structural base score.

**3-Gate PBL Structure** — The non-negotiable scaffold for every redesigned assignment:
- Gate 1: Hyper-local dataset (must be un-Googleable)
- Gate 2: Prompt architecture + theory-driven error correction (this is where learning happens)
- Gate 3: Non-essay artifact (ADR, Mermaid diagram, policy brief, simulation) + async audio/video defense

**Defensive Friction (forbidden)** — Prompt logs, AI transcript submissions, "reflection on AI use" essays. These shift focus to tool mechanics and invite gaming. The pipeline explicitly removes any assignment requirement that resembles this.

**PASS_WITH_WARNING in constraint-auditor** — This is not a green light. It means the regex found no banned terms, but LLM semantic check (Mode B) is still mandatory. An assignment can require a "written analysis" without using the word "essay."

---

## Institutional Context

The pipeline customizes for a specific institution via `mock_payload.json`:

```
.gemini/skills/local-context-fetcher/assets/mock_payload.json
```

Default institution: **St. John Fisher University** (bell hooks pedagogy, Catholic heritage, AI collaboration required, prefers ADRs and Mermaid maps over essays).

To switch institutions: invoke the Context Manager agent with a JSON payload or natural language description. It calls `update_payload.py` which deep-merges into `mock_payload.json`. The Resilient Designer reads this at runtime via `fetch_local_context()`.

---

## Boodlebox Integration

The `Boodlebox/` directory is a **separate deployment target** — it mirrors the three core agents (Vulnerability Assessor, Resilient Designer, Blueprint Compiler) as standalone persona instructions + knowledge bank files for the Boodlebox web platform.

Key difference: Boodlebox agents have no access to the Python skill scripts. Their "skills" are embedded as `.txt` knowledge bank files. Do not add Python logic to Boodlebox personas — write it in the `.gemini/` skill scripts and then document the logic in the corresponding knowledge bank `.txt` file.

---

## Development Conventions

- **No new folder structures** outside established skill package formats (`scripts/`, `assets/`, `references/`). The orchestrator spec prohibits arbitrary directory invention.
- **All skill scripts return JSON strings.** Functions used by agents must serialize output. The `__main__` CLI wrappers may use `sys.stdin` or `--file` flags but must not change the function signature.
- **No hardcoded institution names** in agent personas. Institutional data belongs in `mock_payload.json`.
- **Output schema for vulnerabilities.json** must match the Resilient Designer's expected input keys: `id`, `original_text`, `qualitative_risk_band`, `core_learning_objective`, `suggested_substitution_framework`.
- **Conda-First**: dependencies go in `environment.yml`. No pip installs in base.
- **Zero-Trust**: any agent needing external data must halt and request user permission — do not silently add web calls.
