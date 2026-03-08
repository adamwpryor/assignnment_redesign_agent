# AI-Resilient Course Modernization Pipeline

## Global Context & Directives

**Primary Objective:** Transition online courses from "knowledge regurgitation" to "AI-collaborative critical thinking".
**Pedagogical Constraint:** Prioritize verifiable *process-over-product* assessment.
**Zero-Trust Enforcement:** This is a locally defined system. If an agent or tool attempts to make a call to the wider web for any reason, it MUST halt and notify the user that it is trying to leave the isolated environment, requesting explicit permission before proceeding.

## Bootloader Master Links

This orchestrator links with the Gemini Local Context Hooking environment. It will look for global registries in the user's home directory, but will gracefully ignore them if they do not exist.

- **Global Agent Registry:** `~/.gemini/registry/agents.json` (or `%USERPROFILE%\.gemini\registry\agents.json`)
- **Global Skill Registry:** `~/.gemini/registry/skills.json` (or `%USERPROFILE%\.gemini\registry\skills.json`)
- **Local Agent Extensions:** `.gemini/agents.json`
- **Local Skill Extensions:** `.gemini/skills.json`

## Orchestrator Paradigm

As the Chief of Staff and Orchestrator of this workspace, development is primarily delegated through the Master Bootloader:

- **Capability Manager / Skill Builder:** Responsible for generating required tool packages (`scripts/` and `SKILL.md`). The orchestrator does not invent arbitrary folder structures (like `templates` or `examples`) outside the `skill-builder`'s established package formats.
- **Engineering Manager:** Ensures all script logic adheres to Zero-Trust and Conda-First environments.

## Routing Logic

Standard multi-agent pipeline handoff via structured data (JSON) and markdown:

1. **Agent 1: Vulnerability Assessor** -> Reads: `input/legacy_syllabus.md` -> Writes: `output/vulnerabilities.json`
2. **Agent 2: Resilient Designer** -> Reads: `output/vulnerabilities.json` -> Writes: `output/resilient_activities.md`
3. **Agent 3: Blueprint Compiler** -> Reads: `input/legacy_syllabus.md` + `output/resilient_activities.md` -> Writes: `output/modernized_course_blueprint.md`
